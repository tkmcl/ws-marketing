# From Data Rich to Decision Ready: A Different Way to Think About AI in Energy

*DRAFT — for review by Michiel before publishing*

---

Here is a number worth sitting with: less than 1 percent.

That is the share of operational data that oil and gas companies actually use to inform decisions — according to McKinsey, which studied sensors across tens of thousands of data points on drilling rigs and found that almost none of it reached the people making choices.[¹](#sources)

This is not a data collection problem. The industry has solved data collection. Upstream operators run facilities instrumented with thousands of sensors. Seismic surveys generate petabytes per campaign. Production systems log readings every second. Digital twins mirror physical assets in near real-time. The data is there.

The problem is what happens — or doesn't happen — next.

---

## The decade we spent getting rich on data

The 2010s were the decade of instrumentation. The energy industry made enormous investments in sensors, historians, cloud infrastructure, and data lakes. It hired data scientists. It built dashboards. It ran pilots.

And many of those pilots worked, technically. The data was captured. The models ran. The outputs were impressive.

But McKinsey found that 70% of oil and gas companies are still stuck in pilot phase despite multi-year investments in digital technologies.[²](#sources) The pilots did not scale. The insights did not reach decisions. The dashboards told engineers what had happened — but did not tell them what to do.

The industry had become data rich. It had not become decision ready.

---

## What "decision ready" actually looks like

Equinor is one of the clearest examples of what happens when the gap closes.

In 2025, Equinor reported USD 130 million in value generated through AI — across predictive maintenance, seismic interpretation, and field development planning.[³](#sources) Since 2020, the cumulative total has exceeded USD 330 million.

The details matter. For Johan Sverdrup Phase 3, AI-driven planning generated thousands of well placement and development alternatives. The result was not a better dashboard — it was a decision: a configuration that human experts had overlooked, which saved the partnership USD 12 million.

That is a different category of outcome. Not "AI surfaced an insight." AI changed what was decided.

The same pattern is visible at ADNOC, which in 2024 deployed its AIQ Advanced Reservoir 360 (AR360) solution across more than 30 reservoirs. The trial phase showed a 70% improvement in accuracy in seismic interpretation and significant advances in anomaly detection.[⁴](#sources) Again, not just faster data processing — better inputs to consequential decisions.

---

## The gap that most AI investments miss

So why does the industry keep building data infrastructure without building decision infrastructure?

Part of the answer is that data and decisions feel like the same problem. They are not.

Data infrastructure asks: *how do we collect, store, and retrieve information?*  
Decision infrastructure asks: *how do we turn that information into a confident choice, made by the right person, at the right time, with the right trade-offs visible?*

These require different thinking. Data infrastructure is largely an engineering challenge. Decision infrastructure is a human one. It demands understanding how specialists actually reason under uncertainty, what slows them down, what they need to trust an output, and how to surface complexity without overwhelming it.

The graveyard of useful-but-unused AI tools in energy is largely filled with systems that solved the data problem but ignored the human one. Systems that were technically correct but practically unusable. Systems that required specialists to change how they worked rather than fitting into how they already worked. Gartner found that at least 50% of generative AI projects were abandoned after proof of concept — and across oil and gas specifically, McKinsey's research shows 70% of digital investments never move beyond pilot.[⁵](#sources)

---

## Two questions that separate AI that informs from AI that decides

When evaluating any AI application in upstream energy, two questions reveal whether it is building decision infrastructure or just adding to the data estate:

**1. Does it change what gets decided — or just what gets reported?**

A predictive maintenance model that fires an alert is informative. A model embedded into a maintenance scheduling workflow — where the recommended action, the trade-offs against production continuity, and the spare parts availability are all visible in one place — changes decisions. The same underlying algorithm. Entirely different operational value.

**2. Will the people who need to use it actually use it?**

This is the question that most pilots skip, and most post-mortems eventually land on. Adoption is not a communications problem. It is a design problem. EY's 2025 research on AI in oil and gas explicitly calls out "the acceptance gap between traditional operations and AI tools" as the last mile that proves most daunting — even after data foundations are in place.[⁶](#sources) Accenture found that 81% of energy executives cite trust as a critical factor in AI adoption, which points squarely to the human and interface layer, not the technical one.[⁷](#sources) Tools built for the specialists who use them — with interfaces that reduce cognitive load rather than increase it, and outputs calibrated to how those specialists already make decisions — get used. Tools built for the engineers who built them frequently do not.

---

## What the next decade requires

The energy sector is entering a new phase of capital discipline. Equinor has cut capex. BP halted buybacks. TotalEnergies halved distributions. The message from every major in the last quarter is consistent: do more with less. Extract more value from existing assets. Make fewer bets, but better ones.

That environment makes the data-to-decision gap expensive in a way it was not before. When capital is abundant, suboptimal decisions are tolerable. When every dollar of investment is scrutinized, the cost of a slow, incomplete, or poorly framed decision compounds.

This is the moment to stop treating data infrastructure and decision infrastructure as the same investment. They are not. One makes you data rich. The other makes you decision ready.

The industry has spent a decade on the first. The next decade belongs to the second.

---

*At WhiteSpace Solutions, we build AI-powered decision platforms for the energy industry. Our tools — AIM (Asset Integrity Management) and AIS (Asset Inventory & Sparing) — are designed to close the gap between operational data and confident decisions, with interfaces built for specialists and outcomes measured in production, cost, and risk.*

---

## Sources {#sources}

1. McKinsey & Company, "Why Oil and Gas Companies Must Act on Analytics" — [mckinsey.com](https://www.mckinsey.com/industries/oil-and-gas/our-insights/why-oil-and-gas-companies-must-act-on-analytics) / CNBC, "Oil firms are swimming in data they don't use" (March 2015) — [cnbc.com](https://www.cnbc.com/2015/03/05/us-energy-industry-collects-a-lot-of-operational-data-but-doesnt-use-it.html)
2. McKinsey 2024 research, cited in: CFlow, "Digital Transformation in Oil and Gas: Complete Guide for 2026" — [cflowapps.com](https://www.cflowapps.com/digital-transformation-in-oil-and-gas/)
3. Equinor, "Artificial Intelligence Saved Equinor USD 130 Million" (January 2026) — [equinor.com](https://www.equinor.com/news/20260107-artificial-intelligence-saved-equinor-usd-130-million) / Globuc summary — [news.globuc.com](https://news.globuc.com/news/ai-equinors-bottom-line/)
4. ADNOC, "ADNOC and AIQ Accelerate Deployment of Industry-First AR360 AI Solution" (2024) — [adnoc.ae](https://www.adnoc.ae/en/news-and-media/press-releases/2024/adnoc-and-aiq-accelerate-deployment-of-industry-first-ar360-ai-solution)
5. Gartner, "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept" (July 2024) — [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025) | Updated finding: at least 50% abandoned by end of 2025 — [gartner.com](https://www.gartner.com/en/articles/genai-project-failure)
6. EY, "Maximizing the Impact of AI in the Oil and Gas Sector" (August 2025) — [ey.com](https://www.ey.com/en_us/insights/oil-gas/maximizing-the-impact-of-ai-in-the-oil-and-gas-sector)
7. Accenture, "Technology Vision 2025: Harnessing AI Transformative Power in the Energy Sector" — [accenture.com](https://www.accenture.com/us-en/blogs/energy/technology-vision-2025-harnessing-ai-transformative-power-energy-sector)
