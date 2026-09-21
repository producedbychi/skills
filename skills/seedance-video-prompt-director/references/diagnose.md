# Diagnose — predict the failure before you write

Most bad Seedance output is not a writing problem, it is a missing lock. Run this pass after inventory and before you write a single line of prompt. For every risk that reads as live, add the named lock to the prompt body. Do not add locks for risks that do not apply — an unnecessary lock is noise that dilutes the ones that matter.

Diagnosis is silent. It never appears in the output.

---

## The risk table

| Risk | Live when | Lock to add |
|---|---|---|
| Empty first frame | Subject must be present at 0.0s | First-frame occupancy lock (`control-locks.md`) |
| Delayed character reveal | Multiple subjects, one arrives late in the described action | First-frame occupancy lock, name every subject at 0.0s |
| Model opens on a useless establishing wide | Scene has a location worth showing | State opening frame size explicitly, name the subject inside it |
| Character drifts far from the landmark | Any "beside / near / at the X" relationship | Landmark proximity lock — physical contact or metric distance |
| Gaze line reverses | Two or more subjects relating to each other | Gaze line lock, separate from body orientation |
| Body orientation ambiguous | Subject relates to something off the frame axis | Torso-facing declaration alongside gaze |
| Left/right positions flip | Two subjects on the same depth plane | Cross-Frame Rules — never swap, never cross center |
| Camera picks the wrong side | Backlight, silhouette, or shadow-side intent | Camera-side declaration in the lighting block |
| Lens drifts to a comfortable middle | Extreme FOV (8°, 12°, 107°, 180°) or multi-beat | Anti-drift lock + per-beat FOV restatement (`optics.md`) |
| Shot goes flat front-lit | Any backlit, low-key, or contre-jour intent | Lighting priority lock + exposure priority (`lighting.md`) |
| Reference identity overwritten by prose | Character or product reference attached | Minimum-anchor character rule — trust the reference |
| Stale tag leaks in | Sequential shots in one session | Context isolation pass (`control-locks.md`) |
| Extra or duplicate characters appear | Crowd scenes, or a subject exits and returns | Subject census line, exit-frame rule from `engine-rules.md` |
| Prop lands in the wrong hand | Any held object that matters | Contact-point declaration — which hand, which grip |
| Motion goes floaty or rubbery | Weight, impact, weapons, falls, running | Physics lock (`physics.md`) |
| Dialogue starts at the wrong time | Any spoken line | Explicit line timing + silence padding |
| Location reference read as framing instead of geography | Environment plate attached | Plate-role declaration — geography and materials, not camera angle |
| Multi-shot cut resets continuity | Any internal cut | Continuity carry list (`cut-rules.md`) |
| Cut described but not rendered | 3+ cuts inside 4 seconds | Sub-second cut rule from `engine-rules.md` — one reference per cut, or extend, or split |
| Body sound with no visible motion | SFX block names breath, sigh, gulp | Audio-visual sync pairing from `engine-rules.md` |

---

## The two questions that catch the most

**"What does frame one look like?"** Answer it out loud, silently, before writing. If the answer is vague, the generation will be too. This single question catches the empty-first-frame, delayed-reveal, and useless-establishing failures at once.

**"Where is the light coming from, and which side is the camera on?"** If you cannot answer both, the shot will render flat front-lit regardless of how the mood is described.

---

## Repair pass

If any of these read true on a finished draft, fix before delivery.

| Symptom | Fix |
|---|---|
| Reads poetic rather than physical | Rewrite Scene & Mood as observable action |
| Too many actions for the runtime | Split into multi-shot, or push the surplus to a second generation |
| Character could drift | Tighten Subject Lock with contact points and ground marks |
| Subjects could swap sides | Tighten Cross-Frame Rules |
| Wardrobe re-described from an attached reference | Cut the redundant description |
| Two camera specs in one prompt | Collapse to a single Camera Capture line |
| Genre registers fighting each other | Keep one base dominant, demote the rest to vocabulary |
| Last frame vague or missing | Write a specific closing composition |
| FOV drifting across beats | Apply the four-mechanism consistency stack in `optics.md` |
| Over word budget | Trim Subject Lock and Movement first, then Cross-Frame Rules |
| Negative-only control | Rewrite as the desired state, keep the negative only as a trailing clause |
