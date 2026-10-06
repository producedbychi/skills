# Reference board renderer contract

Read this when preparing a plan for `scripts/render_board.py`. The renderer is an optional local exporter. It does not inspect websites, download images, or establish image-use rights.

## Command

```text
python scripts/render_board.py PLAN --output-dir DIR [--formats pptx,pdf] [--overwrite]
```

The default formats are `pptx,pdf`. Install the packages listed in `scripts/requirements.txt` in the Python environment used to run the helper. The helper prints a JSON manifest with output paths, page counts, and any PDF font fallback.

The output filenames use a sanitized project title, such as `Project-title.pptx` and `Project-title.pdf`. Put each revision in its own output directory to keep older exports. `--overwrite` replaces title-named files in that directory.

## Plan format

Save a UTF-8 JSON file with `version` set to `1`. Use the saved plan as the source for revisions. Before rebuilding, inspect the latest PPTX for user edits and carry them into the plan or rebuilt deck so the render does not erase them.

```json
{
  "version": 1,
  "project": {
    "title": "Project title",
    "client": "Client name",
    "revision": "2026-10-06 v1",
    "status": "Draft for review",
    "brief": "Decision this review should settle"
  },
  "style": {
    "background": "F7F4EE",
    "text": "202020",
    "accent": "93503A",
    "font": "Aptos",
    "pdf_font_regular": "fonts/regular.ttf",
    "pdf_font_bold": "fonts/bold.ttf"
  },
  "references": [
    {
      "id": "R01",
      "path": "images/reference.jpg",
      "title": "Reference title",
      "source": {
        "label": "Publisher or client-supplied",
        "original_file": "reference.jpg",
        "url": "https://example.com/source",
        "creator": "Creator, if known"
      },
      "rights": "Permission status or unknown"
    }
  ],
  "directions": [
    {
      "id": "D01",
      "title": "Direction title",
      "thesis": "Plain-language premise",
      "application": "How this direction serves the project",
      "tradeoff": "Optional limitation or element to leave behind",
      "layout": "pair",
      "cards": [
        {
          "reference_id": "R01",
          "role": "Light reference",
          "observe": "A visible quality in this image",
          "apply": "How that quality informs this project",
          "fit": "contain"
        }
      ]
    }
  ]
}
```

Required fields are `project.title`; each reference's `id`, `path`, and `title`; each direction's `id`, `title`, and `thesis`; and each card's `reference_id`, `observe`, and `apply`. Include at least one reference, direction, and card per direction. A card must point to a declared reference. IDs must be unique across references and directions.

Omitted project fields default to revision `v1`, status `Draft for review`, and an empty client or brief. The style object is optional. Its defaults are background `F7F4EE`, text `202020`, accent `93503A`, and PowerPoint font `Aptos`. Choose type and colors for the project; these fallback values are not client brand guidelines. Colors may include an optional leading `#`.

Omitted direction layout defaults to `pair`. Choose a layout per direction, rather than applying one arrangement to every image set:

| Layout | Arrangement and pagination |
| --- | --- |
| `pair` | Up to two equal-priority references per page. A remaining single card gets a study page. |
| `hero` | One reference per study page. |
| `lead-support` | The first card remains the lead. Each later card gets a comparison page with that lead. Continuation pages repeat the original lead, rather than promoting a support image. A single-card direction gets a study page. |
| `gallery` | Up to three references per page, with equal priority. Extra cards continue in their saved order. |
| `mosaic` | The first card leads, with up to two smaller support references on the same page. Extra supports continue in saved order with the original lead repeated. One card gets a study page; two cards get a lead-and-support page. Application and tradeoff notes sit with the imagery. |

Card fit defaults to `contain`; `cover` crops the image to fill its frame. Choose `cover` when the crop is intentional and the reference remains identifiable in the image or its source details. These layouts are bounded conveniences, not a universal design system. Use another available design tool when the composition needs different image relationships or richer art direction.

The optional card `role` is a short free-text purpose label, such as `Light reference`, `Material detail`, or `Identity only`. It appears with that image's caption. Use it when the role helps the reviewer interpret what to borrow. It does not establish approval or rights. Full reference titles and source details remain in the provenance section.

Source details are optional. A missing label defaults to `Source not specified`; a missing rights statement defaults to `Unknown. Reference use only.` Source URLs must use HTTP or HTTPS. Reference images and the source appendix carry clickable source links where supplied. The appendix includes a thumbnail and one complete source record for each used reference. Unused references stay in the plan.

Each source record also shows the input image's filename. For a renamed copy or detail crop, supply `source.original_file` with the original filename so the reviewer can locate its source. It names a file, not a machine directory or a permission grant.

The opening page previews the first two directions. Full direction pages follow. Observations and applications remain beside their references. Mosaic pages also show direction-level application and tradeoff notes. The other layouts preserve their earlier geometry and place those notes in the source appendix for short sets, or on separate notes pages for longer sets. When those layouts are useful, keep the important choice visible in image-linked notes or use another composition tool for a visual comparison. Every direction's full notes remain accessible in both formats.

## Images, text, and fonts

Use local raster images with absolute paths or paths relative to the plan file. Supported formats are PNG, JPEG, WEBP, GIF, BMP, and TIFF. The renderer uses the first frame of animated images, applies EXIF orientation, and makes temporary PNG copies for export; it leaves the originals unchanged. SVG and remote image URLs are unsupported.

The renderer validates the full plan, image files, references, colors, and text before saving exports. It reports text that exceeds field or page limits instead of clipping or shrinking annotations. Correct the plan and rerun after any validation error.

PPTX keeps text and images as separate editable elements. Both formats use one planned page geometry, image order, crop choice, and set of line breaks. The renderer embeds normalized source images without reducing them to thumbnail resolution. A supplied low-resolution image will still have its original limitations.

Use a font family installed in the presentation environment, with matching local regular and bold TTF files for the PDF. The helper uses declared TTF metrics for line wrapping. Without them, it uses conservative width estimates and PDF Helvetica, so font appearance and text fit still need visual review. If only a regular TTF is supplied, PDF headings also use that regular face and the manifest reports the fallback. Confirm that the chosen fonts cover every character in the plan; the renderer does not infer font support. Supply compatible TTFs for PDF text outside Latin-1.

## Review

- Keep IDs stable across revisions when the underlying reference or direction stays the same. Give new material a new ID.
- Review every exported page and its links against [visual-design.md](visual-design.md). Confirm the images are useful at viewing size, notes stay attached and readable, and no content overlaps or clips.
- Render fresh previews for the current export. Count pages from the actual files so leftover previews from an earlier revision cannot enter the review.
- Inspect native PowerPoint renders as well as the PDF when the host supports it. Otherwise report the narrower structural checks performed. A successful exit code confirms generation, not visual quality or client readiness.
