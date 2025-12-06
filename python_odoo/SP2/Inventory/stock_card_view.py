from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockCardView(models.Model):
    _inherit = 'stock.card.view'

    @api.model
    def replace_view(self, warehouse_ids, product_ids, categ_ids, start_date, end_date):
        # Server-side validation to ensure proper date range
        start = fields.Date.to_date(start_date) if start_date else None
        end = fields.Date.to_date(end_date) if end_date else None
        if start and end and start > end:
            raise ValidationError(_("Date range is not valid: From Date must be earlier than To Date."))

        wizard = self.env['setu.stock.movement.report'].create({
            'company_id': self.env.company.id,
            'warehouse_ids': [(6, 0, warehouse_ids)],
            'product_ids': [(6, 0, product_ids)],
            'product_category_ids': [(6, 0, categ_ids)],
            'start_date': start_date or False,
            'end_date': end_date or False
        })

        wizard._pre_download_report()
        self.set_view(wizard.get_report())
        wizard._post_download_report()

    @api.model
    def get_warehouse_domain_for_user(self):
        domain = [('company_id','=', self.env.company.id)]
        user_warehouses = self.env.user.warehouse_ids
        if user_warehouses:
            domain.append(('id', 'in', user_warehouses.ids))
        allowed_warehouses = self.env['stock.warehouse'].search(domain)
        return allowed_warehouses.ids