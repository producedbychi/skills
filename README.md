# Produced by Chi skills

This is my personal collection of AI agent skills for creative production and marketing. Use them to define brand positioning, plan video projects, prepare moodboards, generate ad images and YouTube thumbnails, direct AI video, and write clearer marketing copy.

I develop these skills through my work at Produced by Chi. They are built for creative studios, production companies, agencies, marketers, and creators. The collection will grow as I develop tools for more creative and business tasks.

Each skill gives an AI agent instructions for a specific job, with supporting references, templates, or scripts where needed. The skills use the `SKILL.md` format for Codex, Claude Code, and other agents that support custom skills.

## Install and update

With Node.js and Git installed, run and choose the skills you want:

```bash
npx skills add producedbychi/skills
```

Add `--skill brand-edge` to select one skill, or `-g` to install across projects.

Update skills installed through the CLI:

```bash
npx skills update
```

The updater lets you choose project or global scope. Back up local customizations first. To install new skills added to this collection, run the install command again.

See the [Skills CLI documentation](https://github.com/vercel-labs/skills) for previewing skills, agent selection, and other options.

## Find a skill for your task

| What you need to do | Skill | What it helps you produce |
| --- | --- | --- |
| Decide who your brand serves and why buyers should choose it | [Brand edge](skills/brand-edge/SKILL.md) | Distinctive positioning and core messaging, with optional workflows for taglines and scoped brand-promise audits. Start with an idea or refine an approved strategy. |
| Turn approved positioning into a campaign idea | [Campaign concept](skills/campaign-concept/SKILL.md) | A creative concept and practical execution brief for the requested ads, video, or landing-page touchpoints. |
| Turn a video idea into a preproduction plan | [Prepro kit](skills/prepro-kit/SKILL.md) | A creative brief, treatment, two-column AV script, shot and resource breakdown, and project paperwork drafts. Start with an idea or request a specific document. |
| Choose a project's visual direction and prepare references for review | [Moodboard builder](skills/moodboard-builder/SKILL.md) | Annotated moodboards and visual-direction decks for client review, with source records and editable PowerPoint and PDF exports. |
| Create or improve a YouTube thumbnail | [YouTube thumbnail generator](skills/youtube-thumbnail-generator/SKILL.md) | A thumbnail image through an available image tool, or a paste-ready prompt package with reference guidance. |
| Design static ads for a product or service | [Ad image generator](skills/ad-image-generator/SKILL.md) | Ad images adapted to your brand, campaign, and placement, with a visual direction and clarity checks. |
| Explain your offer and rewrite confusing marketing copy | [Messaging for dummies](skills/messaging-for-dummies/SKILL.md) | Buyer-relevant messaging that preserves your brand voice, clarifies the offer, and removes generic AI writing patterns. |
| Turn a video brief into an AI video generation prompt | [Seedance video director](skills/seedance-video-director/SKILL.md) | A Seedance 2.0 prompt with camera direction, lighting, continuity, and scene instructions. |

## How to use these AI skills

1. Choose a skill from the table and read its `SKILL.md`.
2. Install it with the command above, or copy the complete folder from `skills/` into your agent's custom-skills directory. Keep its supporting files together.
3. Start a new task and name the skill. Supply your project context, brand assets, source material, and the output you need.

For example, ask "Use prepro-kit to turn this video idea into a creative brief and AV script" or "Use messaging-for-dummies to make this service offer easier for buyers to understand."

Install `prepro-kit` as one folder. Its modes live in `references/`. You can request the full workflow or one document. The skill marks unapproved choices as provisional. Supply approved company details and templates for business documents. Private rates, payment details, and contract terms are not included; legal and tax terms need qualified review.

Image generation and document export depend on the tools available to your agent. A skill supplies guidance, not a subscription or access to a generation model. Review outputs before publishing or sending them to a client. These skills do not guarantee ad conversions or YouTube performance.

## Repository structure

Each skill lives in `skills/<skill-name>/` and contains a required `SKILL.md`. Supporting resources stay inside that folder.

## Adding a skill

Create `skills/<skill-name>/SKILL.md`. Add only the references, templates, assets, or scripts the skill needs. List the new skill in the task table so readers can find it as the collection grows.
