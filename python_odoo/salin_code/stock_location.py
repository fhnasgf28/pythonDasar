from odoo import _, api, fields, models
import json
from odoo.exceptions import ValidationError, UserError

class StockLocation(models.Model):
    _inherit = 'stock.location'

    is_expired_stock_location = fields.Boolean(string="Is Expired Stock Location", readonly=True)
    occupied_unit = fields.Float('Qty Accupied', digits='Product Unit of Measure', copy=False, readonly=True, compute="_compute_occupied_unit")

    @api.constrains('return_location', 'location_id')
    def _check_return_location(self):
        for record in self:
            if record.return_location:
                warehouse = record.get_warehouse()
                if warehouse:
                    existing_return_loc = self.search([
                        ('id', '!=', record.id),
                        ('return_location', '=', True),
                        ('id', 'child_of', warehouse.view_location.id),
                    ], limit=1)
                    if existing_return_loc:
                        raise ValidationError(_("A return location already exists for this warehouse. Only one return location is allowed per warehouse."))

    @api.returns('stock.warehouse', lambda value: value.id)
    def get_warehouse(self):
        """ Returns warehouse id of warehouse that contains location """
        domain = [('view_location_id', 'parent_of', self.ids)]
        return self.env['stock.warehouse'].search(domain, limit=1)