from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MaintenanceOrder(models.Model):
    _inherit = 'maintenance.order'

    @api.model
    def _read_group_state(self, stages, domain, order):
        state = ['draft', 'in_progress', 'done', 'cancel']
        return state

    @api.model
    def _default_approval_matrix(self, company=None, branch=None):
        if not company:
            company = self.env.company
        default = self.env.context.get('default_approval_matrix_id', False)
        if default:
            return default
        if not branch:
            branch = self.env.branch
        matrix_type = 'order_internal' if self.env.context.get('default_mo_type_code', 'internal') == 'internal' else 'order_external'
        return self.env['asset.approval.matrix'].search([
            ('company_id', '=', company.id),
            ('branch_id', '=', branch.id),
            ('matrix_type', '=', matrix_type)
        ], limit=1).id
