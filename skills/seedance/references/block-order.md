# Prompt architecture — block order and block definitions

One prompt shape, used for every capability, format and genre. What varies is which blocks appear and how dense each one runs — not the order.

---

## The order

```
Scene & Mood
Active References
Frame Map
Subject Lock — @tag        (one block per subject)
Cross-Frame Rules          (2+ subjects, or any internal cut)
Movement
Last Frame
World Plate
Sound Bed
Capture Realism
Camera Capture
```

**Optional and conditional:**
- **Active References** — only when references are attached
- **Cross-Frame Rules** — only with two or more subjects, or internal cuts
- **Capture Realism** — ships by default; drop only when the user asks for a glossy, clean or commercial-slick register
- **Format Mode** — a single line before Frame Map when the shot is a controlled multi-shot rather than a oner

**Never a separate block:** a style header at the top, a negative-constraints block at the bottom, output settings the user sets in the UI.

---

## Why this order

Spatial facts land before camera style, because the model resolves geometry first and whatever arrives late gets averaged. Optics land at the bottom, three positions from the end, because at the top the FOV competes with identity data and buried mid-body it fades into the prose. The prompt opens on what the moment *is* and closes on how it was shot.

---

## Distributed style

Style is not one object and does not get a prefix. Each aspect lives in the block that carries it. A style prefix at the top scatters the model's attention across the whole prompt; anchoring each aspect to its home block concentrates it.

| Aspect | Home block |
|---|---|
| Lighting | World Plate, echoed in Movement and Last Frame |
| Colour and grade | World Plate + Camera Capture — every colour tied to a surface, a source, and a purpose |
| Lens character | Camera Capture |
| Skin and micro-realism | Capture Realism + Subject Lock state |
| Acting | Subject Lock state + Movement muscle-level descriptors |
| Physics realism | Capture Realism + Movement environmental layer |
| Composition | Frame Map |
| Continuity | Cross-Frame Rules + Subject Lock lock-down lines |
| Wardrobe state | Subject Lock state-changes — the reference carries the wardrobe itself |
| Format, grain, fps | Camera Capture |

---

## Block definitions

### Scene & Mood
One or two sentences: what this moment is dramatically, written as observable action. Energy over position — what bodies and forces are doing. Frame Map handles the geometry. No scene numbers, no prior-scene context, no subjects who are not in this shot.

### Active References
Only the tags used in this shot, each with its role stated. See `reference-syntax.md`. Never a stale tag, never an invented tag, never a tagged subject who is not visible or required here.

### Frame Map
Anchors every subject in screen space before motion enters. Horizontal (left/center/right third, or x%), vertical (upper/center/lower third), depth (foreground/midground/background), frame occupancy (CU/MS/WS or % of frame height), negative space. Skip percentages for clean classical compositions — centered single, over-the-shoulder, profile two-shot. Percentages earn their place when the composition is asymmetric or drift would break the shot. Multi-shot: name Shot 1 framing and Shot 2 framing inline. This is also where the first-frame occupancy lock lives.

### Subject Lock
One discrete block per subject, never jammed together. Pins identity tag, body orientation, pose, state described physically, expression at the lips/eyes/brow/jaw level, gaze direction, contact points (feet on which surface, hand on which object), state-changes the reference cannot carry, and a lock-down line. See the minimum-anchor rule in `control-locks.md`.

### Cross-Frame Rules
Standard language: *`@tag1` and `@tag2` never swap positions, never cross center, never change depth. Distance, screen sides, eyelines and silhouettes hold across the full runtime.* When subjects must cross, state the crossing explicitly with its timing. For multi-shot, this is where the continuity carry list goes.

### Movement
Four layers, named in this order in flowing paragraph form, never tangled:

1. **Character motion** — physical actions across the runtime, per-beat timestamps where action demands, speeds in km/h
2. **Micro-motion** — breath, hair, fabric, jewelry
3. **Environmental motion** — rain, smoke, dust, traffic, wind, particles, with % density and meter depth
4. **Camera motion** — only if not covered in Camera Capture; usually omitted here

Name each layer explicitly, including when a layer is "nothing else moves." Stating that nothing moves is a directive; absence is not.

### Last Frame
The exact composition at the end of the runtime — where each subject sits at close, final pose, state and gaze, what is in focus, negative space, visual punctuation. Closes with the text suppression line unless in-frame text was requested:

> No on-screen text, no captions, no signage typography, no rendered text in the frame.

### World Plate
Location, time of day, weather, set dressing, atmospheric quality, lighting arrangement. Anchored to a plate tag if one is attached. Atmosphere in % density and meter visibility. When a plate reference is attached, state its role as geography and materials — not as camera angle or framing.

### Sound Bed
Diegetic by default: specific sounds, named surfaces, no music, no score, no lyrics, no genre cues. Music is permitted when the genre or capability calls for it (music-video, beat-sync, commercial with a bed) — say so explicitly rather than describing a song. Body sounds require corresponding visible body motion in Movement; see the audio-visual sync rule in `engine-rules.md`. For a fully silent capture: *Sound Bed: none, fully silent capture, audio added in post.*

### Capture Realism
The block that makes footage read as capture rather than render. Names the physics; Camera Capture names the gear. Four mechanics, all tuned per scene:

1. **Depth via suspended atmosphere between planes.** Atmosphere held in the air *between* camera, subject and background, so distant planes render softer, desaturated and lower-contrast than the foreground and the figure sits inside the air rather than pasted on a flat plane. Scale thin / light / heavy per scene.
2. **Moisture without shine** — only for wet, humid or sweaty scenes. Damp not beaded, wet not glossy, muting and deepening with no specular hotspot. Delete entirely for dry scenes.
3. **Per-zone specular kill on skin** — skip when there are no humans. Zero shine on forehead, nose bridge, cheekbones, temples, chin, collarbones, paired with biology cues: peach fuzz at jaw and hairline, soft fine pore texture, subsurface scattering, warmth preserved. The flattering ceiling is locked — texture stays fine, soft and even. No acne, no blemishes, no cratered pores, no clinical macro. Realism never makes a face look worse.
4. **Contrast curve stated three ways** — tonal curve (shadows lifted gently, highlights rolled off, nothing clipping or crushing), specular removal (every pixel matte and diffuse), grade (low-contrast, slightly desaturated, warmth preserved). Three statements is what holds it.

Never overlaps Camera Capture — no gear, no frame rate, no runtime here.

### Camera Capture
A single closing paragraph: body, lens as FOV° (mm), filtration, movement character, film stock, grade, frame rate, runtime. The only place camera, grade and stock language appears in the whole prompt — never doubled. Multi-shot sequences name per-shot lens differences inline.

Default camera energy is handheld with breath and organic operator drift. **Locked-off is opt-in only** — when the user asks for locked off, tripod, static, still camera, or names a shot type that requires it (surveillance plate, formal studio portrait, security-cam aesthetic).

---

## Word budget

- Single-shot scene: 280–400 words in the prompt body
- Multi-shot: up to 600

Density belongs where control matters — identity anchors, spatial blocking, first frame, gaze, landmark proximity, hand and prop states, timed action, optics, lighting, physics, dialogue. Density is wasted on generic beauty description, non-critical wardrobe, background extras, inactive props, and anything already visible in a reference.

Improvement comes from stronger signal, not more words. If a draft runs long, trim Subject Lock and Movement first, then Cross-Frame Rules.
