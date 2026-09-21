# Antislop and the kinetic verb bank

Two things this file does:
1. Lists words and phrases that signal AI writing and that you should avoid in Seedance prompts
2. Provides a kinetic verb bank organized by intensity tier so you can pull the right register for the genre

---

## Words and phrases to avoid

These read as AI-generic and weaken Seedance's read of the prompt. Avoid in both prose and section headers.

### Empty intensifiers

breathtaking, stunning, captivating, mesmerizing, awe-inspiring, riveting, gripping, spellbinding, unforgettable

### Hollow craft signals

masterfully, meticulously, exquisitely, beautifully crafted, expertly composed, painstakingly detailed, lovingly rendered, lavishly produced

### Marketing slop

cinematic masterpiece, visual feast, a symphony of, kaleidoscope of, rich tapestry, vibrant tapestry, journey through, voyage into, descent into

### Frictionless verbs

seamlessly, effortlessly, flawlessly, harmoniously, fluidly (when used to describe the entire shot rather than a specific motion)

### Tech-bro words

cutting-edge, state-of-the-art, next-level, revolutionary, groundbreaking (only acceptable when the actual content is groundbreaking — almost never)

### Vague action verbs

elevate, unlock, unleash, harness, empower, transform (when used as abstractions)

### Over-explanatory phrases

a testament to, speaks volumes, resonates deeply, evokes a sense of, conjures, embodies the essence of

### Tone tells

The model loves writing "masterful" and "stunning" because the training data is full of marketing copy. Strip these compulsively. If the cluster on the table is well-lit, write "the cluster catches a long specular highlight on its leading edge" — describe what the camera sees. Don't tell Seedance the cluster is "stunningly lit."

---

## Kinetic verb bank by intensity tier

Use this when writing Dynamic Description / shot beats. Pull from the tier that matches your genre register. Mixing tiers is fine — but the dominant register should match the brief.

### Tier 1 — Quiet observational

For documentary, atmospheric, contemplative, slow-build horror.

drift, settle, rest, hold, pool, gather, unfold, ease, fold, lift, rise, sink, glide, hover, suspend, breathe, soften, dim, brighten, catch, pass, lean, trace, ripple, ease, whisper (as physical motion only — wind whispering, not narration), tilt, shift, tip

### Tier 2 — Active / present

For cinematic narrative, explainer, commercial product (default tier for Hayden Valley work).

walk, step, turn, reach, grasp, lift, tip, pour, set, place, lower, raise, push, pull, slide, roll, fold, unfold, open, close, press, tap, hold, stack, arrange, position, pivot, swivel, glance, watch, study, scan, follow, track, settle, rest, breathe, exhale

### Tier 3 — Kinetic / energetic

For UGC, viral hook, ad creative, action-light, music video.

snap, flick, jerk, whip, bounce, lurch, hop, leap, dart, sprint, dash, crash, slap, pound, drum, beat, surge, burst, pulse, throb, race, rush, charge, swerve, weave, dodge, duck, vault, plant, slam, hit, strike, punch, kick

### Tier 4 — High action

For action-intense, fight scenes, intense commercial.

DETONATE, EXPLODE, BLAST, SHATTER, FRACTURE, RUPTURE, COLLAPSE, SLAM, SMASH, HURL, PIVOT, TEAR, RIP, GRAB, WRENCH, DRIVE, HAMMER, POUND, ROCKET, BARREL, TUMBLE, CRASH, SPILL, ERUPT, BURST, SPRAY, STRIKE, POUND, CRASH, SHUDDER, RECOIL, RICOCHET, WHIP, LUNGE, LEAP, VAULT, SOAR, PLUMMET

### Tier 5 — Cataclysmic

For Higgsfield-style transformation finales, fantasy explosions, horror releases.

VAPORIZE, ANNIHILATE, SHATTER OUTWARD, IMPLODE, COLLAPSE INWARD, DETONATE OUTWARD, ERUPT, BURST, RIP APART, TEAR THROUGH, DECIMATE, OBLITERATE, FRAGMENT, DISSOLVE INTO, DISINTEGRATE INTO, SCATTER INTO, EXPLODE OUTWARD, SHOCKWAVE OUTWARD

Use Tier 5 sparingly — once or twice per scene at the climax beat. Past that and the prompt loses its punch.

---

## Expression verbs (transformations, not states)

Replace state language ("she looks worried") with transformation language ("the brow furrows tight as her eyes widen").

### Transformations of fear / panic
brow furrows tight, eyes widen, mouth opens, jaw drops, breath catches, throat tightens, shoulders draw up, hands grip [object], fingers whiten, eyes dart, head snaps toward [direction]

### Transformations of relief / settling
brow softens, corners of the mouth lift, breath releases, shoulders drop, eyelids ease, hand opens, grip relaxes, fingers unfurl, head tips back, weight settles into the chair

### Transformations of focus / determination
jaw sets, eyes narrow, brow drops, mouth tightens to a line, hands still, breath slows, weight shifts forward, posture squares, gaze locks onto [object]

### Transformations of recognition / surprise
eyes widen, head pulls back, breath catches, mouth opens slightly, hand moves to mouth or chest, brow lifts, posture freezes mid-motion

### Transformations of warmth / softening
shoulders drop, jaw releases, eyes crinkle at the corners, mouth lifts at one corner first then both, breath releases through nose, head tips slightly

These transformations are how Seedance reads emotion. Always specify the muscle-level signature, not the emotion label.

---

## When the user asks for a specific tone

Map their language to the verb bank:

- "Calm, contemplative" → Tier 1
- "Editorial, controlled" → Tier 2
- "Energetic, snappy" → Tier 3
- "High action, explosive" → Tier 4
- "Apocalyptic, transformative" → Tier 5

If the user asks for "viral energy" or "TikTok pace," pull Tier 3 + lean on snap cuts. If they ask for "documentary" or "trade show realism," pull Tier 2 + reduce cut frequency. If they ask for "Higgsfield-style" or "full action," pull Tier 4–5 + dense cuts + high VFX brackets.

---

## Sentence rhythm

Long descriptive paragraphs with semicolons feel AI-generic. Short kinetic sentences with strong verbs read as direction.

❌ "The hero, who has just emerged from the portal, finds himself standing on a galloping horse, with a cowboy in pursuit, and he begins to panic."

✅ "The hero drops from the portal feet-first onto a galloping horse. Tie whipping. Eyes wide. The cowboy gallops behind, gaining ground."

Aim for 6–14 word sentences in shot descriptions. Mix lengths but lean short.

---

## What to keep

The antislop list is not "kill all adjectives." Specific sensory detail still earns its place:

✅ "Mahogany-to-near-black gradient" — specific color description
✅ "Brushed pewter shop bowl with soft satin sheen" — specific material
✅ "Faint cocoa-haze in the air" — specific atmosphere
✅ "Powder-blue food-safe nitrile glove" — specific wardrobe

Keep adjectives that point at something specific Seedance can render. Cut adjectives that just signal vibe ("breathtaking," "stunning," "exquisite").
