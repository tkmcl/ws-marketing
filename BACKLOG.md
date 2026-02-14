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
| 2026-02-14 | Canva integration | Michiel (brochure request) | ❓ Needs scoping | Would enable one-click brochures, LinkedIn carousels, event one-pagers. Canva has Connect API (enterprise) or browser automation option. |

## Context from #ada-marketing

### LinkedIn (Feb 11)
Michiel asked me to draft emails to Aker attendees from an SPE event. He linked a LinkedIn search results page — I cannot access LinkedIn search (requires authentication). **Solution needed:** Either browser relay integration for LinkedIn, or Michiel provides names manually.

### Glu Communication (Feb 14)
Michiel asked me to "talk to Glu" to understand WhiteSpace dashboard design patterns (Heineken, Neptune, CNOOC). Tom mentioned using the @ handle. **Need:** Glu's session key, channel, or a way to reach them.

### PDF/Excel Files (Feb 10, 12)
Slack file URLs (`files.slack.com`) redirect to a login page when I try to fetch them. Michiel has worked around this by pasting content directly. **Solution needed:** Proper Slack file download integration or alternative file sharing method.

## Action Plans

### Canva Integration (Added: 2026-02-14)
**Goal:** Enable Ada to create brochures, LinkedIn carousels, and event one-pagers directly.

**Option A: Browser Automation (Fastest to Test)**
- Use OpenClaw's browser tool to control Canva in a logged-in session
- Steps: Tom sets up browser relay → Ada navigates template → populates text/images → exports PDF
- Pros: No API keys, uses existing capability
- Cons: Brittle if Canva UI changes, needs manual login refresh
- Effort: ~2-4 hours to test

**Option B: Canva Connect API (Robust, Longer Setup)**
- Use Canva's official API to create/edit designs programmatically
- Steps: Register app at canva.com/developers → OAuth credentials → build skill → Ada calls with structured content
- Pros: Stable, proper integration
- Cons: Requires Canva Pro/Teams with API access, dev time
- Effort: ~1-2 days

**Option C: Hybrid (Current Workaround)**
- Ada outputs structured "design brief" JSON, human pastes into Canva template (~5 min)
- Pros: Works today, zero dev time
- Cons: Still requires human step

**Recommendation:** Use Option C now, evaluate Option A (browser automation) as quick-win automation.

**Next step:** Tom to set up logged-in browser relay session for testing when ready.

---

## Resolved Items

(None yet)

---

**Process:** When Michiel asks for something I can't do, I add it here and tag @Tom in Slack.
