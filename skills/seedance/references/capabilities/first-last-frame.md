# First / last frame control

Set both a starting frame AND an ending frame as separate reference images. Seedance generates the arc between them.

---

## When the user is in this capability

- "I have the opening frame and the closing frame — generate the transition between them."
- "Start at this composition, end at this composition."
- "I want a transformation arc from state A to state B."
- "First frame is the buyer frustrated, last frame is the buyer relieved — generate what happens in between."

Whenever the brief specifies both bookend compositions, you're in first/last frame.

---

## Prompt structure

```
@image1 as first frame + @image2 as last frame + [transition description] + [duration]
```

Example:

> @image1 as first frame: the buyer at her desk, frustrated, gripping the red felt-tip pen, supplier sprawl crowding the periphery.
>
> @image2 as last frame: the same buyer at the same desk, relaxed, the pen set aside, a single Hayden Valley case open at center revealing the assortment.
>
> Generate the 7-second transition from @image1 to @image2. The frustrated state transforms to the relieved state through a single coating-wipe of warm light sweeping across the desk. Camera holds POV throughout. The buyer's hand and posture change progressively across the duration.

---

## What first/last frame is good for

- **Transformation arcs** — state A becomes state B (frustrated to relieved, calm to powered-up)
- **Reveal sequences** — closed to open, hidden to revealed
- **Time progression** — morning to evening, before to after
- **Character emotional arcs** — fear to confidence, surprise to acceptance
- **Product transformations** — packaged to open, raw to finished
- **Environmental shifts** — clear to stormy, day to night, full to empty

---

## What first/last frame doesn't do well

- **Heavy action sequences** — the constraint of bookend frames fights against kinetic energy. Use multi-shot instead.
- **Long character arcs over many beats** — first/last frame works for one transition, not a multi-step narrative.
- **Surprise endings** — bookend frames make the ending visible from the start, which kills surprise.

---

## Tagging the bookends

Always state which image is the first frame and which is the last:

> @image1 as first frame.
> @image2 as last frame.

If you're using more than two images (a third for character consistency, a fourth for style):

> @image1 as first frame.
> @image2 as last frame.
> @image3 — character reference (the buyer's identity, used throughout).
> @image4 — visual style reference only (the lighting and color grade across the duration).

---

## Describing the transition

Even though Seedance generates the transition, you should describe what happens:

> Transition from @image1 to @image2: the buyer's expression softens progressively across the duration. The supplier sprawl on the desk dissolves into the clean composition (papers fading, mugs disappearing, samples vanishing). A single Hayden Valley case fades in at the center. The light shifts from cool fluorescent to warm Golden Hour across the duration.

Without transition description, Seedance may generate an unintuitive bridge between the bookends.

---

## Camera grammar

Specify what the camera does between the bookends:

> Camera holds POV throughout (matching both @image1 and @image2's first-person framing).

> Camera begins at @image1's medium close-up, slow push-in across the duration, settles at @image2's tight close-up.

> Camera matches @image1's three-quarter angle at the start, eases through a 90-degree orbit to match @image2's profile angle at the end.

The bookend compositions imply specific camera positions. State whether the camera moves or holds.

---

## Lighting and color grade transitions

Lighting and grade can shift across the duration:

> @image1 has Industrial Noir grade (cool fluorescent). @image2 has Warm Golden Hour grade (warm editorial). The transition shifts from cool to warm progressively across the duration. The light source motivation shifts: in @image1, the dominant light is overhead fluorescent. In @image2, the dominant light is warm directional from camera-right.

Specify the grade trajectory.

---

## Specific transformation patterns

### Character emotional arc
@image1: character with one emotional state. @image2: same character with different emotional state. Transition: progressive transformation of expression, posture, breath.

### Object transformation
@image1: object in state A (closed, empty, raw). @image2: object in state B (open, full, finished). Transition: object morphs through visible intermediate states.

### Environmental shift
@image1: location at one time of day / weather. @image2: same location at different time / weather. Transition: time-lapse or atmospheric morph.

### Reveal sequence
@image1: subject occluded (covered, hidden, dark). @image2: subject revealed (uncovered, visible, lit). Transition: occlusion clears progressively.

### Person-replacement
@image1: subject A in position. @image2: subject B in same position. Transition: an occlusion (passing object, light flash, etc.) hides the subject change.

---

## Duration and pacing

For first/last frame, duration matters more than format. The transition unfolds across the full duration.

- **Fast transitions (4–6s):** dramatic morph, quick reveal, snap transformation
- **Medium transitions (8–11s):** progressive arc with visible intermediate states
- **Slow transitions (12–15s):** drawn-out transformation with held middle states

State the duration in the prompt:

> Generate the 11-second transition. The intermediate state at 5–6 seconds should show partial transformation — about halfway between @image1 and @image2.

---

## Limits

- Both frames must use compatible compositions (similar framing, scale, position)
- If the framings differ wildly, the transition may feel disjointed
- Up to 9 reference images, but typically only 2 are bookends — others are for character / style consistency
- The transition's visual logic should be motivated (state A → state B has a clear cause)

---

## Common first/last frame requests

- "Hayden Valley Scene 1 mood arc — frustrated to relieved buyer"
- "Product unboxing — closed package to revealed product"
- "Time-lapse — empty cafe to full cafe across the morning"
- "Transformation reveal — caterpillar to butterfly"
- "Before / after — messy room to organized room"
- "Hero awakening — sleeping form to fully transformed superhero"
- "Reveal moment — covered statue to uncovered statue"

---

## Negative prompt

```
Negative: no cuts, no scene changes, no time skips except as part of the bookend transition, no third state outside the @image1 → @image2 arc, no camera angle change that breaks both bookend compositions.
```

This locks the transition between the two specified states.

---

## When to use vs not use

Use first/last frame when the bookend compositions are the dramatic point — the contrast / transformation IS the content.

Don't use when:
- The brief has more than one transformation moment (use multi-shot)
- The bookend compositions are nearly identical (no transformation to generate)
- The transition is the focal action (rather than the bookends being the focal points)
