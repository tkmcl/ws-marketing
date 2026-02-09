import os
import json
import urllib.request

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
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            return json.loads(res_body)["id"]
    except Exception as e:
        print(f"Error creating page {title}: {e}")
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))
        return None

def get_h1(text):
    return { "object": "block", "type": "heading_1", "heading_1": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

def get_h2(text):
    return { "object": "block", "type": "heading_2", "heading_2": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

def get_p(text):
    return { "object": "block", "type": "paragraph", "paragraph": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

def get_bullet(text):
    return { "object": "block", "type": "bulleted_list_item", "bulleted_list_item": { "rich_text": [{ "type": "text", "text": { "content": text } }] } }

# Define blocks for all 15 accounts... (Batch 1: Equinor, Harbour, Conoco, Petoro, PDO)
# ... scripts will follow in chunks ...
equinor_blocks = [get_h1("Equinor 2026 Deep Dive"), get_h2("1. Executive Summary"), get_p("In 2026, Equinor stands as the archetypal 'Transition Major,' navigating the friction between its legacy as Europe’s energy security guarantor and its ambition to be a global renewables powerhouse. Having weathered the initial volatility of the mid-2020s, Equinor is aggressively high-grading its portfolio, slashing capital expenditure in power and low-carbon solutions by $4 billion (spread over 2026-27) to protect returns. The firm is an integrated energy system orchestrator, leveraging cash flows from the NCS to fund its shift into offshore wind and CCS. 2026 is the year of 'Digital Maturation,' where prototypes move from experimental to mission-critical infrastructure."), get_h2("2. Market Positioning"), get_p("Equinor is reacting to the projected 2026 supply surplus with a 'Defensive Alpha' strategy. While global peers may struggle with high-cost barrels, Equinor’s low-cost NCS production (averaging ~$40/boe breakeven) provides a massive buffer. It has announced a 10% reduction in operating costs for 2026, achieved through portfolio high-grading and deep automation."), get_h2("3. Financial Frame"), get_bullet("Capex: Projected at $13 billion for 2026."), get_bullet("Dividends: Predictable Progressive Dividends maintained."), get_h2("4. Operational Roadmap"), get_bullet("Rosebank (UK): Start-up 2026/27."), get_bullet("Northern Lights (Norway): Commercial scaling 2026."), get_h2("5. Digital & AI Maturity"), get_p("Proprietary Echo system and Omnia platform with partners Kongsberg and SLB."), get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Unmanned Operating Model Overlay.")]
harbour_blocks = [get_h1("Harbour Energy 2026 Deep Dive"), get_h2("1. Executive Summary"), get_p("2026 is Harbour's first 'steady state' year after the Wintershall Dea integration. Diversified production stable at 435-455 kboepd."), get_h2("2. Market Positioning"), get_p("Resilient Independent branding. Costs at $13.5/boe."), get_h2("3. Financial Frame"), get_bullet("Capex: $1.7-1.9B for 2026."), get_h2("4. Operational Roadmap"), get_bullet("Zama: Operatorship transition."), get_bullet("Greensand: First injection 2026."), get_h2("5. Digital & AI Maturity"), get_p("Focused on 'Unified Asset Visibility' after acquisitions."), get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Merged Asset Optimization.")]
conocophillips_blocks = [get_h1("ConocoPhillips 2026 Deep Dive"), get_h2("1. Executive Summary"), get_p("Full operational integration of Marathon Oil assets. Premier Lower 48 player targeting $1B cost improvement."), get_h2("2. Market Positioning"), get_p("Disciplined Scale. Balancing Permian with global LNG."), get_h2("3. Financial Frame"), get_bullet("Capex: $12B (preliminary)."), get_bullet("Synergies: >$1B run-rate."), get_h2("4. Operational Roadmap"), get_bullet("Willow: Moving toward first oil."), get_bullet("North Field East: Startup 2H 2026."), get_h2("5. Digital & AI Maturity"), get_p("GWDW cloud expansion into Marathon assets."), get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: AI-driven cost-cutting mandate support.")]

page_ids = {}
page_ids["Equinor"] = create_page("Equinor 2026 Deep Dive", "Equinor", equinor_blocks)
page_ids["Harbour"] = create_page("Harbour Energy 2026 Deep Dive", "Harbour Energy", harbour_blocks)
page_ids["Conoco"] = create_page("ConocoPhilips 2026 Deep Dive", "ConocoPhilips", conocophillips_blocks)

print(f"PAGE_IDS_BATCH1: {json.dumps(page_ids)}")
