from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    state = fields.Selection(selection_add=[('waiting_material', 'Waiting For Material')])

    @api.onchange('move_raw_ids', 'bom_id')
    def _check_material_availability(self):
        """Check if the required materials are available when BOM consumption is strict."""
        for production in self:
            if production.bom_id and production.bom_id.consumption == 'strict':
                has_available_material = any(move.state in ['assigned', 'done'] for move in production.move_raw_ids)

                if not has_available_material:
                    production.state = 'waiting_material'

    def action_confirm(self):
        """Override confirm action to enforce material check."""
        res = super(MrpProduction, self).action_confirm()
        self._check_material_availability()
        return res

    def action_assign(self):
        """Override assign action to check materials."""
        res = super(MrpProduction, self).action_assign()
        self._check_material_availability()
        return res
