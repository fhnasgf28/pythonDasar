def fetch_industry_from_ai(self, description):
    url = "farhan"
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }
    payload = {"description": description}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("industry", "Unknown")
    except requests.exceptions.RequestException as e:
        _logger.error(f"Error fetching industry from AI: {e}")
        return "Unknown"


def update_industries_ai(self):
    """
    Mengupdate field industries_ai berdasarkan hasil.
    """
    leads = self.search([('industries_ai', '=', False), ('description', '!=', False)])

    for lead in leads:
        industry = self.fetch_industry_from_ai(lead.description)
        lead.sudo().write({'industries_ai': industry})
        _logger.info(f"Updated CRM Lead {lead.id} with industry: {industry}")
