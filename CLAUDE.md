# CLAUDE.md

## What This Is
This is an OpenClaw agent workspace for "ws-marketing" — a marketing intelligence bot for WhiteSpace Solutions. The primary user is Michiel (CCO), who interacts via Telegram.

## Workspace Structure
- Root `.md` files (SOUL.md, AGENTS.md, USER.md, IDENTITY.md) are auto-loaded by OpenClaw
- `reference/` — reference docs the agent reads (ACCOUNTS.md, BRAND.md, etc.)
- `memory/` — agent writes daily logs here
- `drafts/` — content drafts

## OpenClaw Config
- Main config: ~/.openclaw/openclaw.json
- Agent state: ~/.openclaw/agents/ws-marketing/agent/
- This agent runs on Gemini 3 Flash via OpenRouter
- Paired to a Telegram bot for Michiel

## What We're Building (v0.1)
1. Daily morning news scan (energy industry, target accounts, competitors)
2. On-demand marketing help via Telegram (drafts, research, competitive intel)
3. Weekly roundup on Fridays

## Key Context
- WhiteSpace Solutions = AI-powered decision intelligence for energy sector
- Brand voice: "Radically human AI", confident but not arrogant, energy sector native
- The agent must NEVER send anything externally — all outputs are drafts