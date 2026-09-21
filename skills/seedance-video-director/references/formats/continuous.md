# Continuous format

A single timeline with timestamped beats. The camera moves and the action evolves, but it doesn't cut. Use this when your scene wants the propulsive feel of a single take across multiple beats.

---

## When to use

- Single-environment narratives that move forward in time without breaking the camera
- Scenes where the camera move IS the visual interest (long crane, slow push-in, lateral track)
- Beat-driven music videos where each beat lives in the same shot
- Cinematic narrative scenes where craftful camera control is the point
- Process / explainer scenes where continuity reinforces clarity

Distinct from POV (continuous = third-person controlled camera; POV = first-person locked perspective).
Distinct from one-take (continuous = one shot but typically within one environment; one-take = explicit multi-environment continuity with no cuts).

---

## Structure

```
[Cinematic opening line — establishes visual quality bar]

[Subject + environment + atmosphere paragraph]

[Camera grammar declaration — what the camera is and isn't doing]

0–Xs: [first beat description, action + atmosphere]

X–Ys: [second beat — camera or action evolves]

Y–Zs: [third beat — escalation continues]

Z–[final]s: [climax / resolution beat]

[Optional SFX block]

[Optional negative prompt block]

Total: [Xs] / 1 continuous shot / [aspect ratio]
```

---

## Camera grammar declaration

Continuous format depends on the camera staying single-shot. Tell Seedance what the camera is doing AND what it's NOT doing.

**Examples:**

- "Single continuous shot. No cuts. Stabilized push-in across the full duration. Camera advances steadily without correction."
- "Single continuous take. Camera holds an extreme low angle, panning right-to-left across the action, then crane-up at 8 seconds to reveal the wider scene. No cuts."
- "Continuous handheld. Camera floats with the subject, micro-jitters throughout, no cuts. Slight lens-breathing on focus pulls."
- "Single uninterrupted take. Camera begins as a stabilized lateral track at chest height, eases into a slow push-in across the second half. No cuts, no transitions."

The "no cuts" / "no transitions" / "uninterrupted" language is what locks Seedance to continuous format. Without it, the engine will default to inserting cuts.

---

## Beat timing

Continuous format uses explicit timestamp markers per beat. The camera doesn't cut between them — the action evolves and the camera responds.

**Standard timing patterns:**

- 8s: Three beats (0–3s, 3–5s, 5–8s)
- 10s: Three to four beats (0–3s, 3–6s, 6–8s, 8–10s)
- 12s: Four beats (0–3s, 3–6s, 6–9s, 9–12s)
- 15s: Four to five beats (0–3s, 3–6s, 6–9s, 9–12s, 12–15s)

Each beat should have clear visual content — what happens, what the camera does to follow it, how the atmosphere shifts.

---

## Beat content per timestamp

For every timestamped beat, include:

1. **What changes in the action** (the protagonist does something new, an event happens, a state transitions)
2. **What the camera does** (continues its push, eases into a new motion, holds momentarily)
3. **What the atmosphere does** (light shifts, dust thickens, crowd reacts)

Example:

> 6–9s: The runner enters the straight, arms unwinding from the turn. Camera continues its lateral track but eases inward, closing distance to her shoulder. The stadium lights begin to flare on the wet track surface, reflections trailing behind her spikes.

Three elements: action change (enters straight + arms unwinding), camera change (continues but eases inward), atmosphere change (lights flare on wet track).

---

## Camera evolution within continuous

The camera doesn't cut, but it can transform within the take. Common evolutions:

- **Push-in then pull-back** — start wide, push to detail, pull back at climax
- **Static then crane up** — hold a low angle, crane up to reveal scope
- **Handheld then stabilize** — start with chase energy, settle for the resolution
- **Pan across, then orbit** — pan reveals subject, orbit explores it
- **Speed ramp** — real-time → slow-motion → real-time within the same continuous shot

Specify when the camera evolves: "across the third beat, the camera eases from stabilized push-in into a slow orbit around the subject."

---

## Slow-motion within continuous

Continuous format handles speed ramps cleanly because there are no cuts to fight against.

**Pattern:**

> 6–9s: The cleaver swings down, RAMPS TO SLOW MOTION as it strikes the surface, the carrot fragments suspended in the air, particles drifting. SNAPS BACK to real-time as the chef's hand releases the handle and the fragments hit the cutting board.

The capitalized "RAMPS TO SLOW MOTION" and "SNAPS BACK" tags are explicit Seedance-readable markers. Keep them in caps for clarity.

---

## Verb density

Continuous format can read flat if the action between timestamps is too sparse. Pack each beat with kinetic verbs and active state changes.

**Sparse (fix this):**
> 3–6s: The runner enters the straight and continues running. The camera follows her.

**Dense (do this):**
> 3–6s: The runner enters the straight, body unwinding from the turn, arms driving forward in coordinated rhythm, breath punching out in cold cloud bursts. The camera continues its lateral track but eases inward, closing distance to her shoulder. The stadium lights flare on the wet track behind her spikes.

---

## When to break continuous and switch to multi-shot

Some scenes resist continuous format. Switch to multi-shot when:

- The scene has more than one environment that the camera can't physically traverse in real-time
- The energy demands cuts (action with explosive impact beats almost always wants multi-shot)
- The dramatic peak needs an extreme angle change Seedance can't render without a cut
- Multiple characters need their own coverage

If you find yourself wanting to write "cut to..." inside a continuous prompt, the prompt wants to be multi-shot. Don't fight it.

---

## SFX block (optional)

Same as multi-shot — append at the end if audio energy matters. For continuous format, the SFX block reads timeline-style (matching the beats):

```
SFX: 0–3s ambient stadium tone, distant crowd; 3–6s rhythmic spike strikes, breath puffs; 6–9s slow-motion stretch on cleaver impact, fragment suspension hush; 9–12s snap-back to real-time, fragments hitting board, single bell tone.
```

---

## Negative prompt block (optional)

For production-grade work:

```
Negative: no watermarks, no subtitles, no text overlays, no logos, no on-screen graphics.
```

---

## Total footer

```
Total: 12s / 1 continuous shot / 16:9
```

Always single shot for continuous format.

---

## Full example skeleton

```
Editorial cinematic realism, ARRI ALEXA Mini, 50mm prime at f/2.8, controlled color grade. Warm Kodak Portra palette, deep preserved shadows, fine grain, halation on highlights.

A florist arranges a single bouquet on a long white oak counter at her shop, late-afternoon sun raking through a tall front window from camera-left. Dust motes drift in the beam. A small ceramic vase waits at the right edge of the counter.

Single continuous take. Camera begins at eye-level locked-off three-quarter, eases into a stabilized push-in across the back half. No cuts.

0–4s: Her hands move across the loose stems on the counter, selecting one, two, then three white peonies. Each stem rises into her left hand, base resting against her palm. The afternoon light catches the peony petals.

4–8s: She lifts the gathered stems, rotates them in her left hand, eyes scanning the bouquet for balance. Her right hand reaches across to the vase, pulls it inward to center frame. The dust in the light beam intensifies as her motion stirs the air.

8–12s: She slides the bouquet into the vase, rotates the vase by its base to set the front-facing arrangement. Her hands rest momentarily on the counter beside it. The camera continues its slow push-in, settling on the finished bouquet. The peonies catch a long highlight from the window light.

SFX: ambient shop tone, soft rustle of stems, water gurgle inside vase, hands settling on wood, single warm room tone.

Total: 12s / 1 continuous shot / 16:9
```
