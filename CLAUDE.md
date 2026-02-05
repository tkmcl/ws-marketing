# CLAUDE.md

## What This Is
This is an OpenClaw agent workspace for "ws-marketing" — a marketing intelligence bot for WhiteSpace Solutions. The primary user is Michiel (CCO), who interacts via Telegram.

## Workspace Structure
- Root `.md` files (SOUL.md, AGENTS.md, USER.md, IDENTITY.md) are auto-loaded by OpenClaw
- `reference/` — reference docs the agent reads:
  - ACCOUNTS.md — target accounts, competitors, industry sources
  - BRAND.md — voice, positioning, messaging guidelines
  - SIGNALS.md — signal taxonomy with classification and relevance scoring
  - PLAYBOOKS.md — trigger-to-action workflows for high-priority signals
  - NOTION.md — Notion integration setup, database schema, delivery routing
  - LINKEDIN-EXAMPLES.md — tone and structure calibration for LinkedIn posts
  - CRON.md — cron job management commands
- `memory/` — agent writes daily logs here
- `user-docs/` — source documents (not committed)

## OpenClaw Config
- Main config: ~/.openclaw/openclaw.json
- Agent state: ~/.openclaw/agents/ws-marketing/agent/
- Secrets (API keys): ~/.openclaw/.env
- This agent runs on Gemini 3 Flash via OpenRouter
- Paired to a Telegram bot for Michiel

## Architecture
Three-layer marketing automation system (see PDF reference doc for full vision):
1. **Data Foundation** — signal detection, classification, and scoring (SIGNALS.md)
2. **Activation Layer** — trigger-based playbooks that turn signals into drafts (PLAYBOOKS.md)
3. **AI CMO** — performance tracking and optimization (future)

## Integrations
- **Telegram** — primary chat interface + daily briefings and alerts
- **Notion** — structured output storage (account briefs, content drafts, competitive analyses, weekly roundups). See reference/NOTION.md for schema and routing rules.

## What We're Building (v0.1)
1. Daily morning news scan with signal classification (energy industry, target accounts, competitors)
2. Playbook activation for high-priority signals (outreach drafts, content, competitive response)
3. On-demand marketing help via Telegram (drafts, research, competitive intel)
4. Weekly roundup on Fridays

## Key Context
- WhiteSpace Solutions = AI-powered decision intelligence for energy sector
- Brand voice: "Radically human AI", confident but not arrogant, energy sector native
- The agent must NEVER send anything externally — all outputs are drafts
