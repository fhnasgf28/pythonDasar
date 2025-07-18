from odoo import fields, api, models, _

class res_partner(models.Model):
    _inherit = 'res.partner'

    # default branch_id
    branch_id = fields.Many2one('res.branch', string="Branch", required=False)

    @api.model
    def _default_domain(self):
        context = dict(self.env.context)
        if context.get('branch_id'):
            return [('branch_id', '=', context.get('branch_id'))]
        return super(res_partner, self)._default_domain()