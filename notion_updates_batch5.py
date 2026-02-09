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

# PERENCO
perenco_blocks = [
    get_h1("Perenco 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("Perenco in 2026 is the 'Secondary Recovery Specialist.' Operating as a private entity, it continues to buy mature assets and extend their life via gas-to-power and LNG."),
    get_h2("2. Market Positioning"), get_p("The Independent Lifecycle Manager. Counter-cyclical growth—buying what the majors divest during the 2026 surplus."),
    get_h2("3. Financial Frame"), get_bullet("Capex: ~$2B for the Cap Lopez LNG project in Gabon. Privately funded and debt-conscious."),
    get_h2("4. Operational Roadmap"), get_bullet("Cap Lopez (Gabon): Reaching steady state for gas export. 150+ decarbonization projects underway globally."),
    get_h2("5. Digital & AI Maturity"), get_p("Focus on edge-automation for mature wells. Partnering with technology EPCs to automate venting reduction."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Mature Asset Digitization. AI to detect sub-optimal flow in 20-30 year old wells.")
]

# PETROBRAS
petrobras_blocks = [
    get_h1("Petrobras 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("Petrobras 2026 is executing the first year of its 2026-2030 Strategic Plan, with US$109B in total capex. The Pre-Salt remains the global standard for offshore efficiency."),
    get_h2("2. Market Positioning"), get_p("The Pre-Salt Alpha. Reacting to surplus by maintaining high dividends while spending US$91B on implementation portfolio assets."),
    get_h2("3. Financial Frame"), get_bullet("Capex: US$109B over 5 years. Focus on 11 FPSOs in Búzios field."),
    get_h2("4. Operational Roadmap"), get_bullet("Búzios Field: Major FPSO deployments. Pelotas and Potiguar exploration focus."),
    get_h2("5. Digital & AI Maturity"), get_p("Deep internal tech center (CENPES) partnering with ABS and Halliburton for FPSO digital twins."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Pre-Salt Digital Twin Optimization. Scaling specialized FPSO AI to increase production by the target 1%.")
]

# ECOPETROL
ecopetrol_blocks = [
    get_h1("Ecopetrol 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("In 2026, Ecopetrol is the 'Integrated Energy Powerhouse' of South America, successfully blending oil/gas with power transmission (ISA)."),
    get_h2("2. Market Positioning"), get_p("Energy Transition Pioneer. Spending 30% of capex on low-carbon but maintaining 730k boed production."),
    get_h2("3. Financial Frame"), get_bullet("Capex: COP 22-27 Trillion in 2026. Budgeted at a conservative $60 Brent."),
    get_h2("4. Operational Roadmap"), get_bullet("Gas development (Offshore Colombia): Critical focus on domestic supply. ISA transmission projects."),
    get_h2("5. Digital & AI Maturity"), get_p("Integrating upstream data with ISA's grid management systems for 'Energy Flow' optimization."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: The Integrated Data Bridge. AI for synchronizing upstream gas production with power grid demand.")
]

ids = {}
ids["Perenco"] = create_page("Perenco 2026 Deep Dive", "Perenco", perenco_blocks)
ids["Petrobras"] = create_page("Petrobras 2026 Deep Dive", "Petrobras", petrobras_blocks)
ids["Ecopetrol"] = create_page("Ecopetrol 2026 Deep Dive", "Ecopetrol S.A.", ecopetrol_blocks)
print(f"PAGE_IDS_BATCH5: {json.dumps(ids)}")
