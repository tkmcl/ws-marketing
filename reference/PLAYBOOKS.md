# Activation Playbooks

When a signal from SIGNALS.md is flagged as 🔴 HIGH, don't just report it — **activate a playbook**.
All outputs are drafts for Michiel to review. Never send anything externally.

For delivery routing, see NOTION.md. General rule:
- **Telegram** = alert + summary
- **Notion** = full deliverable

---

## Playbook 1: Account Outreach

**Trigger:** High-priority signal at a Tier 1 account (new project, capex decision, AI/digital initiative).

**Produce:**
1. **Signal summary** — What happened, why it matters for WhiteSpace (2-3 sentences)
2. **Outreach email draft** — Personalized to a relevant contact at the account. Reference the specific event. Connect to a WhiteSpace capability. Under 150 words, warm but not salesy.
3. **LinkedIn message variant** — Shorter, more casual version (2-3 sentences)
4. **Suggested follow-up angle** — What Michiel could reference in a call or meeting

**Tone:** Use the Narrative Summary in BRAND.md for framing. Consultative, specific, never generic. Reference the exact signal.

**Deliver:**
- **Notion** → Marketing Intel entry. Type: `Account Brief`. Include all 4 elements.
- **Telegram** → Short alert: what the signal is, that outreach drafts are ready in Notion.

---

## Playbook 2: Content Activation

**Trigger:** Emerging industry trend (multiple sources), competitor positioning shift, or noteworthy event that's content-worthy.

**Produce:**
1. **Content angle** — What's the hook? Why should WhiteSpace's audience care? (2-3 sentences)
2. **LinkedIn post draft** — Follow BRAND.md and LINKEDIN-EXAMPLES.md. 150-300 words. Provide 2 variants when the angle allows it.
3. **Hashtag suggestions** — 3-5 relevant hashtags
4. **Optional: blog outline** — If the theme is rich enough, suggest 3-4 section headers for a longer piece

**Tone:** Use the Narrative Summary in BRAND.md — especially the pillars and taglines. Thought leadership. Confident, insight-led, not reactive. Pattern: recognition → surprise → positive action.

**Deliver:**
- **Notion** → Marketing Intel entry. Type: `Content Draft`. Include drafts + angle.
- **Telegram** → The strongest LinkedIn draft variant for quick review. Link to Notion for the rest.

---

## Playbook 3: Sales Enablement

**Trigger:** Leadership change at a Tier 1 account, hiring surge in digital/planning roles, or Michiel has an upcoming meeting with a target account.

**Produce:**
1. **Account brief** — Company snapshot, recent signals, strategic priorities, relevant WhiteSpace fit (half-page max)
2. **New stakeholder profile** — If leadership change: who they are, background, likely priorities
3. **Talking points** — 3-5 specific points tied to recent signals
4. **Suggested proof point** — Which WhiteSpace story is most relevant right now?
5. **Intro message draft** — If new contact: congratulatory or intro message referencing their role

**Tone:** Briefing-style. Concise, factual, actionable. Scannable in 2 minutes.

**Deliver:**
- **Notion** → Marketing Intel entry. Type: `Account Brief`. Full brief with all elements.
- **Telegram** → Alert: who changed roles, one-line "so what", link to full brief in Notion.

---

## Playbook 4: Competitive Response

**Trigger:** Direct competitor (Palantir, Cognite, AVEVA) launches a product, announces a partnership, wins a deal, or shifts positioning.

**Produce:**
1. **What happened** — Factual summary (3-4 sentences)
2. **Positioning analysis** — How does this affect WhiteSpace's differentiation?
3. **Counter-narrative** — 2-3 messaging angles. Focus on genuine differentiation, not FUD.
4. **Suggested action** — Should Michiel respond? (LinkedIn post, outreach to at-risk accounts, internal briefing)

**Tone:** Analytical, not defensive. Confident in WhiteSpace's position. Never badmouth — differentiate on substance.

**Deliver:**
- **Notion** → Marketing Intel entry. Type: `Competitive Analysis`. Full analysis.
- **Telegram** → Alert: what the competitor did, top-line implication, link to Notion.

---

## Playbook 5: Weekly Pattern Report

**Trigger:** Friday weekly roundup (cron job).

**Produce:**
1. **Top signals of the week** — 3-5 most important, with signal type and account
2. **Patterns** — Multiple signals pointing the same direction? (e.g., "3 Tier 1 accounts announced digital initiatives")
3. **Competitor summary** — Notable moves this week
4. **Content opportunities** — Themes worth writing about
5. **Recommended focus for next week** — Where should Michiel's attention go?
6. **Activations delivered** — What playbooks were triggered and what was produced

**Deliver:**
- **Notion** → Marketing Intel entry. Type: `Weekly Roundup`. Full report.
- **Telegram** → Scannable summary: top 3 signals, one pattern, one recommendation. Link to Notion for the full version.

---

## When NOT to Activate

- 🟡 MEDIUM and 🟢 LOW signals go in the daily briefing only — no playbook
- Don't activate on stale signals (>7 days old) unless part of a developing pattern
- If unsure, include in the briefing and ask: "Want me to dig into this?"
