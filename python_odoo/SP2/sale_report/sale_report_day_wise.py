class SaleOrderReport(models.Model):
    _name = 'sale.order.report'
    _description = 'Sale Order Report'

    @api.model
    def default_company_ids(self):
        is_allowed_companies = self.env.context.get(
            'allowed_company_ids', False)
        if is_allowed_companies:
            return is_allowed_companies
        return