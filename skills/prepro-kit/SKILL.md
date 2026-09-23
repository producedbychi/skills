---
name: prepro-kit
description: Prepare a video project with a creative brief, treatment, AV script, production breakdown, and stage-appropriate paperwork. Use for one document or the full planning package.
---

# Pre-pro kit

This is one installable skill. Its modes make different decisions and produce different artifacts. Read only the reference needed for the request, plus earlier-stage references when their output is missing and the current work depends on it.

| Mode | Job | Read |
| --- | --- | --- |
| `brief` | Define the project problem, audience, message, deliverables, and constraints. | [Creative brief](references/brief.md) |
| `treatment` | Propose a creative direction that answers the brief. | [Treatment](references/treatment.md); use [creative brief](references/brief.md) if no usable brief exists. |
| `script` | Write a two-column audio and video script from the chosen direction. | [AV script](references/script.md); consult the treatment or brief as needed. |
| `breakdown` | Turn a direction or script into a shoot, asset, and edit plan. | [Breakdown](references/breakdown.md); consult upstream material as needed. |
| `paperwork` | Draft the commercial or rights document needed at this stage. | [Paperwork](references/paperwork.md). |
| `full` | Build a connected preproduction package. | Read the references as each stage becomes relevant. |

An explicit mode wins. Otherwise select the smallest mode that answers the user's request. A request for an estimate does not require a treatment. A request for a treatment does not require a separate brief document if the supplied context already answers the brief questions. If the user invokes the skill with no project or deliverable, ask what they are making and which output they need.

## Shared operating rules

1. Inspect the supplied project folder, client material, existing documents, and approvals before asking questions. A project may have no existing brief, script, or treatment.
2. Keep a compact source of project facts: client and project, problem, objective, audience, message and proof, deliverables and channels, budget and timing, assets, decision-makers, rights, and constraints. Label material items `confirmed` when supported by the user's instruction or a supplied approved source, `proposed` when you recommend them, and `unknown` when evidence is missing. Identify the source of consequential facts. If sources conflict, surface the conflict.
3. Ask focused questions when an answer would change the creative direction, price, obligation, permission, or deadline. For other gaps, proceed with an explicit assumption or leave a field unresolved. Do not treat a generated draft, supplied asset, or unreviewed reference as approval.
4. Produce the requested artifact, not an explanation of what one should contain. Scale its detail to the project. If the user asks for a file, create it in the requested location and preserve existing files.
5. Before delivery, check the artifact against its mode's quality checks and the shared facts. State what is ready for a client decision, what is only a working draft, and the few decisions needed next. When delivering multiple artifacts, use a short manifest with each artifact's status, location if saved, and blocking input. Do not claim an artifact was saved if it appears only in the response.

For `full`, establish or normalize the brief, develop a treatment, write a two-column AV script for video deliverables, translate the work into a breakdown, and prepare only the paperwork relevant now. If the scope also includes email, a landing page, or other non-video pieces, define their role and content requirements in the brief and treatment; draft their copy only when requested. Do not force them into an AV script. The AV script can be beat-based when runtime is provisional, but it must show planned picture and sound. Do not manufacture an invoice or agreement merely to fill a package. In the manifest, mark each output `working draft`, `client review`, `approved` only with evidence, `pending input`, or `not applicable`, and explain omissions. If essential strategic inputs are missing, make a working brief with explicit decisions rather than a falsely approval-ready one. The user may still request provisional downstream drafts; carry the same assumptions through them. Stop before making a consequential legal or financial choice that cannot be grounded in supplied terms. Reconcile deliverables, dates, fees, revisions, and usage across all outputs.

This skill stops at preproduction. Source-media selects, editing, final-cut review, signing, sending documents, and collecting payment require their own request. If the project includes AI-generated media, the breakdown specifies shot intent, reference needs, and clearance questions. Generate media only when requested.
