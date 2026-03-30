from odoo import api, fields, models, _
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.invoice_lines.move_id')
    def _compute_invoice(self):
        for order in self:
            invoices = order.mapped('order_line.invoice_lines.move_id')
            order.invoice_ids = invoices
            order.invoice_count = len(invoices)

    @api.depends('state', 'date_order','date_approve')
    def _compute_date_calendar_start(self):
        for order in self:
            order.date_calendar_start = order.date_approve if (order.state == 'purchase') else order.date_order

    def _compute_access_url(self):
        super(PurchaseOrder, self)._compute_access_url()
        for order in self:
            order.access_url = 'my/purchase/%s' % (order.id)

    @api.depends('order_line.date_planned')
    def _compute_date_planned(self):
        for order in self:
            dates_list = order.order_line.filtered(lambda x: not x.display_type and x.date_planned).mapped('date_planned')
            if dates_list:
                order.date_planned = max(dates_list)
            else:
                order.date_planned = False