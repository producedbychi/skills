# Explainer / clarity

> **Lens note.** The camera stacks in this file are grade, stock and finish templates. Their millimeter values are legacy — convert the lens to a FOV degree from the ladder in `optics.md` before writing (`47° (50mm)`, `29° (85mm)`, `84° (24mm)`). Millimeters never lead, and apertures, ISO and lens brand names control nothing.


The concept is the hero. Visual hierarchy serves comprehension. Use as base genre for: tutorials, how-to videos, science education, product demonstration, B2B explainers, onboarding videos, course intros.

---

## Structural priorities (when used as base)

1. **Clarity over cinema.** Every shot serves the viewer's understanding. Polish is a tool, not the goal.
2. **Visual hierarchy.** What's most important is largest, brightest, or most centered. Subordinate detail is intentionally smaller, dimmer, or peripheral.
3. **Sequential logic.** Beats follow the explanation's structure. The user can pause at any moment and the visual should reinforce the spoken content.
4. **Demonstrative shots.** Camera shows what's being explained. If the VO says "press the button on the side," the shot shows the button on the side.

---

## Style declaration line patterns

- "Editorial explainer cinematography, RED Komodo, 50mm prime, controlled stabilized motion, clean key lighting, neutral color grade, high resolution, 16:9."
- "Educational documentary realism, ARRI ALEXA Mini, 35mm and 100mm Macro alternation, controlled handheld for environments and locked-off for detail beats, Warm Golden Hour grade, 16:9."
- "Tutorial cinematography, clean overhead diffusion, soft directional key, controlled camera moves, 50mm prime, 4K resolution, 16:9 or 9:16 depending on platform."

---

## Verb register (Tier 2 — Active / present)

show, demonstrate, point, indicate, hold, lift, place, set, turn, rotate, twist, press, tap, slide, fold, unfold, separate, combine, stack, arrange, position, align, assemble, disassemble, demonstrate, observe, examine, study.

Explainer verbs are demonstrative. They show the audience what's happening with clear physical action.

---

## Camera grammar defaults

- **Establishing:** wide stabilized, sometimes locked-off, shows the full scope of what's being explained
- **Demonstration beats:** medium 35–50mm, slight overhead three-quarter angle for hands-and-tools shots
- **Detail beats:** macro 90–100mm, locked-off, sharp focus on the demonstrated element
- **Result beat:** medium showing the completed work, slight pull-back to context
- **Transition beats:** match cuts on visual continuity, no whip pans

The explainer camera is purposeful and unobtrusive. The viewer should focus on the content, not the camera.

---

## Lighting defaults

- Soft overhead diffusion for even illumination
- Soft directional key from one side for slight modeling
- Cool fill from opposite side
- Practical lighting visible if it's part of the explained environment (a workstation lamp, an oven light)
- High exposure ratio in highlights (don't crush, don't blow out)

Avoid: dramatic single-source key (too cinematic), hard contrast (kills detail visibility), color gels (distracting).

---

## Color grade

- Neutral, slightly warm
- True whites preserved (important for documents, screens, lab settings)
- Slightly desaturated overall to keep focus on the demonstrated subject
- Halation only on bright practicals, not on overall highlights

---

## Beat density

Explainer beats are slightly slower than action / commercial. The viewer needs time to absorb each step.

- 7s scene: 3 cuts (one per major beat)
- 11s scene: 4 cuts
- 15s scene: 5 cuts

Don't over-cut. Holding a beat for 3+ seconds while the VO explains is correct for explainer.

---

## Visual hierarchy techniques

### Centered composition
The most important element is centered in the frame. Subordinate detail is around the edges.

### Selective focus
The most important element is in sharp focus. Background and unrelated elements are intentionally softened.

### Scale
The most important element is largest. Macro detail of the relevant component, with the larger context softened.

### Color isolation
The most important element holds saturation; the rest is desaturated. Useful for product demos with one accent color.

### Light isolation
The most important element catches the key light. Subordinate detail is in fill or shadow.

These are alternatives, not all required at once. Pick one technique per beat to keep the read clean.

---

## Demonstration patterns

### "Hands at work"
Macro down on hands manipulating an object. Wardrobe consistent across beats. Background controlled. Action is the focal point.

### "Step by step"
Multi-shot, each shot is one step. Hold each shot long enough for the audience to track what changed.

### "Before / after"
Side-by-side composition or A/B cut between two states of the same subject. Clear visual contrast.

### "Reveal sequence"
Closed → opening → revealed. Useful for product unboxing, package opening, drawer pulls.

### "Diagram in the world"
Real subject with overlaid arrows, callouts, or schematic guides held as clean negative space for motion graphics composite in post.

---

## Sound design

For explainer, audio is functional:

- Clear ambient (no competing noise)
- Voice-over track room (clean enough for VO to sit on top)
- Functional SFX where they help comprehension (button click, lid pop, machine hum)
- Music optional and only as a low background mat

The SFX block for explainer is brief:

```
SFX: ambient room tone, hand-on-tool contact, single button click, completion chime, soft VO room.
```

---

## Composition with other genres

### As modifier on `commercial-product`
- "Demonstration commercial" — shows the product in use rather than just hero shots
- Common for software, tools, kitchen appliances, fitness equipment
- Product is hero, but action is demonstrative rather than aspirational

### As modifier on `science-education`
- Strengthens the educational register
- Adds CGI overlay potential for scientific visualization

### As modifier on `ugc-authentic`
- Casual instructional content
- "How I do this" register from a personal voice

### As modifier on `viral-hook`
- "Did you know" or "here's how" educational hook
- Information-driven attention grab

---

## What this genre does NOT do

- Dramatic cinematic camera moves (cranes, hyper-stylized angles)
- Action-driven climaxes (the climax is comprehension, not impact)
- Heavy color grades (kills visibility of demonstrated subject)
- Distracting atmospheric particulate
- Theatrical performance from on-camera people

---

## Reference image style

- "Editorial demonstration photography, soft overhead diffusion, locked-off three-quarter angle, neutral color grade"
- "Tutorial-style still, hands working with product, clean controlled lighting, 50mm prime"
- "Educational subject photography, true white background or controlled environment, sharp focus on subject"

---

## Common scenes

- Hands assembling, disassembling, manipulating an object
- Step-by-step process with clear visual progression
- Product demonstration with key features called out
- Before / after transformation
- Reveal of the inside of something (cutaway, exploded view)
- Schematic-style overhead of objects laid out for explanation
- Talking head with B-roll of the demonstrated subject

---

## Negative prompt block

```
Negative: no watermarks, no subtitles (unless instructional captions are explicitly part of the design), no decorative on-screen text, no dramatic music, no flashy transitions, no cinematic camera moves that obscure the demonstrated subject.
```
