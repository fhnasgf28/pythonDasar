from odoo import models, fields, api


class SaleConsignment(models.Model):
    _inherit = 'sale.order'

    consignment = fields.Boolean(string='Consignment', default=False)

    def button_transfer_request(self):
        self.ensure_one()
        location_choices = self.consignment_line_ids.mapped('destination_location_id').ids
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transfer Request',
            'res_model': 'request.transfer.header',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': self.customer_id.id,
                'default_sales_consignment_id': self.id,
                'default_destination_filter_ids': location_choices
            }
        }