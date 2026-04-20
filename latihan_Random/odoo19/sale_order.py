from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    item_text_filter = fields.Char(string='Item Text Filter', store=False, search= '_search_item_text_filter', help='Filter items by text')

    def _search_by_item_text(self, operator, value):
        order_lines = self.env['sale.order.line'].search([
            ('product_id.item_text', operator, value)
        ])
        order_ids = order_lines.mapped('order_id').ids
        return [('id', 'in', order_ids)]

    @api.onchange('hm_team_ids')
    def _onchange_hm_team_ids(self):
        for record in self:
            record.main_hm_team_id = self.hm_team_ids[0] if len(self.hm_team_ids.ids) > 0 else False

    def action_create_multiple_recurring_invoices(self):
        for order in self.env['sale.order'].browse(self._context_get('active_ids', [])):
            order.action_create_multiple_recurring_invoices()

    @api.depends('recurring_invoice_count')
    def get_total_recuurring_amount(self):
        for rec in self:
            total_amount = 0
            for line in self.env['account.move'].search([('recurring_sale_order_id', '=', rec.id)]):
                total_amount += line.amount_total
            rec.recurring_total = total_amount


