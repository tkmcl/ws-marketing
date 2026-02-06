# Notion Integration

Ada writes structured marketing outputs to private Notion databases.

## Authentication

Use the environment variable `$NOTION_API_KEY` for API calls:

```bash
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{ ... }'
```

## Databases

| Name | Database ID | Purpose |
|---|---|---|
| Marketing Intel | `2fe1cf93fe62804789a7f53a1887db80` | Account briefs, competitive analyses, content drafts, weekly roundups |

### Marketing Intel — Properties

| Property | Type | Values |
|---|---|---|
| Title | title | Descriptive headline for the entry |
| Type | select | `Account Brief`, `Competitive Analysis`, `Content Draft`, `Weekly Roundup` |
| Account | select | `Equinor`, `Shell`, `TotalEnergies`, `BP`, `Palantir`, `Cognite`, `AVEVA`, or other |
| Signal type | select | `New Project`, `Capex/Budget`, `Leadership Change`, `Digital/AI`, `Competitor Move`, `Energy Transition`, `M&A` |
| Status | status | `Not started` (To-do) · `In progress` (In progress) · `Done` (Complete) |
| Date | date | Date the entry was created |

## What Goes Where

| Output | Destination | Why |
|---|---|---|
| Daily briefing, quick alerts | **Telegram only** | Ephemeral, conversational |
| Account briefs, competitive analyses | **Notion** (+ Telegram summary) | Structured, searchable, reusable |
| Content drafts (LinkedIn, blog) | **Notion** (+ Telegram preview) | Easy to review, edit, and track |
| Weekly roundups | **Notion** (+ Telegram summary) | Full version persists, summary is scannable |

## Rules

- All Notion entries are internal drafts. Nothing public.
- When writing to Notion, always send a short Telegram summary linking to the entry.
- Status defaults to `Not started` on creation. Michiel updates it manually.
