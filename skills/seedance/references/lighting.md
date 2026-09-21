# Lighting — a constraint, not decoration

Seedance's default is flat, evenly exposed, front-lit coverage. Every other lighting intent has to be defended in the prompt, and it has to be defended as a physical arrangement rather than a mood word. "Moody lighting" renders as flat. "The camera sits on the shadow side of the subject with the sun behind them" renders as intended.

Lighting is written in the World Plate and echoed in Movement and Last Frame — not as a top-of-prompt style prefix.

---

## Always define

- primary light source (and whether it is visible in frame)
- light direction relative to the subject
- which side the camera is on relative to the light
- which side of the subject is in shadow or rim
- background brightness relative to the subject
- exposure priority — what the shot is exposed *for*
- which highlights are permitted

Worked example:

> The camera sits on the shadow side. Morning sun enters from camera-right, behind and slightly to the side of him, laying gold rim light along the shoulder and the top of the head while the camera-facing side stays dark. Background reads two stops brighter than the figure.

---

## Backlit / contre-jour lock

The most commonly requested and most commonly failed lighting setup. When the intent is silhouette or backlight:

> The subject stays between the camera and the brighter background. The camera holds on the shadow side. The face stays in deep shadow. Only rim light, edge light, wet speculars, eye glints and environmental bounce reveal detail. No frontal key, no beauty fill, no flat exposure.

If previous generations still came back flat, escalate — this is the strongest phrasing available:

> The entire frame is exposed for the backlight, not for the face. The face is allowed to fall into crushed shadow. The silhouette and the rim contour carry the image.

---

## Exposure priority

Naming what the shot is exposed for resolves most lighting ambiguity in one clause.

- *exposed for the window, interior falls dark*
- *exposed for the practical lamp, the room falls off into black*
- *exposed for skin, the window blows out to white*
- *exposed for the sky, the foreground reads as silhouette*

---

## Lighting characters

Pull one, then write it as an arrangement.

| Character | Physical arrangement |
|---|---|
| Natural / available | single dominant source named, no added fill |
| Soft single source | large diffuse source at 45° camera-left, gentle falloff, no second source |
| Hard single source | bare source, hard-edged shadows with defined boundaries |
| Practical-motivated | the visible in-frame lamp, sign, or screen is the only source |
| Side rake | source at 90° to the lens axis, long shadows across texture |
| Rim / edge | source behind the subject, contour light only |
| Underlit | source below eye line, shadows rising up the face |
| Volumetric | visible beams cut by atmosphere, particulate density stated |
| God ray | one directional shaft through an obstruction, named |
| Top-down | overhead diffusion, shadows falling straight down |

---

## Continuity across cuts

Light direction is one of the first things to break on an internal cut. Any multi-shot prompt carries: same source, same direction, same color temperature, same exposure priority. State it in the continuity carry line rather than trusting the model to hold it.

---

## Colour discipline

Never write a bare palette list. Every colour attaches to a surface, a light source, and a purpose in the shot.

- ❌ teal and amber, moody blue tones
- ✅ sodium-amber from the single street lamp 30 meters back, catching the wet brick on the left wall; the unlit right side of the alley falls to blue-black

Bare palette lists are the second-largest cause of grade drift across beats, after millimeter-only lens specs.
