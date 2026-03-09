def update_industries_ai(self):
    print('farhanassegaf kodingan ini dieksekusi')
    leads = self.search([('industry_ai', '=', False), ('description', '!=', False)])
    for lead in leads:
        sale_orders = self.env['sale.order'].search(
            [('partner_id', '=', lead.partner_id.id), ('state', 'in', ['sale', 'done'])])
        description = " ".join(sale_orders.mapped('order_line.name')) if sale_orders else False
        industry = self.fetch_industry_from_ai(description)
        lead.sudo().write({'industry_ai': industry})
        _logger.info(f"Updated CRM Lead {lead.id} with industry: {industry}")
        print(f"[UPDATE] CRM Lead {lead.id} updated with industry: {industry}")