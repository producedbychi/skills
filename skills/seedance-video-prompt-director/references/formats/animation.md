# Animation format

Stylized 3D or 2D output. Cel-shaded anime, claymation, low-poly 3D, manga ink, paper cutout, stop-motion, Chinese xianxia animation, etc. Each segment timed explicitly, style locked at the top of the prompt and reinforced at the bottom.

---

## When to use

- The brief calls for stylized non-photoreal output (anime, claymation, low-poly, etc.)
- The user provides a keyframe in a specific animation style and wants the video to match
- The genre is fantasy / xianxia / cyberpunk where stylized rendering serves the story
- The video is a transformation across animation styles (live-action → claymation → anime)

Don't use for photoreal commercial / cinematic / documentary content. Use multi-shot, continuous, or POV instead.

---

## Structure

```
[Style declaration line — locks the aesthetic]

[Style reference + character reference clarification — what each image is for]

[Subject + environment + atmosphere paragraph in the locked style]

0–Xs: [first segment, timed explicitly]

X–Ys: [second segment]

Y–Zs: [third segment]

Z–[final]s: [climax / resolution segment]

[Style footer — reinforces the aesthetic]

[Optional SFX block]

[Optional negative prompt block]

Total: [Xs] / 1 shot or N shots / [aspect ratio] / 24fps
```

---

## Style declaration line

The opening line locks the animation aesthetic. Be specific.

**Patterns:**

- "Bold 2D anime illustration, cel-shaded flat coloring, thick confident outlines, warm amber and muted earth tones with cool electric blue holographic accents, anime speed lines and impact frames, 2.35:1 widescreen, 24fps."
- "3D claymation cinematic — soft clay texture on every surface, visible fingerprint and tool marks on clay forms, slightly exaggerated organic proportions, warm dramatic lighting, 2.35:1 widescreen, 24fps."
- "Chibi low-poly 3D aesthetic — small rounded chunky bodies with oversized expressive heads, smooth soft polygon surfaces, cinematic warm lighting, soft depth of field, 2.35:1 widescreen, 24fps."
- "1980s–90s seinen manga ink — bold black lines, cross-hatching, screentone dots, no color, no grey, high contrast black & white on aged paper, thick pen nib linework, ink bleed on heavy blacks, Akira / Ghost in the Shell density, scanline noise grain, halftone dots in midtones, 2D hand-drawn ink — zero 3D, zero CGI, 2.35:1, 24fps."
- "Cinematic stylized 3D animation — photorealistic environment particle simulation, stylized characters, volumetric atmosphere, neon energy VFX, realistic sand / snow / dust physics, 2.35:1 widescreen, 24fps."
- "Live-action mixed media — photorealistic real-world environment with real people, single 2D flat cartoon character composited in, cel-shaded flat coloring on cartoon character only, cartoon physics and expressions on cartoon character only, 2.35:1 widescreen, 24fps."

The opening line is the most important part of an animation prompt. If it's vague, Seedance will pick its own aesthetic and the result will drift.

---

## Style reference + character reference clarification

When using image references in animation, distinguish what each one is for. Often a keyframe image serves both as character reference AND visual style reference. State both roles explicitly.

> @image1 is the character reference AND visual style reference — a young woman drawn in a bold anime / illustration style: clean flat cel-shading, thick confident outlines, limited color palette with warm amber and muted tones. The entire video must match this exact 2D anime illustration aesthetic.

If the keyframe is style-only (different character) — clarify:

> @image2 is the visual style reference ONLY — use this image for lighting, color palette, environment design, and 3D claymation aesthetic. DO NOT use the character from @image2. Create a NEW original character in the same claymation style: [describe the new character].

Without this clarification, Seedance will copy the wrong things from the wrong images.

---

## Segment timing

Animation prompts use the same timestamp pattern as continuous format, but the timing typically signals stylistic / VFX shifts rather than just action shifts.

> 0–3s: She wakes up. Anime panic expression — wide eyes, sweat drop, hair sticking up.
>
> 3–6s: Fast anime montage — water splash on face drawn with bold stylized water lines, suit jacket throwing, hasty button adjustment. Classic anime speed lines in the background.
>
> 6–9s: Watch activates — holographic 3D city map snaps open in stylized 2D flat design floating beside her.
>
> 9–12s: She freezes. Close-up — eyes narrowing. Anime curiosity expression: head tilting slightly.
>
> 12–15s: The watch DETONATES. Anime-style explosive shockwave rings blast outward instantly — bold black outlines, blinding electric blue and white energy. Body vaporizes into flat geometric shards of light. Speed lines explode radially.

---

## Genre-specific animation conventions

Different animation styles have specific visual conventions Seedance reads as part of the aesthetic. Mention them explicitly.

### Anime / 2D illustration
- Anime panic expressions (wide eyes, sweat drop, hair sticking up)
- Anime speed lines on fast movement
- Impact frames (single bold stylized frame at peak action)
- Cel-shaded flat coloring with thick outlines
- Stylized 2D UI panels for tech / VFX (holographic notifications)
- Dutch-angle frames for tension
- Hard cuts to white / impact bursts at climaxes

### Claymation / stop-motion
- Visible fingerprint texture on all surfaces
- Tool marks, slight asymmetry on figures
- Squash on impact (bodies compressing on landing)
- Slightly stuttered motion (intentional frame steps)
- Soft clay-like texture even on inanimate objects (fire becomes clay ribbons)
- Warm dramatic lighting

### Low-poly 3D / chibi
- Small rounded chunky bodies, oversized expressive heads
- Smooth soft polygon surfaces (not hard edges)
- Stiff blocky finger movements
- Cartoon sweat drops, frustration lines
- Soft depth of field

### Manga (1980s–90s seinen)
- Cross-hatching for shadows
- Halftone dots / screentone in midtones
- Black-and-white only, no color, no grey shading
- Thick pen nib linework with ink bleed on heavy blacks
- Speech bubbles (with text — call out kanji or English)
- Scanline noise / age grain
- Sound-effect kanji integrated into frames

### Stylized 3D (xianxia / fantasy / desert hero)
- Photorealistic environment with stylized characters (selective realism)
- Volumetric particles (dust, snow, energy)
- Neon / supernatural VFX integrated into the world
- Realistic physics on environment, exaggerated physics on characters

### Mixed media (2D in live-action)
- Real photographed environment + flat 2D cartoon character
- Cartoon physics on the cartoon only (squash, exaggerated reaction)
- Live-action people react with realistic confusion to the cartoon
- Composited dust clouds / impact frames stay 2D

---

## VFX brackets in animation

Animation often has dense VFX. Use inline brackets:

> Her body [VFX: green energy ribbons spiraling up her body, armor plates snapping onto limbs and torso piece by piece, visor locking over her eyes, cannon assembling on her arm].

> The watch DETONATES [VFX: anime-style explosive shockwave rings blasting outward, bold black outlines, blinding electric blue and white energy, particles sucked inward in a violent spiral vortex, speed lines exploding radially in all directions filling the entire frame].

VFX brackets work even better in animation than in photoreal because the engine has more leeway with stylized effects.

---

## Style footer

After the action description, repeat the style commitment.

> Style: bold 2D anime illustration, cel-shaded flat coloring, thick confident outlines, warm amber and muted earth tones with cool electric blue holographic accents, anime speed lines and impact frames, 2.35:1 widescreen, 24fps.

The footer reinforces the aesthetic. Without it, Seedance can drift toward photoreal as the prompt progresses.

---

## SFX block

Animation often has stylized sound effects (kanji impact sounds, anime whooshes, claymation squashes). Append an SFX block:

```
SFX: anime panic gasp, classic anime speed-line whoosh, holographic UI activation chime, anime curiosity hmmm, watch detonation explosion, anime impact frame BANG, smash cut to white silence.
```

---

## Negative prompt block

For animation, the negative prompt is critical to keep the aesthetic locked.

```
Negative: no photorealism, no live-action, no 3D rendering on 2D scenes, no realistic lighting on stylized scenes, no watermarks, no subtitles, no text overlays except where specified.
```

For mixed-media (2D in live-action), the negative is different:

```
Negative: no full 2D cartoon environment (only the character is 2D), no animated background characters, no watermarks, no subtitles.
```

---

## Total footer

```
Total: 15s / 1 shot / 16:9 / 24fps
```

Animation always specifies 24fps in the footer. Some animations also benefit from 12fps "on twos" (traditional animation cadence) — call this out explicitly if you want it.

---

## Full example skeleton (anime)

```
Bold 2D anime illustration, cel-shaded flat coloring, thick confident outlines, warm amber and muted earth tones with cool electric blue holographic accents, anime speed lines and impact frames, 2.35:1 widescreen, 24fps.

@image1 is the character reference AND visual style reference — a young woman in a fitted suit drawn in bold anime style: clean flat cel-shading, thick confident outlines, limited color palette with warm amber and muted tones. The entire video must match this exact 2D anime illustration aesthetic. Maintain consistent 2D anime illustration style throughout all frames.

In her cluttered anime-style apartment at golden hour. Posters cover the walls, speakers on shelves. Warm amber light floods the room.

0–4s: She bolts upright in bed, eyes wide, instantly panicked — classic anime shock expression: wide eyes, sweat drop, hair sticking up. Her watch BUZZES. A glowing holographic notification pops up from the watch in a stylized 2D UI panel: "Anna, café in 10 minutes." Her face: pure anime panic — open mouth, eyebrows raised high. She THROWS off the covers and LEAPS out of bed. Handheld-style shaky pan, fast cuts.

4–9s: Fast anime montage — water splash on her face drawn with bold stylized water lines. She GRABS her suit jacket off a chair and throws it on mid-run. Buttons her collar with fumbling fingers in front of a mirror. Classic anime speed lines in the background during fast movements. Quick snap cuts with motion blur streaks. Dutch angle frames emphasize tension. She keeps glancing at her watch nervously. Expression: jaw tight, focused urgency.

9–13s: Watch activates — holographic 3D city map SNAPS OPEN in stylized 2D flat design floating beside her. Two familiar buttons: Long route 25min / Short route 10min. A third option flickers into existence below them, glowing brighter, pulsing with electric energy: ⚡ ULTRAFAST — NEW. She FREEZES. Close-up — eyes narrowing, one eyebrow raised. Anime curiosity expression. A slow smirk creeps across her face. Close-up on her finger hovering over the button. She TAPS it.

13–15s: The watch DETONATES [VFX: anime-style explosive shockwave rings blast outward instantly — bold black outlines, blinding electric blue and white energy]. Her entire body VAPORIZES into flat geometric shards of light in a single frame, particles SUCKED inward in a violent spiral vortex. Speed lines EXPLODE radially in all directions filling the entire frame. Single frame of pure white. Smash cut to white.

Style: bold 2D anime illustration, cel-shaded flat coloring, thick confident outlines, warm amber and muted earth tones with cool electric blue holographic accents, anime speed lines and impact frames, 2.35:1 widescreen, 24fps.

SFX: alarm-clock anime panic gasp, water splash anime whoosh, classic anime speed-line whoosh on every fast cut, holographic UI activation chime, slow-creep curiosity hmmm, watch detonation BANG, anime impact frame WHITE-OUT silence.

Negative: no photorealism, no live-action, no 3D rendering, no realistic lighting, no watermarks, no subtitles, no text overlays except for the holographic UI panel and watch options as specified.

Total: 15s / 1 shot / 2.35:1 / 24fps
```
