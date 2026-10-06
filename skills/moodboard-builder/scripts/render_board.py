#!/usr/bin/env python3
"""Render a version 1 reference-board plan as an editable deck and/or PDF."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
import os
import re
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any


class PlanError(ValueError):
    pass


HEX_COLOR = re.compile(r"^#?[0-9a-fA-F]{6}$")
HTTP_URL = re.compile(r"^https?://", re.IGNORECASE)
MAX_LENGTHS = {
    "project.title": 72,
    "project.client": 120,
    "project.revision": 48,
    "project.status": 48,
    "project.brief": 300,
    "style.font": 80,
    "reference.id": 16,
    "reference.path": 1000,
    "reference.title": 40,
    "source.label": 100,
    "source.url": 500,
    "source.creator": 120,
    "source.original_file": 255,
    "reference.rights": 160,
    "direction.id": 16,
    "direction.title": 52,
    "direction.thesis": 190,
    "direction.application": 105,
    "direction.tradeoff": 105,
    "card.observe": 135,
    "card.apply": 135,
    "card.role": 40,
}
SUPPORTED_IMAGES = {"JPEG", "PNG", "WEBP", "GIF", "BMP", "TIFF"}
PAGE_W, PAGE_H = 960.0, 540.0
SW, SH = PAGE_W / 72, PAGE_H / 72


@dataclass
class SceneElement:
    kind: str
    x: float
    y: float
    w: float
    h: float
    text: str = ""
    lines: list[str] = field(default_factory=list)
    font_size: float = 12
    leading: float = 15
    color: str = "202020"
    bold: bool = False
    align: str = "left"
    path: Path | None = None
    reference_id: str = ""
    fit: str = "contain"
    url: str = ""
    fill: str = ""


@dataclass
class ScenePage:
    label: str
    elements: list[SceneElement] = field(default_factory=list)


@dataclass
class BoardScene:
    width: float
    height: float
    pages: list[ScenePage] = field(default_factory=list)


def need_string(value: Any, name: str, *, optional: bool = False) -> str:
    if value is None and optional:
        return ""
    if not isinstance(value, str) or not value.strip():
        raise PlanError(f"{name} must be a non-empty string")
    if len(value) > MAX_LENGTHS.get(name, 500):
        raise PlanError(f"{name} is too long ({len(value)} characters; limit {MAX_LENGTHS.get(name, 500)})")
    return value.strip()


def optional_string(obj: dict[str, Any], key: str, name: str) -> str:
    value = obj.get(key)
    if value is None or value == "":
        return ""
    return need_string(value, name)


def require_object(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise PlanError(f"{name} must be an object")
    return value


def require_array(value: Any, name: str, *, nonempty: bool = True) -> list[Any]:
    if not isinstance(value, list) or (nonempty and not value):
        suffix = "a non-empty array" if nonempty else "an array"
        raise PlanError(f"{name} must be {suffix}")
    return value


def color_value(value: Any, name: str) -> str:
    if not isinstance(value, str) or not HEX_COLOR.fullmatch(value):
        raise PlanError(f"{name} must be a six-digit hex color, such as F7F4EE")
    return value.lstrip("#").upper()


def approximate_lines(text: str, width_points: float, font_size: float) -> int:
    limit = width_points / (font_size * 0.64)
    lines = 1
    used = 0.0
    for word in text.split():
        weight = sum(1.0 if unicodedata.east_asian_width(ch) in ("W", "F") else
                     0.32 if ch.isspace() else
                     0.38 if ch in "il.,:;!'|`" else
                     0.82 if ch in "MW@%&" else
                     0.62 if ch.isupper() else 0.54 for ch in word)
        if weight > limit:
            raise PlanError(f"text contains a word too wide for its layout: {word[:40]!r}")
        if used and used + 0.32 + weight > limit:
            lines += 1
            used = weight
        else:
            used += (0.32 if used else 0) + weight
    return lines


def check_box(text: str, name: str, width_in: float, height_in: float, font_size: float) -> None:
    lines = approximate_lines(text, width_in * 72 - 4, font_size)
    max_lines = int((height_in * 72 - 3) // (font_size * 1.28))
    if lines > max_lines:
        raise PlanError(f"{name} does not fit its text box ({lines} lines needed, {max_lines} fit); shorten the text")


def validate_plan(path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise PlanError(f"cannot read plan {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise PlanError(f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    plan = require_object(raw, "plan")
    if plan.get("version") != 1 or isinstance(plan.get("version"), bool):
        raise PlanError("version must be the number 1")

    project = require_object(plan.get("project"), "project")
    project_data = {
        "title": need_string(project.get("title"), "project.title"),
        "client": optional_string(project, "client", "project.client"),
        "revision": optional_string(project, "revision", "project.revision") or "v1",
        "status": optional_string(project, "status", "project.status") or "Draft for review",
        "brief": optional_string(project, "brief", "project.brief"),
    }
    style = require_object(plan.get("style", {}), "style")
    style_data: dict[str, Any] = {
        "background": color_value(style.get("background", "F7F4EE"), "style.background"),
        "text": color_value(style.get("text", "202020"), "style.text"),
        "accent": color_value(style.get("accent", "93503A"), "style.accent"),
        "font": optional_string(style, "font", "style.font") or "Aptos",
        "pdf_font_regular": optional_string(style, "pdf_font_regular", "style.pdf_font_regular"),
        "pdf_font_bold": optional_string(style, "pdf_font_bold", "style.pdf_font_bold"),
    }

    refs_input = require_array(plan.get("references"), "references")
    dirs_input = require_array(plan.get("directions"), "directions")
    ids: set[str] = set()
    refs: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    plan_dir = path.resolve().parent
    for i, item in enumerate(refs_input, 1):
        item = require_object(item, f"references[{i}]")
        rid = need_string(item.get("id"), "reference.id")
        if rid in ids:
            raise PlanError(f"duplicate ID {rid!r}")
        ids.add(rid)
        rel = need_string(item.get("path"), "reference.path")
        if HTTP_URL.match(rel) or rel.lower().startswith(("data:", "file:")):
            raise PlanError(f"reference {rid}: image path must be a local file, not a URL")
        image_path = Path(rel).expanduser()
        if not image_path.is_absolute():
            image_path = plan_dir / image_path
        image_path = image_path.resolve()
        if not image_path.is_file():
            raise PlanError(f"reference {rid}: image file does not exist: {image_path}")
        if image_path.suffix.lower() in (".svg", ".svgz"):
            raise PlanError(f"reference {rid}: SVG images are unsupported; use a local PNG, JPEG, WEBP, GIF, BMP, or TIFF file")
        try:
            from PIL import Image

            with Image.open(image_path) as im:
                fmt = im.format
                im.verify()
            if fmt not in SUPPORTED_IMAGES:
                raise PlanError(f"reference {rid}: unsupported image type {fmt or image_path.suffix}; use PNG, JPEG, WEBP, GIF, BMP, or TIFF")
            with Image.open(image_path) as im:
                width, height = im.size
                im.load()
        except PlanError:
            raise
        except Exception as exc:
            raise PlanError(f"reference {rid}: image is unreadable: {exc}") from exc
        if width < 1 or height < 1:
            raise PlanError(f"reference {rid}: image has invalid dimensions")
        source = require_object(item.get("source", {}), f"reference {rid}.source")
        url = optional_string(source, "url", "source.url")
        if url and not HTTP_URL.match(url):
            raise PlanError(f"reference {rid}: source.url must begin with http:// or https://")
        original_file = optional_string(source, "original_file", "source.original_file") or image_path.name
        if original_file in (".", "..") or "/" in original_file or "\\" in original_file:
            raise PlanError(f"reference {rid}: source.original_file must be a filename, not a path")
        ref = {
            "id": rid,
            "path": image_path,
            "title": need_string(item.get("title"), "reference.title"),
            "source": {
                "label": optional_string(source, "label", "source.label") or "Source not specified",
                "url": url,
                "creator": optional_string(source, "creator", "source.creator"),
                "original_file": original_file,
            },
            "rights": optional_string(item, "rights", "reference.rights") or "Unknown. Reference use only.",
            "width": width,
            "height": height,
        }
        refs.append(ref)
        by_id[rid] = ref

    directions: list[dict[str, Any]] = []
    for i, item in enumerate(dirs_input, 1):
        item = require_object(item, f"directions[{i}]")
        did = need_string(item.get("id"), "direction.id")
        if did in ids:
            raise PlanError(f"duplicate ID {did!r}")
        ids.add(did)
        layout = item.get("layout", "pair")
        if layout not in ("pair", "hero", "lead-support", "gallery", "mosaic"):
            raise PlanError(f"direction {did}: layout must be pair, hero, lead-support, gallery, or mosaic")
        cards_in = require_array(item.get("cards"), f"direction {did}.cards")
        cards: list[dict[str, Any]] = []
        for j, card in enumerate(cards_in, 1):
            card = require_object(card, f"direction {did}.cards[{j}]")
            ref_id = need_string(card.get("reference_id"), "card.reference_id")
            if ref_id not in by_id:
                raise PlanError(f"direction {did}: card references unknown reference ID {ref_id!r}")
            fit = card.get("fit", "contain")
            if fit not in ("contain", "cover"):
                raise PlanError(f"direction {did}, reference {ref_id}: fit must be 'contain' or 'cover'")
            cards.append({
                "reference_id": ref_id,
                "observe": need_string(card.get("observe"), "card.observe"),
                "apply": need_string(card.get("apply"), "card.apply"),
                "role": optional_string(card, "role", "card.role"),
                "fit": fit,
            })
        directions.append({
            "id": did,
            "title": need_string(item.get("title"), "direction.title"),
            "thesis": need_string(item.get("thesis"), "direction.thesis"),
            "application": optional_string(item, "application", "direction.application"),
            "tradeoff": optional_string(item, "tradeoff", "direction.tradeoff"),
            "layout": layout,
            "cards": cards,
        })
    for key in ("pdf_font_regular", "pdf_font_bold"):
        font = style_data[key]
        if font:
            font_path = Path(font).expanduser()
            if not font_path.is_absolute():
                font_path = plan_dir / font_path
            font_path = font_path.resolve()
            if not font_path.is_file() or font_path.suffix.lower() != ".ttf":
                raise PlanError(f"style.{key} must point to a local .ttf file: {font_path}")
            style_data[key] = font_path
    return {"project": project_data, "style": style_data, "references": refs, "directions": directions}


def require_packages(formats: list[str]) -> tuple[Any, Any, Any]:
    missing = []
    try:
        from PIL import Image, ImageOps
    except ImportError:
        Image = ImageOps = None
        missing.append("Pillow")
    pptx = None
    if "pptx" in formats:
        try:
            from pptx import Presentation
            from pptx.dml.color import RGBColor
            from pptx.enum.text import PP_ALIGN
            from pptx.util import Inches
            pptx = (Presentation, RGBColor, PP_ALIGN, Inches)
        except ImportError:
            missing.append("python-pptx")
    report = None
    if "pdf" in formats:
        try:
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            from reportlab.lib.utils import ImageReader, simpleSplit
            from reportlab.pdfgen import canvas
            report = (pdfmetrics, TTFont, ImageReader, simpleSplit, canvas)
        except ImportError:
            missing.append("reportlab")
    if missing:
        raise PlanError("missing package(s): " + ", ".join(missing) + ". Install them with: python -m pip install -r scripts/requirements.txt")
    return Image, ImageOps, (pptx, report)


def chunks(items: list[Any], size: int) -> list[list[Any]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def normalize_images(plan: dict[str, Any], directory: Path, modules: tuple[Any, Any]) -> None:
    Image, ImageOps = modules
    directory.mkdir(parents=True, exist_ok=True)
    for index, ref in enumerate(plan["references"], 1):
        target = directory / f"reference-{index:04d}.png"
        try:
            with Image.open(ref["path"]) as source:
                normalized = ImageOps.exif_transpose(source).convert("RGBA")
                normalized.save(target, format="PNG")
                ref["width"], ref["height"] = normalized.size
        except Exception as exc:
            raise PlanError(f"reference {ref['id']}: cannot normalize image: {exc}") from exc
        ref["render_path"] = target


def check_pdf_glyphs(plan: dict[str, Any], formats: list[str]) -> None:
    if "pdf" not in formats or plan["style"]["pdf_font_regular"]:
        return
    values = [plan["project"][key] for key in ("title", "client", "revision", "status", "brief")]
    for ref in plan["references"]:
        values.extend((ref["id"], ref["title"], ref["source"]["label"], ref["source"]["creator"],
                       ref["source"]["original_file"], ref["rights"]))
    for direction in plan["directions"]:
        values.extend((direction["id"], direction["title"], direction["thesis"], direction["application"], direction["tradeoff"]))
        for card in direction["cards"]:
            values.extend((card["observe"], card["apply"], card["role"]))
    if any(ord(char) > 255 for value in values for char in value):
        raise PlanError("PDF text contains non-Latin-1 characters; set style.pdf_font_regular to a compatible local .ttf file")


def text_color(hex_color: str, rgb_class: Any) -> Any:
    return rgb_class.from_string(hex_color)


def _word_weight(word: str) -> float:
    return sum(1.0 if unicodedata.east_asian_width(ch) in ("W", "F") else
               0.32 if ch.isspace() else
               0.38 if ch in "il.,:;!'|`" else
               0.82 if ch in "MW@%&" else
               0.62 if ch.isupper() else 0.54 for ch in word)


_scene_font_paths: dict[bool, Path] = {}
_scene_font_cache: dict[tuple[bool, int], Any] = {}


def _scene_text_width(text: str, size: float, bold: bool) -> float:
    font_path = _scene_font_paths.get(bold) or _scene_font_paths.get(False)
    if font_path:
        try:
            from PIL import ImageFont

            cache_key = (bold, max(1, round(size * 4)))
            if cache_key not in _scene_font_cache:
                _scene_font_cache[cache_key] = ImageFont.truetype(str(font_path), cache_key[1])
            return _scene_font_cache[cache_key].getlength(text) / 4
        except Exception:
            pass
    return size * 1.1 * sum(_word_weight(word) + (0.32 if index else 0)
                            for index, word in enumerate(text.split()))


def wrap_scene_text(text: str, width: float, size: float, bold: bool = False) -> list[str]:
    lines: list[str] = []
    current: list[str] = []
    for word in text.split():
        candidate = " ".join((*current, word))
        if _scene_text_width(word, size, bold) > width:
            raise PlanError(f"text contains a word too wide for its layout: {word[:40]!r}")
        if current and _scene_text_width(candidate, size, bold) > width:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines or [""]


def wrap_filename(text: str, width: float, size: float) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        candidate = current + char
        if current and _scene_text_width(candidate, size, False) > width:
            lines.append(current)
            current = char
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines or [""]


def add_scene_text(page: ScenePage, text: str, x: float, y: float, w: float, h: float, *,
                   size: float, color: str, bold: bool = False, align: str = "left",
                   leading: float | None = None, url: str = "") -> None:
    leading = leading or size * 1.22
    lines = wrap_scene_text(text, w, size, bold)
    if len(lines) * leading > h + 0.5:
        raise PlanError(f"layout text does not fit ({len(lines)} lines in {h:.0f} pt): {text[:80]}")
    page.elements.append(SceneElement("text", x, y, w, h, text, lines, size, leading, color, bold, align, url=url))


def add_scene_image(page: ScenePage, ref: dict[str, Any], x: float, y: float, w: float, h: float,
                    fit: str = "contain") -> SceneElement:
    if fit == "contain":
        frame_x, frame_y, frame_w, frame_h = x, y, w, h
        scale = min(frame_w / ref["width"], frame_h / ref["height"])
        w, h = ref["width"] * scale, ref["height"] * scale
        x, y = frame_x + (frame_w - w) / 2, frame_y + (frame_h - h) / 2
    image = SceneElement("image", x, y, w, h, path=ref.get("render_path", ref["path"]),
                         reference_id=ref["id"], fit=fit)
    page.elements.append(image)
    return image


def add_caption(page: ScenePage, card: dict[str, Any], ref: dict[str, Any], x: float, y: float,
                w: float, *, ink: str, accent: str, size: float = 10.5, max_height: float = 95) -> None:
    title = f"{ref['id']}  ·  {ref['title']}"
    if card["role"]:
        title += f"  ·  {card['role']}"
    title_lines = wrap_scene_text(title, w, 10.5, True)
    title_height = len(title_lines) * 13
    add_scene_text(page, title, x, y, w, title_height, size=10.5, color=accent, bold=True, leading=13)
    text = f"Notice: {card['observe']}  Use: {card['apply']}"
    body_y = y + title_height + 3
    add_scene_text(page, text, x, body_y, w, max_height - (body_y - y), size=size, color=ink,
                   leading=size * 1.24)


def add_mosaic_card(page: ScenePage, card: dict[str, Any], ref: dict[str, Any],
                    title_x: float, title_y: float, title_w: float, title_h: float,
                    body_x: float, body_w: float, card_bottom: float,
                    *, ink: str, accent: str, title_size: float = 9.3,
                    body_size: float = 8.6) -> None:
    title = f"{ref['id']}  ·  {ref['title']}"
    if card["role"]:
        title += f"  ·  {card['role']}"
    title_lines = wrap_scene_text(title, title_w, title_size, True)
    title_leading = title_size * 1.18
    actual_title_h = len(title_lines) * title_leading
    if actual_title_h > title_h + 0.5:
        raise PlanError(f"mosaic card title does not fit: {title[:80]}")
    add_scene_text(page, title, title_x, title_y, title_w, title_h, size=title_size,
                   color=accent, bold=True, leading=title_leading)
    body = f"Notice: {card['observe']}  Use: {card['apply']}"
    body_y = title_y + actual_title_h + 2
    add_scene_text(page, body, body_x, body_y, body_w,
                   card_bottom - body_y, size=body_size, color=ink,
                   leading=body_size * 1.23)


def mosaic_groups(cards: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    if len(cards) <= 3:
        return [cards]
    lead = cards[0]
    return [[lead, *cards[index:index + 2]] for index in range(1, len(cards), 2)]


def _make_scene(plan: dict[str, Any], manifest: dict[str, Any]) -> BoardScene:
    global _scene_font_paths, _scene_font_cache
    style, project = plan["style"], plan["project"]
    _scene_font_paths = {}
    _scene_font_cache = {}
    if style["pdf_font_regular"]:
        _scene_font_paths[False] = style["pdf_font_regular"]
    if style["pdf_font_bold"]:
        _scene_font_paths[True] = style["pdf_font_bold"]
    ink, accent, bg = style["text"], style["accent"], style["background"]
    scene = BoardScene(PAGE_W, PAGE_H)
    by_id = {ref["id"]: ref for ref in plan["references"]}

    def page(label: str) -> ScenePage:
        value = ScenePage(label)
        scene.pages.append(value)
        return value

    # Cover presents the decision beside one representative from each direction.
    cover = page("Overview")
    add_scene_text(cover, project["title"], 46, 34, 870, 50, size=33, color=ink, bold=True, leading=38)
    identity = "  ·  ".join(part for part in (project["client"], project["status"]) if part)
    if identity:
        add_scene_text(cover, identity, 48, 84, 850, 22, size=10, color=accent, bold=True)
    if project["brief"]:
        add_scene_text(cover, "DECISION", 48, 116, 140, 16, size=9, color=accent, bold=True)
        brief_lines = wrap_scene_text(project["brief"], 650, 15)
        brief_height = len(brief_lines) * 18
        add_scene_text(cover, project["brief"], 48, 134, 650, brief_height, size=15, color=ink, leading=18)
    else:
        brief_height = 0
    gap, frame_w, frame_h = 24, 421, 226
    image_y = max(181, 144 + brief_height)
    frame_h = max(160, 407 - image_y)
    for index, direction in enumerate(plan["directions"][:2]):
        card = direction["cards"][0]
        ref = by_id[card["reference_id"]]
        x = 48 + index * (frame_w + gap)
        image = add_scene_image(cover, ref, x, image_y, frame_w, frame_h, card["fit"])
        add_scene_text(cover, "DIRECTION OVERVIEW", image.x, 414, image.w, 15, size=8.5, color=accent, bold=True)
        title_lines = wrap_scene_text(direction["title"], image.w, 15, True)
        title_y = 431
        title_height = len(title_lines) * 19
        add_scene_text(cover, direction["title"], image.x, title_y, image.w, title_height,
                       size=15, color=ink, bold=True, leading=19)
        summary_y = title_y + title_height + 3
        summary_size, summary_leading = 9, 10.5
        summary_lines = wrap_scene_text(direction["thesis"], image.w, summary_size)
        available = 510 - summary_y
        if len(summary_lines) * summary_leading <= available:
            add_scene_text(cover, direction["thesis"], image.x, summary_y, image.w, available,
                           size=summary_size, color=ink, leading=summary_leading)
    if len(plan["directions"]) > 2:
        add_scene_text(cover, f"+ {len(plan['directions']) - 2} more directions in this review", 48, 497, 850, 14,
                       size=8, color=accent)

    # The requested layout belongs to each direction. Legacy pair/hero plans keep their meaning.
    page_sizes = {"pair": 2, "hero": 1, "lead-support": 1, "gallery": 3}
    for direction in plan["directions"]:
        if direction["layout"] == "lead-support" and len(direction["cards"]) > 1:
            lead = direction["cards"][0]
            groups = [[lead, support] for support in direction["cards"][1:]]
        elif direction["layout"] == "mosaic":
            groups = mosaic_groups(direction["cards"])
        else:
            groups = chunks(direction["cards"], page_sizes[direction["layout"]])
        for group_index, group in enumerate(groups):
            board_page = page(direction["title"])
            add_scene_text(board_page, direction["title"], 42, 34, 875, 37, size=27, color=ink, bold=True, leading=32)
            if group_index:
                add_scene_text(board_page, "continued", 790, 43, 124, 17, size=9, color=accent, align="right")
            add_scene_text(board_page, direction["thesis"], 43, 75, 870, 33, size=12.5, color=ink, leading=15)
            n = len(group)
            if direction["layout"] == "mosaic":
                notes: list[str] = []
                if direction["application"]:
                    notes.append("Application: " + direction["application"])
                if direction["tradeoff"]:
                    notes.append("Tradeoff: " + direction["tradeoff"])
                if notes:
                    add_scene_text(board_page, "   ·   ".join(notes), 43, 110, 874, 29,
                                   size=8.5, color=ink, leading=10.3)
                if n == 1:
                    card = group[0]
                    ref = by_id[card["reference_id"]]
                    image = add_scene_image(board_page, ref, 94, 143, 772, 286, card["fit"])
                    add_caption(board_page, card, ref, 43, 436, 874,
                                ink=ink, accent=accent, size=9.1, max_height=68)
                elif n == 2:
                    lead, support = group
                    lead_ref = by_id[lead["reference_id"]]
                    lead_image = add_scene_image(board_page, lead_ref, 43, 143, 550, 270, lead["fit"])
                    add_caption(board_page, lead, lead_ref, 43, 419, 550,
                                ink=ink, accent=accent, size=8.9, max_height=85)
                    support_ref = by_id[support["reference_id"]]
                    support_image = add_scene_image(board_page, support_ref, 620, 143, 297, 235, support["fit"])
                    add_caption(board_page, support, support_ref, 620, 384, 297,
                                ink=ink, accent=accent, size=8.7, max_height=120)
                else:
                    lead = group[0]
                    lead_ref = by_id[lead["reference_id"]]
                    lead_image = add_scene_image(board_page, lead_ref, 43, 143, 440, 220, lead["fit"])
                    add_caption(board_page, lead, lead_ref, 43, 369, 440,
                                ink=ink, accent=accent, size=8.9, max_height=132)
                    for idx, card in enumerate(group[1:]):
                        ref = by_id[card["reference_id"]]
                        row_y = 143 + idx * 181
                        add_scene_image(board_page, ref, 506, row_y, 411, 122, card["fit"])
                        add_mosaic_card(board_page, card, ref,
                                        506, row_y + 126, 411, 22,
                                        506, 411, row_y + 177,
                                        ink=ink, accent=accent, title_size=8.5,
                                        body_size=8.1)
            elif direction["layout"] == "hero" or n == 1:
                card = group[0]
                ref = by_id[card["reference_id"]]
                image = add_scene_image(board_page, ref, 145, 112, 670, 300, card["fit"])
                add_caption(board_page, card, ref, image.x, image.y + image.h + 4, image.w,
                            ink=ink, accent=accent, size=9.5, max_height=98)
            elif direction["layout"] == "lead-support":
                lead = group[0]
                lead_ref = by_id[lead["reference_id"]]
                lead_image = add_scene_image(board_page, lead_ref, 43, 112, 480, 292, lead["fit"])
                add_caption(board_page, lead, lead_ref, lead_image.x, lead_image.y + lead_image.h + 4,
                            lead_image.w, ink=ink, accent=accent,
                            size=9.25, max_height=106)
                supports = group[1:]
                support_w, support_h = 360, 260
                for idx, card in enumerate(supports):
                    ref = by_id[card["reference_id"]]
                    image = add_scene_image(board_page, ref, 556, 112, support_w, support_h, card["fit"])
                    add_caption(board_page, card, ref, image.x, image.y + image.h + 4, image.w,
                                ink=ink, accent=accent,
                                size=9.25, max_height=116)
            elif direction["layout"] == "gallery":
                gap = 18
                card_w = (875 - gap * (n - 1)) / n
                for idx, card in enumerate(group):
                    x = 43 + idx * (card_w + gap)
                    ref = by_id[card["reference_id"]]
                    image = add_scene_image(board_page, ref, x, 122, card_w, 258, card["fit"])
                    add_caption(board_page, card, ref, image.x, image.y + image.h + 4, image.w,
                                ink=ink, accent=accent,
                                size=9.25, max_height=116)
            else:  # `pair`, including version 1 plans that omit `layout`.
                gap = 32
                card_w = (875 - gap) / 2
                for idx, card in enumerate(group):
                    x = 43 + idx * (card_w + gap)
                    ref = by_id[card["reference_id"]]
                    image = add_scene_image(board_page, ref, x, 112, card_w, 300, card["fit"])
                    add_caption(board_page, card, ref, image.x, image.y + image.h + 4, image.w,
                                ink=ink, accent=accent,
                                size=9.25, max_height=98)

    used = {card["reference_id"] for direction in plan["directions"] for card in direction["cards"]}
    source_refs = [ref for ref in plan["references"] if ref["id"] in used]
    note_directions = [direction for direction in plan["directions"] if direction["application"] or direction["tradeoff"]]
    merge_notes_into_sources = bool(source_refs) and len(note_directions) <= 2
    if not merge_notes_into_sources:
        for note_group in chunks(note_directions, 4):
            notes_page = page("Direction notes")
            add_scene_text(notes_page, "Direction notes", 42, 34, 870, 38, size=25, color=ink, bold=True)
            for idx, direction in enumerate(note_group):
                y = 86 + idx * 103
                add_scene_text(notes_page, direction["title"], 44, y, 868, 18, size=11, color=accent, bold=True)
                lines = []
                if direction["application"]:
                    lines.append("Application: " + direction["application"])
                if direction["tradeoff"]:
                    lines.append("Tradeoff: " + direction["tradeoff"])
                add_scene_text(notes_page, "   ·   ".join(lines), 44, y + 20, 868, 76,
                               size=10, color=ink, leading=12)

    if source_refs:
        groups = chunks(source_refs, 4)
        for group_index, group in enumerate(groups):
            appendix = page("Sources and notes")
            add_scene_text(appendix, "Sources and rights", 42, 34, 870, 38, size=25, color=ink, bold=True)
            source_top = 87
            if group_index == 0 and merge_notes_into_sources:
                for idx, direction in enumerate(note_directions):
                    y = 82 + idx * 27
                    add_scene_text(appendix, direction["title"], 44, y, 174, 18,
                                   size=9, color=accent, bold=True)
                    lines = []
                    if direction["application"]:
                        lines.append("Application: " + direction["application"])
                    if direction["tradeoff"]:
                        lines.append("Tradeoff: " + direction["tradeoff"])
                    add_scene_text(appendix, "   ·   ".join(lines), 220, y, 690, 24,
                                   size=8.5, color=ink, leading=10)
                source_top = 145
            for idx, ref in enumerate(group):
                y = source_top + idx * 92
                add_scene_image(appendix, ref, 44, y, 72, 72, "contain")
                add_scene_text(appendix, f"{ref['id']}  ·  {ref['title']}", 130, y, 770, 18,
                               size=11, color=accent, bold=True)
                attribution = ref["source"]["label"]
                if ref["source"]["creator"]:
                    attribution += "  ·  " + ref["source"]["creator"]
                if ref["source"]["url"]:
                    attribution += "  ·  Open source"
                add_scene_text(appendix, attribution, 130, y + 21, 770, 16, size=9, color=ink,
                               url=ref["source"]["url"])
                add_scene_text(appendix, "Rights: " + ref["rights"], 130, y + 39, 770, 22,
                               size=8.5, color=ink, leading=10.5)
                original_file_text = "Original file: " + ref["source"]["original_file"]
                original_file_lines = wrap_filename(original_file_text, 770, 8.2)
                if len(original_file_lines) * 9.5 > 30:
                    raise PlanError(f"source.original_file is too long for its source record: {ref['source']['original_file']}")
                appendix.elements.append(SceneElement(
                    "text", 130, y + 62, 770, 30, original_file_text, original_file_lines,
                    8.2, 9.5, ink,
                ))

    for index, board_page in enumerate(scene.pages, 1):
        add_scene_text(board_page, f"{project['revision']}  ·  {index}", 700, 517, 216, 13,
                       size=8, color=ink, align="right")
    manifest["scene"] = scene
    return scene


def render_pptx(plan: dict[str, Any], destination: Path, manifest: dict[str, Any]) -> None:
    Presentation, RGBColor, PP_ALIGN, Inches = manifest["packages"][0]
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    blank = prs.slide_layouts[6]
    style = plan["style"]
    bg, font = text_color(style["background"], RGBColor), style["font"]
    scene: BoardScene = manifest["scene"]
    alignment = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}
    for scene_page in scene.pages:
        slide = prs.slides.add_slide(blank)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = bg
        for element in scene_page.elements:
            if element.kind == "image":
                ref = next(ref for ref in plan["references"] if ref["id"] == element.reference_id)
                shape = slide.shapes.add_picture(str(element.path), Inches(element.x / 72), Inches(element.y / 72),
                                                 width=Inches(element.w / 72), height=Inches(element.h / 72))
                if element.fit == "contain":
                    ratio, box_ratio = ref["width"] / ref["height"], element.w / element.h
                    if ratio > box_ratio:
                        target_h = element.w / ratio
                        shape.top, shape.height = Inches((element.y + (element.h - target_h) / 2) / 72), Inches(target_h / 72)
                    else:
                        target_w = element.h * ratio
                        shape.left, shape.width = Inches((element.x + (element.w - target_w) / 2) / 72), Inches(target_w / 72)
                else:
                    ratio, box_ratio = ref["width"] / ref["height"], element.w / element.h
                    if ratio > box_ratio:
                        visible = box_ratio / ratio
                        shape.crop_left = shape.crop_right = (1 - visible) / 2
                    else:
                        visible = ratio / box_ratio
                        shape.crop_top = shape.crop_bottom = (1 - visible) / 2
                if ref["source"]["url"]:
                    shape.click_action.hyperlink.address = ref["source"]["url"]
                continue
            if element.kind == "rect":
                from pptx.enum.shapes import MSO_SHAPE
                shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(element.x / 72), Inches(element.y / 72),
                                               Inches(element.w / 72), Inches(element.h / 72))
                shape.fill.solid()
                shape.fill.fore_color.rgb = text_color(element.fill, RGBColor)
                shape.line.fill.background()
                continue
            from pptx.enum.text import MSO_ANCHOR
            from pptx.util import Pt
            box = slide.shapes.add_textbox(Inches(element.x / 72), Inches(element.y / 72),
                                           Inches(element.w / 72), Inches(element.h / 72))
            frame = box.text_frame
            frame.clear()
            frame.word_wrap = False
            frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
            frame.vertical_anchor = MSO_ANCHOR.TOP
            paragraph = frame.paragraphs[0]
            paragraph.text = "\n".join(element.lines)
            paragraph.alignment = alignment[element.align]
            paragraph.line_spacing = Pt(element.leading)
            for run in paragraph.runs:
                run.font.name = font
                run.font.size = Pt(element.font_size)
                run.font.bold = element.bold
                run.font.color.rgb = text_color(element.color, RGBColor)
                if element.url:
                    run.hyperlink.address = element.url
        
    project = plan["project"]
    prs.core_properties.title = project["title"]
    prs.core_properties.subject = "Reference board"
    prs.core_properties.author = project["client"] or ""
    prs.save(str(destination))
    manifest["pages"]["pptx"] = len(scene.pages)


def render_pdf(plan: dict[str, Any], destination: Path, manifest: dict[str, Any]) -> None:
    from reportlab.lib.colors import HexColor
    pdfmetrics, TTFont, ImageReader, _, canvas_module = manifest["packages"][1]
    project, style = plan["project"], plan["style"]
    warnings: list[str] = []
    if style["pdf_font_regular"]:
        pdfmetrics.registerFont(TTFont("BoardRegular", str(style["pdf_font_regular"])))
        regular = "BoardRegular"
    else:
        regular = "Helvetica"
        warnings.append(f"PDF uses Helvetica because no PDF TTF was supplied; requested style font is {style['font']}.")
    if style["pdf_font_bold"]:
        pdfmetrics.registerFont(TTFont("BoardBold", str(style["pdf_font_bold"])))
        bold = "BoardBold"
    elif style["pdf_font_regular"]:
        bold = "BoardRegular"
        warnings.append("PDF uses the supplied regular TTF for bold text because no bold TTF was supplied.")
    else:
        bold = "Helvetica-Bold"
    manifest["pdf_font"] = {"regular": regular, "bold": bold, "warnings": warnings}
    c = canvas_module.Canvas(str(destination), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle(project["title"])
    c.setAuthor(project["client"] or "Reference board")
    scene: BoardScene = manifest["scene"]
    references = {ref["id"]: ref for ref in plan["references"]}
    for scene_page in scene.pages:
        c.setFillColor(HexColor("#" + style["background"]))
        c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        for element in scene_page.elements:
            if element.kind == "rect":
                c.setFillColor(HexColor("#" + element.fill))
                c.rect(element.x, PAGE_H - element.y - element.h, element.w, element.h, stroke=0, fill=1)
            elif element.kind == "image":
                ref = references[element.reference_id]
                reader = ImageReader(str(element.path))
                source_w, source_h = reader.getSize()
                if element.fit == "cover":
                    scale = max(element.w / source_w, element.h / source_h)
                    target_w, target_h = source_w * scale, source_h * scale
                    x = element.x + (element.w - target_w) / 2
                    y = PAGE_H - element.y - (element.h + target_h) / 2
                    c.saveState()
                    clip = c.beginPath()
                    clip.rect(element.x, PAGE_H - element.y - element.h, element.w, element.h)
                    c.clipPath(clip, stroke=0, fill=0)
                    c.drawImage(reader, x, y, width=target_w, height=target_h, mask="auto")
                    c.restoreState()
                    link_box = (element.x, PAGE_H - element.y - element.h,
                                element.x + element.w, PAGE_H - element.y)
                else:
                    x, y = element.x, PAGE_H - element.y - element.h
                    target_w, target_h = element.w, element.h
                    c.drawImage(reader, x, y, width=target_w, height=target_h, mask="auto")
                    link_box = (x, y, x + target_w, y + target_h)
                if ref["source"]["url"]:
                    c.linkURL(ref["source"]["url"], link_box, relative=0, thickness=0)
            else:
                font_name = bold if element.bold else regular
                c.setFillColor(HexColor("#" + element.color))
                c.setFont(font_name, element.font_size)
                for idx, line in enumerate(element.lines):
                    y = PAGE_H - element.y - element.font_size - idx * element.leading
                    if element.align == "right":
                        c.drawRightString(element.x + element.w, y, line)
                    elif element.align == "center":
                        c.drawCentredString(element.x + element.w / 2, y, line)
                    else:
                        c.drawString(element.x, y, line)
                    if element.url:
                        text_width = pdfmetrics.stringWidth(line, font_name, element.font_size)
                        left = element.x if element.align == "left" else element.x + (element.w - text_width) / 2
                        c.linkURL(element.url, (left, y - 2, left + text_width, y + element.font_size + 2), relative=0, thickness=0)
        c.showPage()
    c.save()
    manifest["pages"]["pdf"] = len(scene.pages)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a version 1 reference-board JSON plan as PPTX and/or PDF.",
        epilog=("Image paths are local and resolve relative to the plan JSON. Cards use contain by default; "
                "cover must be requested per card. Directions default to pair layout. Project defaults are revision v1 "
                "and status Draft for review. Style defaults are background F7F4EE, text 202020, accent 93503A, "
                "and font Aptos. Missing source labels default to Source not specified; missing rights default to "
                "Unknown. Reference use only. Existing files are kept unless --overwrite is passed. "
                "PDF uses Helvetica unless local TTF paths are declared in style.")
    )
    parser.add_argument("plan", type=Path, help="path to the plan JSON")
    parser.add_argument("--output-dir", type=Path, required=True, help="directory for generated files")
    parser.add_argument("--formats", default="pptx,pdf", help="comma-separated formats: pptx,pdf (default: pptx,pdf)")
    parser.add_argument("--overwrite", action="store_true", help="replace output files that already exist")
    args = parser.parse_args(argv)
    formats = [part.strip().lower() for part in args.formats.split(",") if part.strip()]
    if not formats or any(f not in ("pptx", "pdf") for f in formats) or len(set(formats)) != len(formats):
        parser.error("--formats must be a comma-separated list of unique values from pptx,pdf")
    try:
        image_modules = require_packages(formats)
        plan = validate_plan(args.plan.expanduser().resolve())
        check_pdf_glyphs(plan, formats)
        output_dir = args.output_dir.expanduser().resolve()
        stem = re.sub(r"[^A-Za-z0-9._-]+", "-", plan["project"]["title"]).strip("-._") or "reference-board"
        targets = {fmt: output_dir / f"{stem}.{fmt}" for fmt in formats}
        if not args.overwrite:
            existing = [str(p) for p in targets.values() if p.exists()]
            if existing:
                raise PlanError("output file already exists; pass --overwrite to replace it: " + ", ".join(existing))
        output_dir.mkdir(parents=True, exist_ok=True)
        collisions = [str(p) for p in targets.values() if p.exists() and not args.overwrite]
        if collisions:
            raise PlanError("output file already exists; pass --overwrite to replace it: " + ", ".join(collisions))
        manifest: dict[str, Any] = {"project": plan["project"]["title"], "status": plan["project"]["status"], "files": {}, "pages": {}, "warnings": []}
        manifest["packages"] = image_modules[2]
        manifest["image_modules"] = image_modules[:2]
        with tempfile.TemporaryDirectory(prefix="reference-board-", dir=str(output_dir)) as tmp:
            normalize_images(plan, Path(tmp) / "assets", image_modules[:2])
            _make_scene(plan, manifest)
            staged: dict[str, Path] = {}
            for fmt in formats:
                stage = Path(tmp) / targets[fmt].name
                if fmt == "pptx":
                    render_pptx(plan, stage, manifest)
                else:
                    render_pdf(plan, stage, manifest)
                staged[fmt] = stage
            if not args.overwrite:
                collisions = [str(p) for p in targets.values() if p.exists()]
                if collisions:
                    raise PlanError("output file already exists; pass --overwrite to replace it: " + ", ".join(collisions))
            for fmt, stage in staged.items():
                os.replace(stage, targets[fmt])
                manifest["files"][fmt] = str(targets[fmt])
        manifest.pop("packages", None)
        manifest.pop("image_modules", None)
        manifest.pop("scene", None)
        if "pdf_font" in manifest:
            manifest["warnings"].extend(manifest["pdf_font"]["warnings"])
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
        return 0
    except PlanError as exc:
        print(f"render_board: error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"render_board: error: render failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
