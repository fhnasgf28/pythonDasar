from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class SetupBarBankConfigWizard(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'

    @api.default
    def _default_branch(self):
        default_branch_id = self.env.context.get('default_branch_id', False)
        if default_branch_id:
            return default_branch_id
        return self.env.company_branches[0].id if len(self.env.company_branches) == 1 else self.env.branch.id

    @api.model
    def _domain_branch(self):
        return [('id', 'in', self.env.branches.ids), ('company_id', '=', self.env.company.id)]

    branch_id = fields.Many2one('res.branch', string='Branch', default=_default_branch, domain=_domain_branch)

    @api.onchange('branch_id')
    def _onchange_branch_id(self):
        selected_branch = self.branch_id
        if selected_branch:
            user_id = self.env['res.users'].browse(self.env.uid)
            allowed_branch = user_id.sudo().branch_ids
            if allowed_branch and selected_branch.id not in [ids.id for ids in allowed_branch]:
                raise UserError("Please select active branch only. Other may create the Multi branch issue. \n\ne.g: If you wish to add other branch then Switch branch from the header and set that.")

    def validate(self):
        res = super(SetupBarBankConfigWizard, self).validate()
        for rec in self:
            vals = {
                'acc_number': rec.acc_number,
                'bank_id': rec.bank_id.id,
                'bank_bic': rec.bank_bic,
                'company_id': rec.company_id.id,
                'branch_id': rec.branch_id.id,
            }
            self.env['bank.account.account'].create(vals)
        return res

    def default_linked_journal_id(self):
        default = self.env['account.journal'].search(
            [('type', '=', 'bank'), ('bank_account_id', '=', False), ('company_id', 'in', [False, self.company_id.id])],
            limit=1)
        return default[:1].id

class AccountReconcile(models.Model):
    _inherit = 'account.reconcile.model'

    @api.model
    def _default_branch(self):
        default_branch_id = self.env.context.get('default_branch_id', False)
        if default_branch_id:
            return default_branch_id
        return self.env.company_branches[0].id if len(self.env.company_branches) == 1 else self.env.branch.id

    @api.onchange('branch_id')
    def _onchange_branch_id(self):
        selected_branch = self.branch_id
        if selected_branch:
            user_id = self.env['res.users'].browse(self.env.uid)
            allowed_branch = user_id.sudo().branch_ids
            if allowed_branch and selected_branch.id not in [ids.id for ids in allowed_branch]:
                raise UserError()
