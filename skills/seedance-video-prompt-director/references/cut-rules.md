# Cut grammar rules

Cuts are where most prompts break down. The engine renders each shot reasonably; the join between shots is where geometry, identity, and pacing fail. These rules govern how cuts work in Seedance 2.0 prompts.

---

## Double contrast (mandatory on every cut)

Every cut changes BOTH shot size AND camera character. If you only change one, the cut reads as continuation, not as a transition.

**Shot-size scale (smallest to largest):**
ECU (extreme close-up) → close-up → medium close-up → medium → wide → extreme wide

**Camera modes:**
Handheld | Static / locked-off | Stabilized tracking | Crane / vertical move | Aerial / drone | Steadicam / gimbal

**Cut from medium-handheld → wide-static** = double contrast. Cuts cleanly.
**Cut from medium-handheld → medium-stabilized-tracking** = single contrast (only camera mode changed). Reads as continuation.
**Cut from medium-handheld → close-up-handheld** = single contrast (only shot size changed). Reads as continuation.

Same camera character can repeat after one beat in between (handheld → static → handheld is fine). Don't repeat camera mode on consecutive cuts.

---

## Re-anchoring after cuts

After every cut, restate spatial facts. Who is where, what direction they face, what they're holding, how they relate to the environment.

**Before cut:** "She sprints right-to-left along the alley wall, briefcase in left hand."

**Wrong reanchor:** "She skids to a stop." (Seedance doesn't know where, doesn't know facing, doesn't know if she still has the briefcase)

**Right reanchor:** "She skids to a stop at the alley's left exit, briefcase still in left hand, body facing back into the alley."

Re-anchoring is annoying to write but it's what keeps Seedance from drifting on continuity.

---

## 180° rule (axis preservation)

When a cut returns to established space, characters must keep the same screen direction. If A faces right and B faces left in the wide shot, A still faces right in the close-up. Don't cross the line of action between cuts unless the camera explicitly travels across it on screen.

If you must cross the axis, write the camera move that does it — a lateral track, a slow orbit — so Seedance executes the cross visibly rather than teleporting.

---

## Inserts: any scale, beat-free, causally motivated

Inserts are sub-second (0.3–0.5s) dramatic punctuation cuts. They can be any shot size — usually macro. They are not story beats.

**Three rules for inserts:**

1. **Inserts must NOT contain story beats.** They're static moments — a hand gripping a railing, a single dust particle drifting, a fingertip pausing on a button. If the insert advances the plot, it's a regular shot, not an insert.

2. **Causally motivated.** The viewer must understand WHY they see this detail. ✅ "Hero slammed onto the hood → his hand gripping the metal." ❌ "Generic boot stepping in a puddle." The insert has to be linked to the surrounding action.

3. **Name the subject.** Specify WHOSE hand, WHOSE eye, WHOSE boot. Without attribution, Seedance renders generic anonymous body parts and the insert reads as stock footage.

Inserts also obey the double contrast rule — they must contrast in both shot size and camera character with the shot before AND after.

---

## Hard cuts vs match cuts vs whip pans

**Hard cut** — instantaneous transition between two shots. Use most of the time. Default cut.

**Match cut** — a visual rhyme bridges the cut (a shape, a motion, a color). Useful when transitioning between locations or time periods. Specify what's matching: "match cut on the spinning wheel — wagon wheel becomes hubcap."

**Whip pan** — fast camera motion blurs the cut into the next shot. Specify the direction: "whip pan left to right reveals the warehouse interior." Keep the velocity high enough that the motion blur reads.

**Smash cut** — abrupt, jarring cut typically with a tonal shift. Specify when you want the jolt: "smash cut to white," "smash cut to silence."

Don't use fades or dissolves unless the brief specifically calls for them — they read as low-energy and aged.

---

## When to cut vs when to hold

**Cut when:**
- The action moves to a new location
- A new character enters the scene with their own kinetic energy
- The camera grammar needs to shift (handheld to locked-off, wide to macro)
- A reaction or insert needs its own frame to land

**Hold when:**
- The action is a single continuous beat
- A camera move IS the visual interest (a long crane, a slow push-in that's the whole point)
- The escalation is happening within the frame and cutting would diffuse it
- You're in POV / one-take format

Generally, action scenes cut more (a 15s action scene might have 6–8 cuts). Cinematic narrative scenes cut less (a 15s narrative scene might have 2–4 cuts). POV and one-take never cut.

---

## Cut on motion peaks

When you do cut, cut on the peak of in-camera motion in the outgoing shot, and open the incoming shot at peak motion as well. The two motions blend across the cut and the join feels propulsive.

**Bad:** Cut from a static shot of someone reaching → static shot of them holding the object. Two stillnesses joined by a cut. Dead.

**Good:** Cut from the hand mid-grasp (motion peak) → the object mid-rotation as it's lifted away (motion peak). The cut feels like one continuous gesture even though it's two shots.

This is especially important when scenes don't have explicit transitions — the visual energy carries the cut.

---

## Insert cadence

Inserts work best at 1 per 5–7 seconds of runtime. More than that and the cut rhythm gets choppy. Less and the prompt feels macro-deprived. A 15s prompt with 2 well-placed inserts reads as cinematic; a 15s prompt with 5 inserts reads as ADHD.

---

## Cuts inside a single Seedance generation

Seedance handles up to about 6–8 cuts cleanly in a 15-second generation. Past that, cuts get blurry and beat boundaries dissolve. If your scene needs more than 8 cuts, either split into two generations or compress some beats into longer single shots.

For 7-second scenes, target 3–5 cuts. For 11-second scenes, target 5–7 cuts. For 15-second scenes, target 6–8 cuts.

---

## Cuts precision scale

Choose the tightest level of control the shot actually requires. Four registers, most to least precise.

**Oner** — one continuous take. Write: *one uninterrupted shot, no internal cuts, the camera never breaks the take.*

**Sequential cuts (untimed)** — beats matter, exact seconds do not. Label them in Movement:
```
CUT 1 — [beat one]
CUT 2 — [beat two]
CUT 3 — [beat three]
```

**Timed multi-shot** — beats land on specific clock positions, every cut declared with its second value and its cut type written out:
```
0.0s → 1.2s — [beat one]
1.2s — HARD CUT
1.2s → 3.5s — [beat two]
```

**Freestyle b-roll** — the camera and the edit get to explore. Rare; only when the user asks for it out loud.

Whenever cuts are specified at all, close the door on unintended edits: *the camera adds no additional cuts, edits happen only at the marks above.*

---

## Cut vocabulary Seedance recognizes

`HARD CUT` · `SMASH CUT` · `MATCH CUT` · `INSERT CUT` · `REVERSE CUT` · `WHIP CUT`

Dissolves, crossfades, fades to black and transition effects only when the user explicitly names one. Otherwise hard cuts.

---

## Continuity carry list

Every internal cut holds all of these. State the ones the scene puts stress on rather than listing all thirteen:

same active subject set · same location geography · same screen direction unless the camera visibly crosses · same gaze targets · same left/right relationship · same light direction and colour temperature · same wardrobe · same wounds and dirt · same props and hand states · same blood, snow, dust, sweat, water, fire, smoke state · same object states · same emotional progression

Never reset the action after a cut. Never teleport a subject. Never change distance to a landmark unless elapsed time and visible movement justify it. Never introduce a new prop or subject after a cut unless the user asked for it.

Every cut needs a reason. If a cut exists only because the prompt has been running a while, cut it.

---

## Whip pan timing

A whip needs at least 0.8 seconds of motion to render as a blur. Anything shorter renders as a hard cut.

```
0.3s — Subject A framed, held
0.8s — WHIP begins, motion blur across the pan
1.4s — Subject B framed, held
```

---

## Speed changes

When mixing real-time and slow-motion beats in one prompt, put a hard cut at every speed change. Never blend speed inside a single continuous shot — one speed per beat, cut cleanly at the transition.

---

## Lens per cut

Each shot gets its own FOV degree only when the content class changes. Hard cuts only between different lens characters; no smooth FOV transitions, no lens drift inside a shot, no lens change without a new shot. For the same lens across all beats, declare it once and restate it at the top and close of every beat — see the extreme-FOV stack in `optics.md`.
