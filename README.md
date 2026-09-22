# Produced by Chi skills

This is my personal collection of reusable AI skills and creative workflows for video, social content, and visual storytelling. Each skill has its own `SKILL.md`, plus any reference material, templates, or scripts it needs.

The skills use the standard `SKILL.md` format, so they can work with Codex, Claude, and other agents that support custom skills.

## What is included

- [Preproduction workflow](skills/preproduction-workflow/SKILL.md) is one skill with treatment, breakdown, and paperwork modes. It can develop the creative direction, plan shots and resources, and draft project documents such as estimates, agreements, invoices, releases, and usage schedules. Legal and tax terms need qualified review.
- [YouTube thumbnail generator](skills/youtube-thumbnail-generator/SKILL.md) creates, reviews, and improves YouTube thumbnails with a native image tool or a paste-ready prompt package.
- [Seedance video director](skills/seedance-video-director/SKILL.md) turns a video brief into a detailed Seedance 2.0 prompt. Its reference guides cover camera work, continuity, lighting, genre, and Seedance capabilities.

## How to use a skill

1. Open the skill you want inside `skills/`.
2. Copy the whole skill folder into your agent's custom-skills directory. Keep its `SKILL.md` and every supporting file together.
3. Start a new task and name the skill, or describe work that matches its purpose.

Install `preproduction-workflow` as one folder. Its modes live in `references/`, so there are no other skill dependencies. Ask for a treatment, breakdown, paperwork, or the full workflow.

For example, install `skills/seedance-video-director/` as a complete folder. Do not copy only its `SKILL.md`, because it reads files in `references/` when it needs them.

## Repository layout

```text
skills/
  preproduction-workflow/
    SKILL.md
    references/
  youtube-thumbnail-generator/
    SKILL.md
  seedance-video-director/
    SKILL.md
    references/
```

## Adding a skill

Create `skills/<skill-name>/SKILL.md`. Place the skill's scripts, templates, and reference files in the same folder. Then add it to the list above.
