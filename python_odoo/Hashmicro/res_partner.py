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

    @api.model
    def create(self, vals):
        res = super(res_partner, self).create(vals)
        config = self.env['sales.config.settings'].search([], limit=1, order='id desc')
        approval = config.is_customer_partner_approval_matrix
        if approval and res.is_customer:
            res.state_customer = 'draft'
        else:
            res.state_customer = 'approved'
        return res

    @api.depends('branch_id')
    def _compute_matrix_customer(self):
        for res in self:
            config = self.env['sales.config.settings'].search([], limit=1, order='id desc')
            approval = config.is_customer_partner_approval_matrix
            res.approving_matrix_customer_id = False
            if approval:
                matrix_id = self.env['approval.matrix.customer'].search([('branch_id', '=', res.branch_id.id)], limit=1)
                if matrix_id:
                    res.approving_matrix_customer_id = matrix_id

    def _compute_approving_matrix_customer(self):
        config = self.env['sales.config.settings'].search([], limit=1, order='id desc')
        is_approving_matrix = config.is_customer_partner_approval_matrix
        for record in self:
            record.is_approving_matrix_customer = is_approving_matrix

    @api.onchange('company_id')
    def _onchange_company_id(self):
        branches = self.env.branches.ids
        return {
            'domain':{
                'branch_id': [
                    ('id', 'in', branches),
                    ('company_id', '=', self.company_id.id)
                ]
            }
        }
