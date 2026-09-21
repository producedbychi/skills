# One-take long shot

Seamless continuous flow across multiple environments without cuts. Seedance generates the camera path through the world without breaking visual continuity.

---

## When the user is in this capability

- "I want a oner — single continuous shot from the street, through the building, up the stairs, onto the roof."
- "One-take chase scene through multiple environments."
- "Seamless tracking shot, never cut."
- "Match @video1's continuous shot — no cuts, just the camera flowing through the world."

If the brief specifies "no cuts," "single continuous shot," "oner," or "long take" across multiple visual moments, you're in one-take.

---

## Prompt structure

```
One continuous shot, no cuts + [camera path description] + [reference images at each beat] + [全程不要切镜头 / "do not cut anywhere"]
```

The "do not cut" / "no cuts" / "全程不要切镜头" language is what locks Seedance to one-take mode. Without it, the engine defaults to inserting cuts.

Example:

> One-take continuous shot. The camera follows the courier @image1 through the building. Beat 1: starts at the building entrance @image2, courier enters. Beat 2: camera follows up the stairs @image3, courier climbs. Beat 3: camera enters the office @image4, courier hands off the package to @image5 (the recipient). Beat 4: camera turns and exits via the window onto the rooftop @image6. Continuous tracking throughout — no cuts, no transitions, no time skips.

---

## Multi-image one-take pattern

One-take often uses multiple images representing the locations the camera passes through:

> Locations:
> @image1 — building entrance
> @image2 — staircase
> @image3 — office
> @image4 — rooftop
>
> Continuous shot: camera enters @image1, travels through @image2 (climbing the stairs), arrives at @image3 (office reveal), exits onto @image4 (rooftop). The character @image5 is the through-line — visible at each location.
>
> No cuts. Continuous tracking throughout.

---

## Camera path description

Describe the camera's full path explicitly:

> Camera path: starts at street-level outside the building (eye-line), pushes forward through the entrance doors (slight upward tilt as the doors swing), tracks across the lobby (lateral motion), enters the elevator (camera holds at chest-height as the elevator ascends — visible elevator floor numbers passing), exits the elevator (camera resumes lateral motion), follows the courier down the hallway (50mm prime), enters the office (slight push-in to medium close-up at the desk), settles on the recipient's reaction.

The more explicit the path, the better Seedance executes the oner.

---

## Camera height changes

One-take can include camera height changes (rising, descending, climbing):

> Camera starts at chest-height, pushes through the entrance, then crane-up to drone-height as the camera rises above the building, follows the courier as they climb the fire escape, then crane-down to chest-height again as the camera arrives at the rooftop. Continuous motion throughout — the height change happens during the climb, not as a cut.

---

## Speed changes within one-take

One-take can include speed ramps without breaking continuity:

> The camera follows the runner at full speed for 5 seconds. RAMPS TO SLOW MOTION at the 5-second mark as the runner approaches the finish line — the camera continues its motion but in slow-motion. SNAPS BACK to real-time at the 8-second mark as the runner crosses the finish, camera continues into the celebration. No cuts, just speed changes within the continuous take.

---

## Person-passes / occlusions

One-take often uses occlusions (passing pedestrians, walls, vehicles) to provide visual variety while maintaining continuity:

> Camera tracks the courier in lateral motion. A pedestrian passes between the camera and the courier — partial occlusion. Camera continues. A truck drives between the camera and the courier — full occlusion for half a second. Camera continues, the courier still in frame after the occlusion clears.

Occlusions create natural rhythm in a long take without using cuts.

---

## Person-replacement during occlusion

A specific one-take pattern: the subject changes during an occlusion, but the camera doesn't cut.

> Camera tracks the woman in red @image1 walking forward. A pedestrian passes between the camera and the subject. After the pedestrian clears, the woman is gone — replaced by a masked figure @image2 staring after her in the same position. Camera continues forward without cutting.

This is a classic one-take reveal pattern. State it explicitly.

---

## Limits

- Up to 9 reference images per generation (for the locations / characters along the camera path)
- Seedance handles continuous motion across 4–6 distinct environments well in 15s. Past 6, the camera path gets compressed
- Speed changes work but be specific about when they happen
- Height changes work but specify the motion (crane-up, drone-rise, climbing-camera)

---

## What one-take does well

- Tour-of-environment shots (showing scope by traveling through)
- Hide-and-reveal (occlusion-based subject changes)
- Scale transitions (street → building → roof, micro → macro)
- Atmospheric immersion (the camera's path conveys mood)
- Hero entrances ("this is where they live, work, fight")

---

## What one-take struggles with

- Fast action with multiple combat beats (cuts give action weight; one-take diffuses it)
- Multiple character coverage (you can't OTS-cut between two speakers in one-take)
- Heavy VFX with explosive moments (one-take captures less of an explosion than multi-shot)
- Precision dialogue scenes (the camera commits to one position per beat, less coverage flexibility)

For these, use multi-shot or continuous formats with explicit cuts.

---

## Common one-take requests

- Spy / espionage tracking sequences
- Hotel / building tours showing scope
- Music video performance shots through environments
- Hero introduction shots
- Crime scene investigations (camera tracks investigator through evidence)
- Event coverage (camera follows host through a venue)
- Dance / choreography in transit

---

## Negative prompt for one-take

Always include:

```
Negative: no cuts, no transitions, no time skips, no fade-outs mid-shot, no scene jumps, no second camera angles introduced.
```

The negation is what locks the one-take format. Without it, Seedance may insert cuts.
