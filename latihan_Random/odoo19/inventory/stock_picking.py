import re
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_consignment_sequence_warehouse(self):
        self.ensure_one()
        return (self.warehouse_id
                or self.picking_type_id.warehouse_id
                or self.location_id.warehouse_id
                or self.location_dest_id.warehouse_id
                )

    def _get_consignment_sequence_prefix(self):
        self.ensure_one()
        if self.picking_type_id.code:
            return 'CONS/OUT' if self.picking_type_id.code == 'outgoing' else 'CONS/IN'
        if self.location_id.warehouse_id and not self.location_dest_id.warehouse_id:
            return 'CONS/OUT'

        return 'CONS/IN'

    def _get_consignment_sequence_suffix(self):
        self.ensure_one()
        match = re.match(r'^[^/]+/(?:CONS/IN|CONS/OUT)(.*)$', self.name or '')
        return match.group(1) if match else False

    @api.model
    def create(self, vals):
        picking = super().create(vals)
        if picking.is_consignment and picking.consignment_id:
            warehouse = picking._get_consignment_sequence_warehouse()
            warehouse_code = warehouse.code.upper() if warehouse and warehouse.code else 'UNKNOWN'
            prefix = picking._  get_consignment_sequence_prefix()
            suffix = picking._get_consignment_sequence_suffix()
            if suffix:
                picking.name = f"{warehouse_code}/{prefix}{suffix}"
        return picking
