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
            "Status": { "status": { "name": "Done" } }
        },
        "children": content_blocks
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))["id"]

def get_h1(t): return { "object": "block", "type": "heading_1", "heading_1": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }
def get_h2(t): return { "object": "block", "type": "heading_2", "heading_2": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }
def get_p(t): return { "object": "block", "type": "paragraph", "paragraph": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }
def get_bullet(t): return { "object": "block", "type": "bulleted_list_item", "bulleted_list_item": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }

# TOTALENERGIES
total_blocks = [
    get_h1("TotalEnergies 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("In 2026, TotalEnergies is the 'Growth Outlier.' While others cut, Total is growing oil and gas production by over 3% annually, backed by high-margin projects in Brazil and US GOM."),
    get_h2("2. Market Positioning"), get_p("Aggressive High-Margin Acquisition. Reacting to surplus by focusing only on 'accretive' barrels with low breakevens."),
    get_h2("3. Financial Frame"), get_bullet("Cost Savings: $7.5B targeted for 2026-2030 across Capex and Opex."),
    get_h2("4. Operational Roadmap"), get_bullet("Brazil & US GOM: Start-ups of key offshore assets. Qatar NFE expansion."),
    get_h2("5. Digital & AI Maturity"), get_p("Deep partnership with SLB for digital solution deployment at scale."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: The $7.5B Efficiency Layer. AI for energy consumption reduction and fixed cost optimization.")
]

# EXXONMOBIL
exxon_blocks = [
    get_h1("ExxonMobil 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("2026 is the year of 'Synergy Capture' for ExxonMobil following the Pioneer deal. It is becoming the world's first truly autonomous industrial enterprise at scale."),
    get_h2("2. Market Positioning"), get_p("Dominance through Technology. Permian is 2026's data center of oil, driving costs down to stay competitive at $40 Brent."),
    get_h2("3. Financial Frame"), get_bullet("Capex: $27-$29B in 2026. Synergies with Pioneer raised to >$3B annually."),
    get_h2("4. Operational Roadmap"), get_bullet("Guyana: Whipping production higher with Payara and beyond. Pioneer transition in Permian."),
    get_h2("5. Digital & AI Maturity"), get_p("Closed-loop automation and AI agents downhole. Pioneering CCS-enabled data centers."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Autonomous Ops Integration. Support their goal of fully autonomous industrial workflows.")
]

# ENI
eni_blocks = [
    get_h1("Eni 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("Eni in 2026 is the 'Satellite Model' pioneer. It has spun off sectors (Plenitude, Enilive) to focus upstream on fast-track developments and low-carbon tech."),
    get_h2("2. Market Positioning"), get_p("Fast-Track Specialist. Reacting to surplus by getting projects from discovery to first oil faster than any peer."),
    get_h2("3. Financial Frame"), get_bullet("EBIT: Targeting positive EBIT for renewable ventures by 2026. Neptune Energy synergies hitting run-rate."),
    get_h2("4. Operational Roadmap"), get_bullet("Baleine (Ivory Coast): Scaling up as a flagship net-zero development."),
    get_h2("5. Digital & AI Maturity"), get_p("Heavy focus on HPC6 (High Performance Computing) for seismic and digital twins."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Fast-Track Lifecycle Management. AI to accelerate engineering phases of 'satellite' developments.")
]

ids = {}
ids["Total"] = create_page("TotalEnergies 2026 Deep Dive", "TotalEnergies", total_blocks)
ids["Exxon"] = create_page("ExxonMobil 2026 Deep Dive", "ExxonMobil", exxon_blocks)
ids["Eni"] = create_page("Eni 2026 Deep Dive", "Eni S.P.A.", eni_blocks)
print(f"PAGE_IDS_BATCH3: {json.dumps(ids)}")
