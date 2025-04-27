from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    @api.depends('state', 'total_summary_line.qty_to_invoice')
    def _get_invoiced(self):
        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        for order in self:
            if order.state not in ('order', 'done'):
                order.invoice_status = 'no'
                continue

            invoices = self.env['account.move.line'].search([('summary_line_id', 'in', order.total_summary_line.mapped('id'))])
            if invoices:
                if any(invoices.filtered(lambda r: r.move_id.state in ('draft','to_approve'))):
                    order.invoice_status = 'not_fully_invoiced'
                    continue
                posted_invoices = invoices.filtered(lambda r: r.move_id.state == 'posted')
                total_posted_amount = sum(posted_invoices.mapped('move_id.amount_total'))
            
                if all(posted_invoices) and total_posted_amount == order.amount_total:
                    order.invoice_status = 'invoiced'
                
                if all(posted_invoices) and total_posted_amount != order.amount_total:
                    order.invoice_status = 'not_fully_invoiced'
            else:
                order.invoice_status = 'no'