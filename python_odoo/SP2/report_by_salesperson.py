from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class SalespersonWizard(models.TransientModel):
    _inherit = "sh.sale.report.salesperson.wizard"


    def domain_company(self):
        return [('id', 'in', self.env.companies.ids)]

    def _domain_branch(self):
        allowed_branch_ids = self.env.user.branch_ids
        if self.company_ids:
            allowed_branches = allowed_branch_ids.filtered(lambda x: x.company_id and x.company_id.id in self.company_ids.ids)
            print("allowed_branches", allowed_branches)
            return [('id', 'in', allowed_branches.ids)]
        else:
            return [('id', 'in', allowed_branch_ids.ids)]

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id,domain=domain_company)
    company_ids = fields.Many2many(
        'res.company', string='Companies', domain=domain_company)
    user_order_dic = fields.One2many('user.order.dic', 'report_id')
    currency_precision = fields.Integer("Currency Precision")
    date_start = fields.Datetime(
        string="Start Date",
        required=True,
        default=lambda self: fields.Datetime.to_string(datetime.now() - relativedelta(months=1))
    )
    branch_ids = fields.Many2many('res.branch', string='Branch', default=lambda self: self.env.user.branch_id, domain=_domain_branch)

    @api.onchange('company_ids')
    def _onchange_company_ids_reset_branches(self):
        # When Companies selection changes, reset Branch selection to allow fresh pick under new company scope
        if self.company_ids:
            self.branch_ids = [(5, 0, 0)]