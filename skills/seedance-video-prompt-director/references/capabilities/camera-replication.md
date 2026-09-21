# Camera & motion replication

Copy camera movement, complex action, or pacing from a reference video onto a new subject. The Seedance capability for "I want the camera moves from @video1 but with my subject."

---

## When the user is in this capability

- "I love the camera moves in this video — replicate them with my product."
- "Match the dance moves from this reference video, but with our spokesperson."
- "Use the same fight choreography as @video1."
- "The camera in this reference does a great Hitchcock zoom — do that with my actor."

If the user provides a reference video and wants its motion / choreography / pacing copied to a new subject, you're in camera-replication.

---

## Prompt structure

```
Reference @video1's [camera moves / action / pacing] + [new subject as @image[N] or text description] + [scene description]
```

Example:

> Reference @video1's full sequence of camera moves. Match the angles, push-ins, and cut rhythm exactly. The subject this time is @image1 (the buyer character) walking through @image2 (the warehouse). The camera grammar follows @video1, but the content is buyer + warehouse instead of @video1's original content.

---

## Critical distinction: camera vs subject

This capability separates the camera grammar from the content. Be explicit:

> Reference @video1 for: camera moves only.
> Do NOT reference @video1 for: subject identity, scene content, or color grade.
>
> Subject: @image1 walking through a warehouse.
> Color grade: warm Golden Hour, NOT @video1's grade.

Without this clarification, Seedance may copy more than the camera (subject, color, atmosphere all bleed in).

---

## What can be replicated

- **Camera moves** — push-ins, pull-backs, orbits, lateral tracks, crane descents
- **Pacing / cut rhythm** — beat density, hold lengths, transition timing
- **Angles** — low-angle, OTS, dutch, eye-level patterns
- **Action choreography** — specific movements (fight beats, dance moves, gesture patterns)
- **Speed dynamics** — slow-motion ramps, speed changes, hyperlapse
- **Specialty moves** — Hitchcock zoom (dolly zoom), bullet-time, snap-zoom

State explicitly which of these you want replicated.

---

## Specialty patterns

### Hitchcock zoom / vertigo zoom
> Reference @video1's Hitchcock zoom moment (the dolly-forward + zoom-out combination). Apply this to the moment of recognition where my character realizes the truth. Zoom dynamic should match @video1 exactly.

### Music video pacing
> Reference @video1's beat-aligned cut pacing. Do not match @video1's content — only its rhythm. Cuts in my video should land on the same intervals as cuts in @video1.

### Action choreography
> Reference @video1's fight choreography. The hero @image1 performs the same sequence of moves as @video1's fighter, in the same order, with the same impact beats. The opponent and environment can differ.

### One-take / long-shot replication
> Reference @video1's continuous tracking shot. Replicate the camera's path through the environment exactly — start position, motion, end position. Apply this to my character @image1 moving through @image2.

---

## Combining with consistency control

Camera replication often pairs with character consistency:

> Reference @video1's camera moves and pacing.
> Subject @image1 throughout (character consistency).
> Scene @image2 (location consistency).
> Color grade: Kodak Portra warmth, NOT @video1's grade.

State all references and their roles. Seedance handles each one.

---

## When camera replication isn't quite right

If the user wants:
- Just the visual style (color grade, atmosphere) but different camera → use **consistency-control** with the style image as `style reference only`
- The exact same beats and content → use **vfx-template** (creative replication, full template copy)
- A continuation of an existing video → user wants video extension (not in this skill — split into independent segments)

Camera-replication is specifically about transferring CAMERA GRAMMAR / CHOREOGRAPHY to a new subject.

---

## Limits

- Reference videos consume more credits than reference images on most Seedance pricing tiers
- Reference video must be 2–15 seconds, 480p–720p
- Up to 3 reference videos per generation
- Highly stylized choreography (specific dance moves, specific fight techniques) may not transfer perfectly — Seedance approximates the motion vocabulary

---

## Common camera-replication requests

- Apply a viral video's camera move pattern to brand content
- Copy a film's signature shot to a music video
- Transfer fight choreography from a stunt reel to original characters
- Use a beauty ad's camera grammar with a new product
- Match a music video's beat-cut pacing to a custom piece
- Replicate a specific cinematic move (Hitchcock zoom, bullet-time, oner) on new subjects
