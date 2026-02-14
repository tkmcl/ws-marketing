# BACKLOG.md - Functionality Requests

Requests from Michiel that need Tom's input or implementation.

## Open Items

| Date | Request | Source | Status | Notes |
|------|---------|--------|--------|-------|
| 2026-02-11 | LinkedIn scraping | Michiel (Aker SPE outreach) | ❓ Needs implementation | Can't access LinkedIn search results (requires auth). Need browser relay or manual list from Michiel. |
| 2026-02-14 | Talk to Glu for dashboard examples | Michiel (TenneT mockup) | ❓ Needs implementation | Can't find Glu session. Need to know how to reach Glu (handle, session key, or direct comms). |
| 2026-02-12 | Read PDF attachments from Slack | Michiel (TenneT Portfolio Planning.pdf) | ❓ Needs implementation | Slack file URLs return login page. Need direct download access or workaround. |
| 2026-02-10 | Read Excel attachments from Slack | Michiel (Kuala Lumpur leads) | ❓ Needs implementation | Same issue as PDF — Slack file URLs return login page. |
| 2026-02-14 | Create dashboard mockup image | Michiel (TenneT pitch) | ❓ Needs scoping | Can generate images via OpenAI, but need reference examples. Glu access would help. |

## Context from #ada-marketing

### LinkedIn (Feb 11)
Michiel asked me to draft emails to Aker attendees from an SPE event. He linked a LinkedIn search results page — I cannot access LinkedIn search (requires authentication). **Solution needed:** Either browser relay integration for LinkedIn, or Michiel provides names manually.

### Glu Communication (Feb 14)
Michiel asked me to "talk to Glu" to understand WhiteSpace dashboard design patterns (Heineken, Neptune, CNOOC). Tom mentioned using the @ handle. **Need:** Glu's session key, channel, or a way to reach them.

### PDF/Excel Files (Feb 10, 12)
Slack file URLs (`files.slack.com`) redirect to a login page when I try to fetch them. Michiel has worked around this by pasting content directly. **Solution needed:** Proper Slack file download integration or alternative file sharing method.

## Resolved Items

(None yet)

---

**Process:** When Michiel asks for something I can't do, I add it here and tag @Tom in Slack.
