# Text-only generation

No reference materials. The user describes a scene in plain text and Seedance generates from that description alone.

---

## When the user is in this capability

- "Make me a video of a sunset over the ocean."
- "I want a quick action scene of a robot fight."
- "Generate a 10-second product hero of a coffee mug rotating."
- "I don't have any reference images, just want to make this from a description."

If no images, videos, or audio are attached AND the user hasn't asked about consistency / matching a reference / continuing a previous video, you're in text-only.

---

## Prompt structure

Standard Seedance prompt structure applies. The format depends on the brief:

```
[Subject] + [action sequence] + [environment / lighting] + [camera language] + [style keywords]
```

Or in the longer format used by this skill:

```
[Cinematic opening line]

[Subject + environment + atmosphere paragraph]

[Shot or beat content per format]

[Optional SFX block]

[Optional negative prompt]

Total: [Xs] / [N shots] / [aspect ratio]
```

---

## Strengths and limits of text-only

Seedance handles short, kinetic, single-subject scenes well in text-only mode. It struggles when:
- The brief requires consistency across multiple shots (use `consistency-control` capability)
- The brief requires matching an existing video's style or motion (use `camera-replication` or `vfx-template`)
- The brief requires a specific person / face that the engine doesn't have a reference for (text-only generates a generic character; for specific identity, you need an image reference)

If the user's text-only brief implies any of the above, suggest they add a reference and shift capabilities.

---

## What text-only does best

- Atmospheric / environmental scenes (landscapes, weather, location moods)
- Single-character action where the character's identity doesn't matter beyond a description
- Generic product beauty shots where the product is described in detail
- Abstract / surreal / artistic content where invention is the point
- Quick exploratory generations to test direction before committing to references

---

## Specificity matters extra

In text-only, the prompt is the only source of truth. Be specific.

❌ "A car driving on a road."
✅ "A 1970s burnt-orange muscle car rumbling down an empty desert highway at golden hour, dust trailing behind it, heat-haze rising from the asphalt."

The text-only prompt describes the entire frame. Don't leave details to the model's interpretation if they matter to the brief.

---

## Style keywords carry extra weight

Include style keywords explicitly, distributed into their home blocks per `block-order.md` — grade and stock in Camera Capture, lighting in World Plate, texture in Capture Realism. Never as a style prefix at the top of the prompt.

> "Cinematic action realism, ARRI ALEXA aesthetic, 35mm anamorphic, controlled handheld, Industrial Noir grade, deep shadows, halation on highlights, fine grain, 16:9, 24fps."

This single line locks the visual aesthetic. Without it, text-only generations drift toward generic stock-footage look.

---

## Common text-only requests

- Scenic establishing (a forest at dawn, a beach at sunset, a mountain in winter)
- Product beauty (a watch on a marble counter, a perfume bottle catching light, a coffee mug steaming)
- Single-character action (a runner crossing a finish line, a dancer mid-leap, a chef plating food)
- Abstract / artistic (paint dropping into water, ink spreading on paper, fabric in slow-motion wind)
- Environmental atmosphere (rain on a window, dust in a sunbeam, fog rolling through trees)
- Sci-fi / surreal (a planet rising over a horizon, a city in space, a dragon over mountains)

---

## Multiple versions when text-only

For text-only requests, especially exploratory ones, produce **2–3 versions** with different design intents. Each version represents a different interpretation of the brief.

Example versions for "a coffee mug on a counter":
- **Version A — editorial product:** macro detail of the mug's rim, soft directional light, shallow depth, controlled push-in
- **Version B — atmospheric breakfast:** wider environmental, mug on a wooden table by a window, steam rising, slight handheld
- **Version C — viral social:** punchy hook with the mug snap-zoomed into frame, vertical composition, oversaturated color

Tell the user how the versions differ. Let them pick.
