# Camera vocabulary library

Pull from this when writing shot descriptions. Variety matters — if every beat opens with "stabilized slow push-in," the prompt reads as flat. Match the camera character to the emotional register of the beat.

---

## Angles

| Angle | What it does | When to use |
|---|---|---|
| Eye-level | Neutral, observational | Default for dialogue, character beats |
| Low-angle | Subject feels powerful, dominant | Hero shots, monsters, vehicles |
| High-angle / overhead | Subject feels vulnerable, small | Defeat moments, surveillance, isolation |
| Bird's-eye / top-down | Pure abstraction, geometric clarity | Process shots, choreography, layouts |
| Worm's-eye / ground-level | Hyper-low, dramatic verticality | Heroic launches, towering subjects |
| Dutch angle | Imbalance, unease, urgency | Action chase, horror, vertigo |
| Over-the-shoulder (OTS) | Two-character relational | Dialogue, confrontation |
| Three-quarter | Slight angle from straight-on | Most product shots, character medium shots |

---

## Focal length — see optics.md

Focal length is not specified here. Lens choice is governed by the FOV degree ladder in `optics.md`, because Seedance treats degrees as discrete anchors and millimeters as suggestions. Never write a millimeter value as the primary lens instruction, and never write an aperture, ISO, or lens brand name as a control.

Write `47° (50mm) eye-level neutral`. Read `optics.md` for the ladder, the selection tree, the visual outcome stacks, and the anti-drift locks.

---

## Camera moves

### Stationary / minimal
- **Locked-off** — camera doesn't move at all. Use for clean reveals, deliberate composition holds.
- **Static** — same as locked-off; use either word.
- **Subtle drift** — minimal float for "alive" feel without explicit motion.

### Push / pull
- **Push-in** — camera moves toward the subject. Velocities: very slow / slow / steady / fast / aggressive.
- **Pull-back** — camera moves away from the subject. Reveals scope.
- **Dolly-in / dolly-out** — same as push/pull. "Dolly" implies a smoother track.
- **Crash zoom / snap zoom** — fast lens-only push to subject. High-energy.
- **Slow zoom-in** — gradual lens-only compression. Builds tension.

### Lateral / horizontal
- **Tracking shot** — camera moves alongside subject, parallel to action.
- **Lateral dolly** — same as tracking but emphasizes the rail-like smoothness.
- **Pan** — camera rotates left-to-right or right-to-left without moving its position.
- **Whip pan** — fast pan with motion blur.
- **Orbit / circle** — camera circles the subject.
- **Half-orbit** — 180° travel around subject.

### Vertical
- **Tilt up / tilt down** — camera rotates vertically without moving its position.
- **Crane up / crane down** — camera moves vertically (up or down).
- **Pedestal up / pedestal down** — same as crane but more measured / studio.
- **Drone descent / drone ascent** — aerial vertical with environmental context.

### Aerial
- **Aerial / drone wide** — high overhead environmental establishing.
- **Drone push-in** — drone moves toward subject from height.
- **Helicopter shot** — wide mobile aerial, not always literally a helicopter.
- **God's-eye top-down** — purely vertical overhead.

### Handheld / motion
- **Handheld** — visible operator motion, organic.
- **Hyper-chaotic handheld** — extreme jitter, near-loss of subject (POV / orb format).
- **Steadicam / gimbal** — stabilized motion that follows action smoothly.
- **Stabilized tracking** — gimbal-smooth lateral travel.
- **Shaky cam** — deliberate operator destabilization for energy.
- **Body-mount** — strapped to a runner / vehicle, low and forward.

### Specialized
- **Hitchcock zoom / dolly zoom / vertigo zoom** — dolly forward + zoom out (or reverse). The background warps. Use sparingly — high-impact.
- **Bullet-time** — frozen subject with rotating camera, multi-camera array effect.
- **Match cut on motion** — cut bridges by visual rhyme.
- **Speed ramp** — gradually shifts from real-time to slow-motion (or reverse).
- **Snap zoom + speed ramp** — combined for action emphasis.

---

## Time

- **Real-time** — default 24fps.
- **Slow motion** — 48fps, 60fps, 120fps. Sub-categories:
  - **Subtle slow-mo** — 48fps, just enough to feel deliberate
  - **Heavy slow-mo** — 120fps+, hyper-detailed
  - **Bullet-time slow-mo** — frozen subject + camera move
- **Speed ramp** — interpolation between real-time and slow-motion. Use "RAMPS TO SLOW MOTION as..." then "SNAPS BACK" to return.
- **Time-lapse** — extreme acceleration. Useful for environmental / process shots.
- **Hyper-lapse** — time-lapse with camera movement.
- **Freeze frame** — held single frame.
- **Stutter / strobe** — repeated micro-cuts on same action.

---

## Transitions

- **Hard cut** — instantaneous transition. Default.
- **Match cut** — visual rhyme bridges the cut. Specify what's matching.
- **Whip-pan transition** — fast pan blends two shots.
- **Smash cut** — abrupt, jarring. Often to white, black, or silence.
- **Speed-ramp transition** — slow-motion holds across cut, then snaps back.
- **L-cut** — audio from the next shot starts before its visual cut.
- **J-cut** — audio from previous shot continues over the next visual.
- **Wipe** — geometric transition (rare in cinematic, common in retro).
- **Iris** — circular reveal (very rare, period-piece marker).

Avoid fades and dissolves unless brief specifically calls for them — they read as low-energy.

---

## Color and grade

| Grade | Look | When to use |
|---|---|---|
| Warm Golden Hour | Honey tones, soft falloff | Commercial product, documentary warmth |
| Kodak Portra | Slight magenta-warm, soft skin | Cinematic, narrative warmth |
| Kodak 2383 | Deep cinematic film print | Premium cinematic |
| Industrial Noir | Cool teals, desaturated greens | Action, thriller, vendor sprawl chaos |
| Cyberpunk neon | Magenta + cyan, high saturation | Sci-fi action, music video |
| Muted Scandinavian Cool | Pale blue-gray, low saturation | R&D, lab, sterile environments |
| ARRI ALEXA aesthetic | Cinema-grade neutral with deep shadows | Default premium |
| RED Komodo aesthetic | Sharper, slightly cooler | Modern commercial |
| Vintage 16mm | Heavy grain, faded color | Nostalgic, indie |
| Black and white high contrast | Pure tonal | Manga, dramatic, art |
| Anamorphic flare | Horizontal lens flares | High-energy commercial, sci-fi |

**Never write a bare palette list.** Every colour attaches to a surface, a light source, and a purpose in the shot. Bare palette lists drift across beats. See the colour discipline section in `lighting.md`.

---

## Lighting — see lighting.md

Lighting is a priority constraint, not a style modifier, and it is written as a physical arrangement: source, direction, camera side, shadow side, background brightness, exposure priority. The characters below are shorthand only — read `lighting.md` before writing any lighting language.

- **Natural / available** — what's already there
- **Three-point** — key + fill + back, classic studio
- **Soft single source** — north-style softbox, editorial
- **Hard single source** — direct key, dramatic shadows
- **Practical lighting** — light sources visible in frame (lamps, signs, screens)
- **Top-down softbox** — overhead diffusion, common for product
- **Side rake / side light** — long shadows, texture-emphasizing
- **Backlight / rim light** — silhouette + edge separation
- **Underlit** — light from below, horror / unease
- **Volumetric** — visible beams of light through atmosphere (dust, fog, smoke)
- **Tyndall effect** — strong dust-in-beam lighting
- **God ray** — single directional shaft of light through obstruction

---

## Atmosphere modifiers

These add density to a shot without changing its structure.

- Dust / particulate (cocoa fines, sugar haze, sand, ash, pollen)
- Smoke / fog / mist (deep / shallow / wisping)
- Steam / vapor (kitchen, industrial, cold-air condensation)
- Fine grain (16mm / 35mm)
- Specular bloom on highlights
- Subtle chromatic aberration near frame edges
- Halation on highlights
- Slight focus breathing
- Lens flare (sun, neon, tungsten)
- Heat shimmer / heat-haze distortion
- Rain / wet surfaces (puddles double the available reflections)

Pick 1–3 per shot based on the genre. Don't pile on six atmospheric modifiers — Seedance won't render all of them and the ones that survive will fight each other.

---

## Common combinations

These read as production-grade. Note the FOV-degree lead — millimeters in parentheses only.

- "Wide-latitude cinema capture, 47° (50mm) eye-level neutral, shallow depth dropping the background into a soft cool wash, Kodak Portra warmth, fine grain, halation on highlights, 24fps 180° shutter, 16:9."
- "Wide-latitude cinema capture, 84° (24mm) classic wide, low-angle handheld with constant micro-drift, desaturated industrial teals, heavy grain, motion blur on fast action, 24fps 180° shutter, 2.35:1."
- "Wide-latitude cinema capture, 12° (200mm) tele detail, locked-off overhead three-quarter, warm golden-hour grade with deep true blacks, fine grain, specular bloom on highlights, 24fps, 16:9."
- "Wide-latitude cinema capture, 180° fisheye, hyper-chaotic handheld POV with strong spherical bulge and chromatic aberration near the frame edges, slightly desaturated, halation on highlights, motion blur throughout, 24fps 180° shutter, 16:9."

Always include: capture register, FOV° (mm), angle and height, movement character, grade, finish notes, frame rate, runtime. Never a second camera spec elsewhere in the prompt.
