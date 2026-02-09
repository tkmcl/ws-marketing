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

# BP
bp_blocks = [
    get_h1("BP 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("In 2026, BP is undergoing a 'Strategic Reset' under Murray Auchincloss. The company is pivoting back to oil and gas returns while high-grading its low-carbon portfolio."),
    get_h2("2. Market Positioning"), get_p("Pragmatic Energy Producer. Reacting to surplus by focusing on uncompetitive exploration projects."),
    get_h2("3. Financial Frame"), get_bullet("Capex Discipline: Managing funding costs and asset owner pressure to maintain yields."),
    get_h2("4. Operational Roadmap"), get_bullet("Gulf of Mexico: Advancing high-margin tieback projects. West Nile Delta gas ramp-up."),
    get_h2("5. Digital & AI Maturity"), get_p("Scaling digital twins across core operating hubs with Microsoft partner focus."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Performance Improvement Overlay. Tools that validate 'Reset' efficiencies for shareholders.")
]

# CHEVRON
chevron_blocks = [
    get_h1("Chevron 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("2026 is the 'Full Hess' year for Chevron. It is now a leader in Guyana and has shifted major capex back to the US Core."),
    get_h2("2. Market Positioning"), get_p("Capital Disciplined Giant. Budgeting for Brent in the $60s while maintaining 10% volume growth."),
    get_h2("3. Financial Frame"), get_bullet("Capex: $18-$19B in 2026. $10.5B focused on US Permian/DJ basins."),
    get_h2("4. Operational Roadmap"), get_bullet("Guyana: Peak development activity with Hess assets. TCO Project (Kazakhstan) steady state."),
    get_h2("5. Digital & AI Maturity"), get_p("Expanding 'Factory Model' digital tools from Permian to international deepwater."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Cross-Regional Factory Model. Applying shale-style data analytics to Guyana deepwater.")
]

# PEMEX
pemex_blocks = [
    get_h1("PEMEX 2026 Deep Dive"),
    get_h2("1. Executive Summary"), get_p("2026 is a critical refinancing year for PEMEX. With $18.7B in debt due, the Mexican government is providing direct financial lifelines tied to operational reform."),
    get_h2("2. Market Positioning"), get_p("Struggling National Giant. Focus is on stopping production declines while managing a massive debt-to-equity rift."),
    get_h2("3. Financial Frame"), get_bullet("Debt: US$18.7B due in 2026. Refinancing and bond buybacks are top priority."),
    get_h2("4. Operational Roadmap"), get_bullet("Dos Bocas (Olmeca): Reaching full refining throughput. Zama (JV with Harbour Energy) primary upstream growth."),
    get_h2("5. Digital & AI Maturity"), get_p("Low maturity in AI, high need for operational visibility to attract JV partners."),
    get_h2("6. WhiteSpace Action Plan"), get_bullet("Entry: Debt-Grade Operational Visibility. Helping PEMEX 'prove' production efficiency to bondholders.")
]

ids = {}
ids["BP"] = create_page("BP 2026 Deep Dive", "BP", bp_blocks)
ids["Chevron"] = create_page("Chevron 2026 Deep Dive", "Chevron", chevron_blocks)
ids["PEMEX"] = create_page("PEMEX 2026 Deep Dive", "PEMEX", pemex_blocks)
print(f"PAGE_IDS_BATCH4: {json.dumps(ids)}")
