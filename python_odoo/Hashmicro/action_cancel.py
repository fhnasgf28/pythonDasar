from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ActionCancel(models.Model):
    _inherit = 'sale.order'

    def action_cancel(self):
        for record in self:
            if record.state == 'sale':
                picking_ids = record.picking_ids
                invoice_ids = record.order_line.mapped('invoice_lines.move_id')
                if invoice_ids and any(invoice.state == 'posted' for invoice in invoice_ids) and \
                    picking_ids and any(picking.state == 'done' for picking in picking_ids):
                    raise ValidationError('You Cannot Cancel Confirmed SO!')
                elif invoice_ids and any(invoice.state == 'draft' for invoice in invoice_ids):
                    raise ValidationError('There is an unfinish invoice. Please cancel the invoice first!')
                else:
                    if picking_ids and any(picking.state == 'done' for picking in picking_ids):
                        raise ValidationError("You can't cancel Delivered SO!")
                    elif picking_ids and any(picking.state not in ('done', 'cancel', 'rejected') for picking in picking_ids):
                        raise ValidationError("There is an unfinish delivery order. Please cancel DO first!")
                    else:
                        record.write({'state': 'cancel', 'sale_state': 'cancel', 'is_quotation_cancel': False})
            else:
                record.write({'state': 'cancel', 'sale_state': 'cancel', 'is_quotation_cancel': True})
