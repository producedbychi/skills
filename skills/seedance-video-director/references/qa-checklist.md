# Quality checks

Apply these checks to the selected capability and format. A reference-only, cut-only, or realism-only check can be not applicable. Fix failed checks before delivery; report unresolved dependencies rather than inventing inputs.

---

## References and isolation

- Is every tag in the prompt actually used in this shot?
- Are all stale tags from previous prompts gone?
- For reference-dependent subjects, does each have a supplied canonical identity reference, including subjects visible in a plate? For text-only subjects, is identity defined consistently without invented tags?
- When a plate is supplied, is its role explicit? Does a requested first-frame or last-frame reference retain its framing role?
- Are scene numbers, script headers, prior-scene summaries and "same as before" phrasing all gone?
- Are platform names, tool names and meta-commentary all gone?

## Frame and subjects

- Is the first frame correct, and are required subjects visible at 0.0s?
- Is every subject pinned to a screen position, a depth layer and a frame occupancy?
- Is every important gaze line stated, separately from body orientation?
- Is landmark proximity anchored by contact or a metric, not by "near"?
- Are props in the correct hands with contact points named?
- Does each subject have its own Subject Lock block with a lock-down line?
- Does wardrobe follow the supplied reference, or the written description for a text-only subject?
- Is the prompt age-blind throughout?

## Optics

- Is the FOV a value on the ladder — never an off-ladder degree, never millimeters alone?
- Does the lens character match the content class of the beat?
- Are content classes kept out of each other's beats?
- Is the lens protected from drift where drift was a risk?
- Is there one closing Camera Capture block, with each shot's camera differences stated inside it when needed?

## Light, physics, motion

- Does the lighting describe the requested style? For directional lighting, are its source, direction, camera side, and exposure priority clear?
- Does the lighting preserve the selected intent, including flat or evenly lit treatment when requested?
- Is every colour tied to a surface, a source and a purpose?
- Are the actions physically possible in the available runtime?
- Does the motion have contact, weight transfer and follow-through where it matters?
- Are the four Movement layers named, including any layer that is "nothing else moves"?

## Structure and timing

- For prompts with cuts, is the cuts precision register chosen and stated correctly?
- Does every cut have a reason, and does the continuity carry list hold across it?
- Are timing blocks internally consistent, and do per-shot times sum to the runtime?
- Do the title runtime and the Camera Capture runtime match?
- Is the cut count inside what the engine renders cleanly for this duration?
- Do sub-second cut sequences have a reference per cut, or were they extended or split?

## Sound and text

- Is dialogue only the scripted line, with its timing stated?
- Do body sounds in Sound Bed have corresponding visible body motion in Movement?
- If on-screen text is requested, are its wording and placement explicit? Otherwise, is the text suppression line present at the close of Last Frame?

## Craft

- Is the prompt written entirely in the visible — no mood-word abstractions, emotion in muscle, speed in km/h, atmosphere in % and meters?
- Is the phrasing positive, with negatives only as trailing clauses on the locks they protect?
- Is style distributed rather than prefixed?
- Is the antislop list clean?
- Does the prompt fit the main skill's word target, with any shorter simple prompt still containing the controls its action requires?
- Is the whole prompt in English?
