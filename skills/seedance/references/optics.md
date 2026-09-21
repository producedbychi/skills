# Optics — FOV degrees, selection, and drift control

Seedance treats a field-of-view stated in degrees as a discrete anchor. Millimeters read as a suggestion. Apertures, ISO values, and lens brand names read as flavor text and control nothing. Multi-beat sequences that name only millimeters drift lens character between beats; degrees hold.

**Write the degree in the prompt body. Millimeters go in parentheses as a reader aid.** `47° (50mm) eye-level neutral`. Never millimeters alone, never an off-ladder degree.

---

## The FOV ladder

Only these values. 23° is not on the ladder — use 18° or 29°.

| FOV | mm equiv | Camera distance | Character | Use for |
|---|---|---|---|---|
| 180° | fisheye | contact to 0.3m | spherical bulge | POV chaos, dream state, hallucination |
| 107° | 14–16mm | 0.5–0.8m | ultra-wide rectilinear | vast interior scale, epic establishing, foreground looming |
| 84° | 20–24mm | 1–1.5m | classic wide | full-body group blocking, environmental action |
| 63° | 28–35mm | 2–3m | reportage wide | observational, walking-alongside, documentary |
| 47° | 40–50mm | 3–5m | eye-level neutral | universal medium, dialogue two-shot, waist-up |
| 29° | 75–85mm | 4–6m | portrait compression | isolated bust, tight dialogue coverage |
| 18° | 100–135mm | 6–8m | portrait tight | identity-hold close-up, held emotional beat |
| 12° | 180–200mm | 10–15m | tele detail | hand insert, object close, jewelry, texture |
| 8° | 300–400mm | 20–25m | extreme long lens | anchored-far observation, sports broadcast, surveillance |

---

## Selection by content type

Pick the FOV from what the beat is *about*, not from how big you want the subject to look.

**Face and identity**
- close face with the room still legible → 84° (the wide-portrait technique)
- medium portrait → 29°
- tight emotional close-up → 18°
- distant observation of a face → 8° with mandatory foreground occlusion

**Environmental action**
- natural documentary action → 47°
- wide environmental action → 84°
- large-scale geography → 107°
- extreme immersion → 180°, only when the entire beat is environmental

**Detail and macro**
- standard detail insert → 12° or 18°
- a small object made huge with deep background → 84° from inches away (foreground-loaded wide)

**Observation at distance**
- broadcast, paparazzi, wildlife, watchtower → 8°
- compressed surveillance portrait → 12° or 8° with foreground occlusion and stated atmospheric haze

---

## Content-FOV alignment rule

The lens must match the content class of the beat. Wide works when the content is environmental, spatial, physical, or body-near-camera. Long works when the content is portrait, observation, isolation, or compression. Macro works as its own insert beat.

**Do not mix content classes inside one lens beat.** Face portrait plus environmental geography plus macro detail in a single beat is the direct cause of lens drift — the model averages toward a comfortable middle and you lose all three. If the scene needs multiple content classes, use internal cuts and assign a separate FOV to each shot.

---

## Visual outcome stacks

The degree sets the anchor; the observable outcome holds it. Seedance responds to described results more reliably than to specifications.

**For any long-lens shot, include at least four:**

- background compressed flat behind the subject
- background dissolved into a soft color wash
- only the subject is sharp, everything else soft
- razor focus on the eyes
- close framing achieved through lens reach, not physical proximity
- camera positioned far from the subject in physical space
- atmospheric haze suspended between camera and subject
- foreground occlusion framing the subject as soft dark bokeh

**For any wide shot, include at least three:**

- foreground body presence looms larger than natural
- environment remains visible to the frame edges
- deep edge-to-edge focus
- straight lines stay rectilinear, no fisheye curve
- camera physically close to the subject
- no long-lens compression, no portrait bokeh

---

## Anti-drift locks

Add only when the diagnosis flagged drift risk — extreme FOV, or a lens character held across multiple beats.

**Long lens:**
> No part of this shot becomes wide or normal coverage. Wider framing comes from the camera moving farther back at the same long-lens reach, not from a lens change. The background stays compressed and dissolved in every frame.

**Wide:**
> No part of this shot becomes portrait coverage. The environment stays visible around the subject, the camera stays physically close, and the frame keeps its wide spatial expansion with deep readable context.

**Neutral:**
> No wide distortion, no long-lens compression. The image stays human-eye neutral throughout.

**Extreme-FOV multi-beat stack.** At 8°, 107°, or 180° across multiple beats, the model loses the lens by beat three. Four mechanisms in combination, no substitutes:

1. one environment or location reference held across every beat
2. the FOV degree spoken at the top of every beat
3. the FOV degree repeated at the close of every beat
4. every color tied to a surface, a light source, and a compositional purpose — never a bare palette list

Drop any one and the sequence drifts.

---

## Named optical techniques

Use by name plus application when the shot calls for one.

**Voyeur / long-lens observation.** Three ingredients simultaneously: a foreground obstruction covering 20–30% of frame thrown out of focus (wall edge, pillar, branch, curtain); suspended atmosphere between camera and subject stated as % density; 8° or 12° with the operator far from the subject. The obstruction can change between shots in a sequence; the vantage stays anchored. Never zoom in on a voyeur shot.

**Broadcast press-box.** `8° (300mm), handheld with a 1–2cm hunting tremor, operator hunting the action from a fixed distant vantage.`

**Foreground-loaded wide.** Small object made huge, background pushed into deep space: `84° (24mm), low angle, camera inches from the object.` For hero props, hands, hardware.

**Wide portrait.** A close face rendered wide so the room stays legible: `63°–84° on a centered face at normal working distance.` The face stays the anchor; the world stays in frame without going soft.

**Compressed atmosphere column.** At 8°–12°, name the particulate as a stacked column between camera and subject: *a thick vertical column of suspended dust between the operator and the figure*, *a wall of heat haze stacked in front of the subject.*

---

## Anti-patterns

Never write these as lens instructions:

- extreme / ultra / super wide-angle lens
- "wide shot" or "establishing shot" as a lens instruction
- zoom out plus wide-angle in the same clause
- "tight wide framing"
- f-stop, ISO, or lens brand as primary control
- two compound camera movements in one shot
- negative-only lens control
- an off-ladder degree value
