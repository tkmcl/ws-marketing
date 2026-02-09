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
        print(f"Error {title}: {e}")
        return None

def get_h1(t): return { "object": "block", "type": "heading_1", "heading_1": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }
def get_h2(t): return { "object": "block", "type": "heading_2", "heading_2": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }
def get_p(t): return { "object": "block", "type": "paragraph", "paragraph": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }
def get_bullet(t): return { "object": "block", "type": "bulleted_list_item", "bulleted_list_item": { "rich_text": [{ "type": "text", "text": { "content": t } }] } }

# PETORO
petoro_blocks = [
    get_h1("Petoro 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("In 2026, Petoro remains the silent guardian of Norway's State's Direct Financial Interest (SDFI). Its 2026 focus is on 'Asset Longevity' and ensuring Equinor and other partners maintain high operational standards on the NCS."),
    get_h2("2. Market Positioning"), get_p("Counter-cyclical value guardian. Reacting to surplus by pushing partners for lower breakevens and higher gas volumes to Europe."),
    get_h2("3. Financial Frame"), get_bullet("Capex: Petoro is a non-operator but coordinates massive SDFI investments (billions). Focus is on 'Lean & Mean' partner operations."),
    get_h2("4. Operational Roadmap"), get_bullet("SDFI Portfolio: Monitoring value from the start-up of two new fields in 2025/26."),
    get_h2("5. Digital & AI Maturity"), get_p("Data consumer role—ingesting digital twin data from Equinor (Echo) and Aker BP to verify resource estimates."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Independent Value Verification. Offering Petoro and the Norwegian government AI-driven third-party audits of operator efficiency.")
]

# PDO
pdo_blocks = [
    get_h1("PDO 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("PDO is the engine of Oman's Vision 2040. In 2026, it is halfway through the 'Oman AI & Digital Future Program (2024-2026),' moving from pilot to enterprise scale."),
    get_h2("2. Market Positioning"), get_p("Low-cost producer focusing on EOR (Enhanced Oil Recovery) to maintain production targets of ~600k bpd."),
    get_h2("3. Financial Frame"), get_bullet("Capex: Tied to the 11th Five-Year Plan. Significant spend on water-flooding and steam-injection tech."),
    get_h2("4. Operational Roadmap"), get_bullet("Yibal Khuff: Ramping up complex multi-product delivery. Focus on PPP (Public-Private Partnership) projects in 2026."),
    get_h2("5. Digital & AI Maturity"), get_p("Advanced Roadmap: Leading digital transformation in Oman, leveraging AI for production forecasting and reservoir modeling."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: EOR Optimization. AI tools to maximize recovery while minimizing steam/water energy intensive cycles.")
]

# SHELL
shell_blocks = [
    get_h1("Shell 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("In 2026, Shell is a leaner, dividend-focused entity under its 'Value over Volume' mandate. It has cut deeper into renewables to double down on integrated gas and high-return upstream."),
    get_h2("2. Market Positioning"), get_p("Reaction to surplus: Shell is playing the 'Gas Arbitrage' game, using its massive LNG fleet to move molecules where prices are highest while slowing down speculative oil exploration."),
    get_h2("3. Financial Frame"), get_bullet("Divestments: Sustained asset sales to fund $60B+ annual capex (including AI/infra)."),
    get_h2("4. Operational Roadmap"), get_bullet("Vito/Whale (US GOM): Full production ramp-up. Rosebank (UK) interest via Adura JV."),
    get_h2("5. Digital & AI Maturity"), get_p("Palantir Foundry is the 'Operating System.' Integration of 'Agentic AI Hives' for supply chain in 2026."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: The Palantir 'Edge.' Offering tools that plug into the Foundry ecosystem for niche asset-level performance.")
]

ids = {}
ids["Petoro"] = create_page("Petoro 2026 Deep Dive", "Petoro", petoro_blocks)
ids["PDO"] = create_page("PDO 2026 Deep Dive", "Petroleum Development Oman", pdo_blocks)
ids["Shell"] = create_page("Shell 2026 Deep Dive", "Shell", shell_blocks)
print(f"PAGE_IDS_BATCH2: {json.dumps(ids)}")
