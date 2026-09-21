# Short drama

> **Lens note.** The camera stacks in this file are grade, stock and finish templates. Their millimeter values are legacy — convert the lens to a FOV degree from the ladder in `optics.md` before writing (`47° (50mm)`, `29° (85mm)`, `84° (24mm)`). Millimeters never lead, and apertures, ISO and lens brand names control nothing.


Dialogue and emotion are the hero. Performance drives the camera. Use as base genre for: scripted dialogue scenes, dramatic confrontations, romantic moments, comedy beats, soap-opera-style scenes, short-form drama (TikTok / Reels narrative content).

---

## Structural priorities (when used as base)

1. **The line is the beat.** Each piece of dialogue is its own beat. Cut on the line, hold on the response.
2. **Emotion labels never appear in the prompt.** Translate every emotional state to physical signature (see `references/antislop.md` expression bank).
3. **Power dynamic is structural.** Identify which dialogue archetype (Confrontation / Interrogation / Negotiation) and follow its camera grammar (see `references/archetype-router.md`).
4. **Dialogue limit ~25–30 spoken words per 15 seconds.** Past that, compress to physical behavior or split into multiple generations.

---

## Style declaration line patterns

- "Short drama cinematography, RED Komodo, 50mm prime at f/2.8 for portraits, controlled handheld with intentional motion, intimate framing, Kodak Portra warmth on skin, 16:9 or 9:16 vertical."
- "Dramatic dialogue scene, ARRI ALEXA Mini, 35mm and 50mm alternation, OTS coverage with intentional axis crossing on power shifts, deep preserved shadows, halation on highlights, 2.35:1, 24fps."
- "Soap-opera dramatic realism, anamorphic 35mm at f/2, shallow depth, rich color grade with warm key on faces, controlled handheld, slight melodramatic lighting (single hard source), 16:9."

---

## Verb register (Tier 2 with selective Tier 3)

reach, lift, set, place, lower, push, pull, slide, rise, walk, step, turn, glance, study, scan, follow, settle, rest, lean, tilt.

For peak emotional beats, escalate selectively:
- snap (head turn at recognition)
- jerk back (surprise / hurt)
- shove (impact during confrontation)
- grip (white-knuckle resolve)
- slam (door, hand on table, item placed in anger)

---

## Dialogue formatting

Use the standard short-drama format:

```
Picture (0–5s): [shot description, no dialogue]
Line 1 (Speaker, emotion): "Spoken line in quotes."
Picture (5–10s): [next shot description]
Line 2 (Speaker, emotion): "Response in quotes."
Picture (10–15s): [final shot description, often non-verbal close]
SFX: [audio direction]
Total: [Xs] / [N shots] / [aspect ratio]
```

The `(Speaker, emotion)` tag tells the model the performance register. Examples:
- (Father, controlled rage)
- (CEO, cold finality)
- (Best friend, suppressed laughter)
- (Lover, quiet betrayal)

Don't write the emotion as a directorial note — bake it into how the line is described.

---

## Camera grammar by archetype

### Confrontation (most common)
- OTS (over-the-shoulder) tight on whoever is speaking
- Cut to OTS on the listener (reaction)
- Camera crosses axis at the power-shift line (the line where dominance flips)
- Inserts on physical tells (hand gripping table, glass set down hard)

### Interrogation
- Low-angle on the questioner
- Eye-level or slight high-angle on the subject
- Slow push-in on the subject during silences
- Pull-back on the questioner during reveals
- Locked-off wide as a recurring composition

### Negotiation
- Symmetrical framing — matching shot sizes on both characters
- Even cut rhythm
- Two-shot establishes equality
- Inserts on subtle physical tells (hand drumming, glance away, chair shift)

---

## Lighting defaults

- Practical sources visible (lamp, candle, window, computer screen)
- Strong key with deep fill ratio for emotional weight
- Catchlights consistent across coverage on both characters
- Backlight separates subjects from background
- Color contrast: warm on faces, cool on environment (or vice versa for tonal flip)

---

## Color grade

- Kodak Portra warmth on skin
- Deep preserved shadows for emotional weight
- Slight magenta in highlights, slight teal in shadows
- Halation on highlights
- Rich saturation (more than documentary, less than music video)

---

## Compression patterns when dialogue exceeds 30 words

If user provides 80 words of dialogue for a 15-second scene:

1. **Identify the power-shift line** — the line where dominance flips or truth emerges.
2. **Keep one line before** (setup)
3. **Keep one line after** (reaction)
4. **Convert other 5–6 lines to physical behavior**

Example. User script:
```
HE: "I never wanted this for us. You know that. I tried to make it work."
SHE: "You tried? You weren't even there."
HE: "I had to be at the office. The deal was—"
SHE: "The deal. Always the deal."
HE: "It was for us!"
SHE: "It was for you."
HE: "I'm leaving."
SHE: "Watch me."
```

Compressed (keeping power shift at line 6 / line 7):
```
Picture (0–5s): She sets down her glass with deliberate slowness, eyes locked on him across the table. He looks down at his hands.
Line 1 (Husband, defensive): "It was for us!"
Picture (5–10s): She doesn't blink. He looks up. Her hand picks up her ring from the table edge, turns it once, sets it down on the white tablecloth.
Line 2 (Wife, cold finality): "It was for you."
Picture (10–15s): She rises from the chair. He stays seated. She walks past him without looking back. He picks up the ring.
SFX: glass set on wood, deliberate footsteps, distant restaurant murmur, single beat of silence at the close.
Total: 15s / 3 shots / 16:9
```

The rest of the dialogue's content lives in the physical behavior. The emotional beat lands harder this way.

---

## Atmosphere

Short drama atmosphere is intimate:
- Warm room tone
- Candlelight or lamp light visible
- Steam from drinks in foreground
- Ice cubes settling in glasses
- Distant ambient (rain, traffic, conversation in adjacent room)

---

## SFX block

Always include for short drama:

```
SFX: ambient room tone, [physical sounds matching beat 1], [physical sounds matching beat 2], [single beat of silence at the climax line], [closing physical sound or held room tone].
```

The "single beat of silence" before or after the climax line is short drama's signature. Use it.

---

## Composition with other genres

### As modifier on `cinematic-narrative`
- Strengthens dialogue / character depth
- Almost the same as cinematic-narrative base — short-drama is more dialogue-forward

### As modifier on `viral-hook`
- "Mini drama" social content
- TikTok-style scripted moments with hooks
- 9:16 vertical, fast pacing within drama register

### As modifier on `commercial-product`
- Narrative ad — story sells the product
- Character beats around the product
- Hayden Valley Scene 1 + Scene 6 buyer arc has short-drama elements (the buyer's emotional turn)

### As modifier on `horror-thriller`
- Psychological dialogue tension
- Restraint at the climax line
- "Get Out" interrogation beats

---

## What this genre does NOT do

- Action verb density (Tier 4–5 verbs almost never)
- Fast-cut rhythms (3–5 cuts in 15s, not 6–8)
- Large environmental scope (drama lives in intimate framing)
- Theatrical performance from non-actor subjects (this is for scripted scenes)

---

## Negative prompt block

```
Negative: no watermarks, no subtitles unless explicitly part of the design, no on-screen text, no fast-cut action sequences, no commercial-bright lighting, no theatrical melodrama (the performance should feel grounded).
```

---

## Reference image style

- "Cinematic dramatic still photography, intimate framing, Kodak Portra warmth, halation on highlights"
- "Anamorphic 2.35:1 portrait, deep preserved shadows, motivated practical lighting"
- "Editorial drama still, 50mm prime at f/2.8, shallow depth"

---

## Common scenes

- Two-character confrontation across a table
- Phone call with the listener visible (one side of the conversation)
- Goodbye / breakup / departure beat
- Reveal of hidden information mid-dialogue
- Silent reaction to news (no dialogue)
- Family dinner with subtext
- Workplace confrontation in a private office
- Bar / restaurant conversation with environmental ambient
