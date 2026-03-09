def fetch_modules_from_ai(self, description_text):
    url_modules = "https://kttx1ae.hashmicro.com/api/v1/check/modules"
    headers = {
        "Content-Type": "application/json"
    }
    payload_modules = {
        "ModulesName": description_text if description_text else "No Description",
        "ModulesList": "[ 'Manufacturing', 'CRM Module', 'Sales Module', 'Purchase Module', 'Construction Module', 'Inventory Module', 'HRM']"
    }

    try:
        response = requests.post(url_modules, headers=headers, data=json.dumps(payload_modules), timeout=10)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except requests.exceptions.RequestException as e:
        _logger.info(f"Error fetching modules from AI: Request failed - {e}")
        return ""  # Return empty dict in case of API error
    except json.JSONDecodeError:
        _logger.info("Error decoding JSON response from AI Module API.")
        return ""


def fetch_industry_from_ai(self, company_name):
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
        "Industries": "['Manufacturing', 'Retail', 'F&B', 'Services', 'IT']"
    }
    valid_industries = ['Manufacturing', 'Retail', 'F&B', 'Services', 'IT']

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        data = response.json()
        # valid_industry = data
        if "IndustryName" in data:
            industry_name = str(data["IndustryName"]).strip()
            if industry_name in valid_industries:
                return industry_name
            else:
                return "Unclear"
    except requests.exceptions.RequestException as e:
        return "Unknown"


def cron_update_industries_ai(self):
    self.update_industries_ai()


def cron_update_modules_ai(self):
    self.update_modules_ai()


def update_industries_ai(self):
    batch_size = 200
    offset = 0
    while True:
        self.env.cr.execute("""
            SELECT id, partner_name 
            FROM crm_lead 
            WHERE industry_ai_id IS NULL 
            AND industry_ai_processed = FALSE
            LIMIT %s OFFSET %s
        """, (batch_size, offset))
        leads = self.env.cr.fetchall()

        if not leads:
            break

        for lead_id, partner_name in leads:
            industry_name = self.fetch_industry_from_ai(partner_name) or "Unknown"

            # Cari industry berdasarkan nama
            industry = self.env['crm.industry'].search([('name', '=', industry_name)], limit=1)
            if not industry:
                industry = self.env['crm.industry'].create({'name': industry_name})
            self.env.cr.execute(
                "UPDATE crm_lead SET industry_ai_id = %s WHERE id = %s",
                (industry.id, lead_id)
            )
            self.env.cr.execute(
                "UPDATE crm_lead SET industry_ai_processed = %s WHERE id = %s",
                (True, lead_id)
            )

        offset += batch_size
        self.env.cr.commit()
    return True


def update_modules_ai(self):
    batch_size = 200
    offset = 0
    while True:
        leads = self.search([('modules_ids', '=', False)], limit=batch_size, offset=offset)
        if not leads:
            break

        for lead in leads:
            sale_orders = self.env['sale.order'].search([
                ('opportunity_id', '=', lead.id),
                ('state', '!=', 'done'),
                ('modules_ai_processed', '=', False)])
            if not sale_orders:
                continue
            descriptions = []
            for order in sale_orders:
                for line in order.order_line:
                    if line.name:
                        descriptions.append(line.name)

            description_text = ', '.join(descriptions) if descriptions else ""
            suggested_modules = self.fetch_modules_from_ai(description_text)  # Fetch module names from AI

            if suggested_modules:
                suggested_modules_dict = json.loads(suggested_modules)
                module_names = [module_name for module_name, value in suggested_modules_dict.items() if value == 1]
                module_records = self.env['crm.module'].search([('name', 'in', module_names)])
                if module_records:
                    lead.write({'modules_ids': [(6, 0, module_records.ids)]})
                    for order in sale_orders:
                        order.write({'modules_ai_processed': True})
                else:
                    _logger.info(f"Lead {lead.id}: No modules found with names: {module_names}")
            else:
                _logger.info(f"Lead {lead.id}: No modules suggested by AI.")

        offset += batch_size
        self._cr.commit()
    return True