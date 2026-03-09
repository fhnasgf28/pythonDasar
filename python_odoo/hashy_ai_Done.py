def fetch_industry_from_ai(self, company_name, description):
    """
    Mengirim data partner_name dan quotation description ke Hashy AI
    dan mengembalikan industri yang sesuai.
    """
    url = "https://kttx1ae.hashmicro.com/api/v1/check/industries"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "CompanyName": company_name if company_name else "unknown Company",
        "Industries": [description] if description else []
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        data = response.json()
        valid_industry = data
        print(f"[SUCCESS] AI Response for '{company_name} - {description}': {valid_industry}")
        return str(valid_industry)
    except requests.exceptions.RequestException as e:
        return "Unknown"


def cron_update_industries_ai(self):
    self.update_industries_ai()


def update_industries_ai(self):
    print('farhanassegaf kodingan ini dieksekusi')
    leads = self.search([('industry_ai', '=', False), ('description', '!=', False)])
    for lead in leads:
        sale_orders = self.env['sale.order'].search([('opportunity_id', '=', lead.id)])
        if not sale_orders:
            continue
        descriptions = []
        for order in sale_orders:
            for line in order.order_line:
                if line.name:
                    descriptions.append(line.name)
        description_text = ', '.join(descriptions) if descriptions else "Unknown"
        industry = self.fetch_industry_from_ai(lead.partner_name, description_text)
        lead.sudo().write({'industry_ai': industry})
        print(f"[UPDATE] CRM Lead {lead.id} updated with industry: {industry}")
    return True