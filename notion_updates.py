import os
import json
import requests

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = "2fe1cf93fe62804789a7f53a1887db80"

def create_page(title, account, content_blocks):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Title": { "title": [{ "text": { "content": title } }] },
            "Account": { "select": { "name": account } },
            "Type": { "select": { "name": "Account Brief" } },
            "Status": { "status": { "name": "Done" } },
            "Date": { "date": { "start": "2026-02-09" } }
        },
        "children": content_blocks
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error creating page: {response.status_code}")
        print(response.text)
        return None
    return response.json()["id"]

def get_h1(text):
    return { "object": "block", "type": "heading_1", "heading_1": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

def get_h2(text):
    return { "object": "block", "type": "heading_2", "heading_2": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

def get_p(text):
    return { "object": "block", "type": "paragraph", "paragraph": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

def get_bullet(text):
    return { "object": "block", "type": "bulleted_list_item", "bulleted_list_item": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

# EQUINOR
equinor_blocks = [
    get_h1("EXECUTIVE STRATEGY BRIEF: Equinor 2026 Deep Dive"),
    get_h2("1. Executive Summary: The 2026 State of the Union"),
    get_p("In 2026, Equinor stands as the archetypal 'Transition Major,' navigating the friction between its legacy as Europe’s energy security guarantor and its ambition to be a global renewables powerhouse. Having weathered the initial volatility of the mid-2020s, Equinor is aggressively high-grading its portfolio, slashing capital expenditure in power and low-carbon solutions by $4 billion (spread over 2026-27) to protect returns. The firm is an integrated energy system orchestrator, leveraging cash flows from the NCS to fund its shift into offshore wind and CCS. 2026 is the year of 'Digital Maturation,' where prototypes move from experimental to mission-critical infrastructure."),
    get_h2("2. Market Positioning: Reacting to the 2026 Supply Surplus"),
    get_p("Equinor is reacting to the projected 2026 supply surplus with a 'Defensive Alpha' strategy. While global peers may struggle with high-cost barrels, Equinor’s low-cost NCS production (averaging ~$40/boe breakeven) provides a massive buffer. It has announced a 10% reduction in operating costs for 2026, achieved through portfolio high-grading and deep automation. It remains committed to natural gas as the 'Bridge of 2026,' maximizing exports to Europe through pipelines to offset potential oil revenue dips."),
    get_h2("3. Financial Frame: Capex, Dividends, and Cost-Cutting"),
    get_bullet("Capex Envelope: Projected at $13 billion for 2026, a reduction from previous peaks. Focus is now on organic project delivery."),
    get_bullet("Dividend Strategy: Maintaining 'Predictable Progressive Dividends' and tactical share buybacks, while protecting the $23 billion renewable investment target."),
    get_bullet("Cost-Cutting Mandate: 10% reduction in operating costs for 2026, focusing on exits from high-cost geographies and centralizing offshore operations."),
    get_h2("4. Operational Roadmap: 2026 FIDs and First Oil"),
    get_bullet("Rosebank (UK): Phase 1 start-up targeted for 2026/2027. Critical project featuring an electrified FPSO."),
    get_bullet("Northern Lights (Norway): Commercial operations scaling up, aiming for 1.5 million tonnes of CO2 storage per year."),
    get_bullet("Barents Sea: FIDs on Johan Castberg satellite tie-backs to maintain platform throughput."),
    get_h2("5. Digital & AI Maturity: Partners and Initiatives"),
    get_p("Proprietary Echo system and Omnia data platform are mission-critical. Key partners include Kongsberg, SLB, and SparkBeyond. 2026 moves from 'visualization' to 'autonomous intervention.'"),
    get_h2("6. WhiteSpace Action Plan: Entry Angles"),
    get_bullet("Angle: Unmanned Operating Model Overlay. Position for remote oversight of unmanned facilities."),
    get_bullet("Angle: Electrification Efficiency. precise power load-balancing AI for Rosebank."),
    get_bullet("Angle: CCS Lifecycle Management. Tracking and verification for Northern Lights.")
]

# HARBOUR
harbour_blocks = [
    get_h1("EXECUTIVE STRATEGY BRIEF: Harbour Energy 2026 Deep Dive"),
    get_h2("1. Executive Summary"),
    get_p("2026 is Harbour's first 'steady state' year after the massive Wintershall Dea integration. It has successfully diversified away from the UK North Sea, with production stable at 435-455 kboepd. The focus is now on debt deleveraging and high-margin international growth."),
    get_h2("2. Market Positioning"),
    get_p("Harbour is positioned as a 'Resilient Independent.' With production costs at $13.5/boe, it remains profitable even in lower price environments. It uses its international footprints (Norway, Argentina, Mexico) to mitigate UK political and fiscal risks."),
    get_h2("3. Financial Frame"),
    get_bullet("Capex: Projected at $1.7-1.9 billion for 2026. Prioritizing capital efficiency over volume expansion."),
    get_bullet("Cash Flow: Estimated FCF of $600M at current prices. Focus on debt reduction following the Wintershall deal."),
    get_h2("4. Operational Roadmap"),
    get_bullet("Zama (Mexico): Transition of operatorship and execution of phased development plan."),
    get_bullet("Viking CCS: Progressing toward FID with partners (BP)."),
    get_bullet("Greensand (Denmark): Targeted first injection of 400k tonnes/year in 2026."),
    get_h2("5. Digital & AI Maturity"),
    get_p("Integration of legacy Wintershall digital twins into Harbour's lean operating model. Focused on 'Unified Asset Visibility' across the new global portfolio."),
    get_h2("6. WhiteSpace Action Plan"),
    get_bullet("Angle: Merged Asset Optimization. Integrating disparate data from the acquisition into a single AI-driven dashboard."),
    get_bullet("Angle: Regulatory Compliance Automation. Managing complex ESG reporting across varied jurisdictions."),
    get_bullet("Angle: Phased Development Analytics. Optimizing the Zama capital rollout.")
]

# CONOCOPHILLIPS
conocophillips_blocks = [
    get_h1("EXECUTIVE STRATEGY BRIEF: ConocoPhillips 2026 Deep Dive"),
    get_h2("1. Executive Summary"),
    get_p("2026 marks the full operational integration of Marathon Oil assets. ConocoPhillips is the premier Lower 48 player, combining scale with capital discipline. It is targeting a $1 billion cost/capex improvement this year."),
    get_h2("2. Market Positioning"),
    get_p("Reaction to surplus is 'Disciplined Scale.' Unlike pure-play shale, Conoco uses its global LNG and Alaska assets to balance Permian volatility. It expects flat to modest growth to protect margins."),
    get_h2("3. Financial Frame"),
    get_bullet("Capex: Preliminary 2026 framework at $12B, down from $17B midpoint in 2025."),
    get_bullet("Efficiency: $1B combined improvement in capex and opex targeted for 2026."),
    get_bullet("Dispositions: On track for $5B target by year-end 2026."),
    get_h2("4. Operational Roadmap"),
    get_bullet("Willow (Alaska): Moving from peak construction toward first oil. Capex beginning to taper off."),
    get_bullet("North Field East (Qatar): First production expected 2H 2026, boosting LNG cash flow."),
    get_bullet("Marathon Integration: Realizing >$1B in run-rate synergies."),
    get_h2("5. Digital & AI Maturity"),
    get_p("Scaling AI models from the Conoco 'GWDW' (Global Web Data Warehouse) to the new Marathon assets. Focus on predictive drilling and autonomous fracking."),
    get_h2("6. WhiteSpace Action Plan"),
    get_bullet("Angle: The $1B Synergy Gap. Mapping our tools to the specific 'automation' portion of their cost-cutting mandate."),
    get_bullet("Angle: Alaska Remote Ops. Digital tools for the unique logistical challenges of Willow."),
    get_bullet("Angle: LNG Feedstock Optimization. Linking upstream production to Qatar-bound exports.")
]

page_ids = {}
page_ids["Equinor"] = create_page("Equinor 2026 Deep Dive", "Equinor", equinor_blocks)
page_ids["Harbour"] = create_page("Harbour Energy 2026 Deep Dive", "Harbour Energy", harbour_blocks)
page_ids["Conoco"] = create_page("ConocoPhillips 2026 Deep Dive", "ConocoPhilips", conocophillips_blocks)

print(f"PAGE_IDS: {json.dumps(page_ids)}")
