def fetch_industry_from_ai(self, description):
    url = "farhana"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "CompanyName": "Unknown",
        "Industries": [description]
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("industry", "Unknown")
    except requests.exceptions.RequestException as e:
        _logger.error(f"Error fetching industry from AI: {e}")
        return "Unknown"


def update_industries_ai(self):
    leads = self.search([('industries_ai', '=', False), ('description', '!=', False)])
    for lead in leads:
        industry = self.fetch_industry_from_ai(lead.description)
        lead.sudo().write({'industries_ai': industry})
