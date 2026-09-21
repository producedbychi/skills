# Story completion

Generate the storyline from a storyboard (multiple images) or a script. Seedance auto-completes the narrative across the visual moments.

---

## When the user is in this capability

- "I have 4 storyboard frames — make a video that tells the story across them."
- "Here's a script, generate a 15-second video matching it."
- "Use these comic panels as the visual reference, animate them with story flow."
- "I have a sequence of product photos — generate a coherent narrative video."

If the user provides multiple images that imply a sequence OR a script that needs visual interpretation, you're in story-completion.

---

## Prompt structure

```
[Storyboard / script reference] + [interpretation style] + [SFX / dialogue requirements]
```

Example:

> Use @image1 through @image4 as a sequential storyboard, in order. Animate the story progression across these frames in a 15-second video. Style: 2D anime illustration, matching the visual aesthetic of the storyboards. Maintain consistent character identity across all frames. Include dialogue and SFX as marked in the storyboard captions.

---

## Multi-image as sequential storyboard

When the user provides 4+ images representing story beats:

> Sequential storyboard: @image1 (opening), @image2 (development), @image3 (climax), @image4 (resolution). Animate the transitions between these frames. Each frame represents approximately 3–4 seconds of the 15-second video. The character holds identity across all frames.

The order matters — list them in narrative sequence.

---

## Script-driven story completion

When the user provides a script (with or without storyboards):

> Generate a 15-second video from this script:
> 
> [Pasted script in quotes]
>
> Style: [genre register from the brief]. Visual interpretation should match the script's pacing — beat 1 takes 0–5s, beat 2 takes 5–10s, beat 3 takes 10–15s. Maintain character identity across beats.

---

## Pacing across storyboard frames

Allocate time per frame based on the narrative weight:
- 4 frames → 3.75s each (even allocation)
- 4 frames with weighted action: 3s + 3s + 5s + 4s (climax frame gets more time)
- 5 frames → 3s each

State the allocation in the prompt:

> Pacing: @image1 holds for 3 seconds (establishing). @image2 holds for 3 seconds (development). @image3 holds for 5 seconds (climax — the longest beat). @image4 holds for 4 seconds (resolution).

---

## Visual style consistency across frames

If the storyboards are in a specific style (anime, manga, watercolor), state this and lock it:

> Visual style: 1980s seinen manga ink — bold black lines, cross-hatching, screentone dots, no color, no grey. The video must maintain this aesthetic across all frames. Do NOT shift to photoreal or 3D.

---

## Speech bubbles and on-screen text

If the storyboards include dialogue in speech bubbles:

> Speech bubbles from @image1 through @image4 should remain in their original positions. Reproduce the kanji / English text exactly as shown in each frame. Animate the speech bubbles entering frame at the appropriate beat.

---

## When story completion needs additional inputs

The user may have the storyboard but no script, or the script but no storyboard. State what's missing and offer to fill the gap:

- Storyboard only → infer dialogue and SFX from the visual content
- Script only → infer visual beats from the dialogue / action descriptions
- Both → use both, with the visual storyboard as the primary

---

## Common story-completion requests

- "Animate this comic page" — comic panels become a video sequence
- "Bring this storyboard to life" — pre-production storyboard becomes the actual video
- "Adapt this short story" — written narrative becomes visual sequence
- "Recreate this advertisement script" — copy-only ad script becomes finished video
- "Tell the story of these 4 product photos" — product images become narrative sequence

---

## Limits

- Up to 9 reference images per generation
- Sequential interpretation works best with 3–6 frames
- More than 6 frames in a 15-second video means each frame gets <2.5s — Seedance compresses unevenly
- For longer narratives, split into multiple Seedance calls (independent segments) and assemble in NLE

---

## Auto-camera and auto-storyboarding

Seedance has native auto-storyboarding capability — given a story, it can plan camera moves, cuts, and pacing without explicit shot direction. Use this when the user just wants Seedance to handle the cinematography:

> Auto-storyboard the following narrative across 15 seconds. Apply [genre]-appropriate camera grammar. The model should plan the shot structure: [paste narrative].

For more directorial control, specify shots explicitly. For exploratory creative, let auto-storyboard handle it.
