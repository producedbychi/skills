# Produced by Chi skills

This is my personal collection of reusable AI skills and creative workflows for video, social content, and visual storytelling. Each skill has its own `SKILL.md`, plus any reference material, templates, or scripts it needs.

The skills use the standard `SKILL.md` format, so they can work with Codex, Claude, and other agents that support custom skills.

## What is included

- [Preproduction workflow](skills/preproduction-workflow/SKILL.md) coordinates the creative treatment, project breakdown, and project paperwork for a client project.
- [Creative brief to treatment](skills/creative-brief-to-treatment/SKILL.md) develops a clear concept and direction from a brief or rough idea.
- [Project breakdown](skills/project-breakdown/SKILL.md) turns the chosen direction into shots, asset needs, dependencies, and a crew or editor handoff.
- [Project paperwork](skills/project-paperwork/SKILL.md) drafts and cross-checks estimates, scopes, agreements, invoices, releases, and usage rights. Legal and tax terms need qualified review.
- [YouTube thumbnail generator](skills/youtube-thumbnail-generator/SKILL.md) creates, reviews, and improves YouTube thumbnails with a native image tool or a paste-ready prompt package.
- [Seedance video director](skills/seedance-video-director/SKILL.md) turns a video brief into a detailed Seedance 2.0 prompt. Its reference guides cover camera work, continuity, lighting, genre, and Seedance capabilities.

## How to use a skill

1. Open the skill you want inside `skills/`.
2. Copy the whole skill folder into your agent's custom-skills directory. Keep its `SKILL.md` and every supporting file together.
3. Start a new task and name the skill, or describe work that matches its purpose.

To use `preproduction-workflow`, install it beside `creative-brief-to-treatment`, `project-breakdown`, and `project-paperwork`. You can also use any of those three on its own. Keep each folder intact so its relative references work.

For example, install `skills/seedance-video-director/` as a complete folder. Do not copy only its `SKILL.md`, because it reads files in `references/` when it needs them.

## Repository layout

```text
skills/
  preproduction-workflow/
    SKILL.md
  creative-brief-to-treatment/
    SKILL.md
  project-breakdown/
    SKILL.md
  project-paperwork/
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
