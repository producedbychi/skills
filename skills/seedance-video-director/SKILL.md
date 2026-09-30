---
name: seedance-video-director
description: "Write or revise Seedance 2.0 video prompts from scene descriptions, scripts, storyboards, or supplied image, video, and audio references. Use when the user specifies Seedance as the target generator. Produce paste-ready prompts or connected segment prompts for longer pieces."
---

# Seedance video director

Produce paste-ready prompts that specify subject placement, visible action, camera behavior, lighting, timing, and continuity. Diagnose the shot's likely failure points before writing and add only the controls that address them.

## The workflow

### 1. Inventory

Catalog silently before writing anything.

Record the subjects, action, environment, duration, aspect ratio, style cues, dialogue, and references mentioned. Assign each attached reference a role such as character, plate, prop, motion, first frame, last frame, or audio.

Preserve supplied characters and their core attributes. For an open-ended scene, develop supporting locations, props, and environmental details; introduce named characters only when the user requests character creation.

### 2. Diagnose

Read [diagnosis](references/diagnose.md). Identify the risks this particular shot invites, then use the matching controls in step 6.

### 3. Confirm consequential unknowns

Ask one compact question when an unknown runtime, reference tag, or mode would materially change the prompt. For text-only requests, use the matching capability without asking for reference tags.

Do not ask when the user has given you what you need, when they are iterating on a prompt you just delivered, when they pre-confirmed a batch, or when they said to skip it. A confirmation turn on a clear request is friction, not care.

Use the user's established reference tags. Confirm unknown tags before producing a render-ready reference-dependent prompt.

### 4. Route

Pick the capability, format, and genre. Read the matching reference files. Treat reference examples as choices within this workflow, not as replacements for its output rules. Routing is complete when every supplied asset has a role, the shot format fits the request, and the diagnosis identifies which controls are needed.

**Capability.** `references/capabilities/<name>.md`. A request can be more than one; read all matching.

| Capability | Signal |
|---|---|
| `text-only` | no references, text only |
| `consistency-control` | same character/product/scene across shots, anchored by references |
| `camera-replication` | reference video, copy its camera moves or choreography onto new subject |
| `vfx-template` | reference video, reproduce its template with the user's elements |
| `story-completion` | storyboard images or a script to complete |
| `sound-control` | explicit voice/dialogue/SFX direction |
| `one-take` | continuous shot, no cuts, possibly across environments |
| `beat-sync` | visual rhythm matched to music or a beat reference |
| `first-last-frame` | both a start and an end frame set as separate references |

**Format.** `references/formats/<name>.md`. Ambiguous requests default to multi-shot.

- `multishot` uses numbered beats with visible cut-to-cut progression.
- `continuous` uses one timeline with timestamped beats and camera movement without cuts.
- `pov-orb` uses a locked first-person perspective without cuts or zoom.
- `animation` establishes the 2D or 3D style and times its segments.

**Genre.** `references/genres/<name>.md`.

Pick exactly one **base**, which sets the structural priority: `commercial-product` · `cinematic-narrative` · `documentary-warm` · `explainer-clarity` · `ugc-authentic` · `science-education` · `short-drama`.

Add zero to three **modifiers**, which overlay vocabulary and energy: `action-intense` · `cinematic-narrative` · `horror-thriller` · `viral-hook` · `fantasy-action` · `music-video`.

The base determines structure; modifiers affect vocabulary and energy. A cinematic commercial with action keeps the product as its focal subject while using the matching camera and movement guidance.

For action, general, or dialogue scenes, read `references/archetype-router.md` to choose the camera priorities, subject movement, and changes across the runtime.

### 5. Choose the optics

Read `references/optics.md`. Pick the FOV degree from the content class of the beat, not from how large you want the subject to read. Write the degree; millimeters go in parentheses as a reader aid.

When a beat needs different views of a face, scene geography, and a macro detail, assign each its own shot and FOV. Preserve continuous or locked-perspective formats when the user requests them.

### 6. Apply the locks

Read `references/control-locks.md` for whichever the diagnosis flagged: first-frame occupancy, spatial blocking, gaze and body orientation, landmark proximity, context isolation, minimum-anchor character description.

Read `references/lighting.md` when the shot needs directional, motivated, or stylized lighting.

Read `references/physics.md` when the shot involves weight, impact, weapons, falls, running, liquids or particles.

Read `references/cut-rules.md` for any prompt with an internal cut.

Read [engine rules](references/engine-rules.md) for generation limits and practical guidance. Verified limits in the selected frontend take precedence over stored numeric notes. Describe a prompt's expected behavior as an intention, not a guaranteed model result.

### 7. Write

Follow the block order in `references/block-order.md` exactly. Spatial facts before camera style. Optics near the bottom. Style distributed into its home blocks, never as a top prefix.

Target 280 to 400 words for a single shot and up to 600 for multi-shot. Keep simple requests concise when extra blocks would add unrelated controls.

### 8. Check the prompt

Read [quality checks](references/qa-checklist.md) and apply those relevant to the selected capability and format. Fix failed checks before delivery. A prompt is ready when its actions fit the runtime, reference tags match supplied assets, and its camera and continuity instructions agree. Report any unresolved input or unverified frontend limit.

### 9. Supply missing-reference prompts when needed

If the concept depends on references the user does not have, label the video prompt as a draft awaiting those assets. Supply style-matched image prompts for the user's chosen image generator and list what must exist before video generation. Keep final reference tags pending until confirmed.

## Prompt principles

Write visible actions and changes rather than abstract moods. Give each shot one dominant action, camera strategy, and lighting motivation. Preserve the user's stated perspective, opening, and ending. For attached identity references, describe the required state and contact points rather than competing with the image's appearance.

Use [prompt principles](references/prompt-principles.md) when wording actions, identity controls, camera variety, or negative constraints. Its examples explain how to phrase the selected controls; they do not require every shot to use every control.

## Output and completion

Default to one paste-ready English prompt in a fenced code block, using the labeled blocks from [block order](references/block-order.md). Put the title, runtime, aspect ratio, shot count, and reference upload list outside the code block. List only attached assets under Active References.

Produce two or three differentiated versions when the user asks for options or creative exploration. A longer runtime, multiple references, or mixed genres alone does not require extra versions. Each version must differ in its scene approach, format, or camera strategy.

For a piece longer than the selected frontend's per-generation limit, provide independent segment prompts with explicit continuity between them. Each segment states its final frame and the next segment's matching start. Preserve wardrobe, light direction, palette, and aspect ratio unless the brief calls for a change. Use [segment delivery](references/segment-delivery.md) for the handoff details.

Deliver the requested prompt or segments, their upload requirements, and any unresolved dependencies. This skill writes prompts; it does not imply that a video has been generated or that a prompt will succeed on the first render.
