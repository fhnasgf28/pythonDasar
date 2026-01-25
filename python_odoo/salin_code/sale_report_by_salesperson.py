from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from odoo import tools
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, timedelta

class UserOrderDic(models.TransientModel):
    _name = "user.order.dic"
    _description = "User Order Dic"

    report_id = fields.Many2one('sh.sale.report.salesperson.wizard')
    list_order = fields.Many2one('list.order', 'order_dic_id')
    salesperson = fields.Char("Name")

class ListOrder(models.TransientModel):
    _name = "list.order"
    _description = "List Order"

    order_dic_id = fields.Many2one('user.order.dic')
    order_number = fields.Char("Order Name")
    order_date = fields.Datetime("Order Date")
    customer = fields.Char("Customer")
    total = fields.Float("Total")
    paid_amount = fields.Float("Paid Amount")
    due_amount = fields.Float("Due Amount")
    branch_id = fields.Many2one('res.branch', string='Branch')

    def unlink(self):
        for rec in self:
            if rec.order_number:
                raise ValidationError("You Cannot delete this record")
        return super(ListOrder, self).unlink()

class SalespersonWizard(models.TransientModel):
    _inherit = "sh.sale.report.salesperson.wizard"

    def domain_company(self):
        return [('id', 'in', self.env.companies.ids)]

    def _domain_branch(self):
        return [('id', 'in', self.env.branch_id.ids)]

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id, domain=domain_company)
    company_ids = fields.Many2many(
        'res.company', string='Companies', domain=domain_company)
    user_order_dic = fields.One2many('user.order.dic', 'report_id')
    currency_precision = fields.Integer("Currency Precision")
    date_start = fields.Datetime(
        string="Start Date", required=True, default=lambda self: fields.Datetime.to_string(datetime.now() - relativedelta(month=1))
    )
    branch_ids = fields.Many2many('res.branch', string='Branch', domain=_domain_branch)

    @api.onchange('company_ids')
    def _onchange_company_ids_update_branch_domain(self):
        user_allowed = self.env.user.branch_ids
        allowed_branches = (
            user_allowed.filtered(lambda b: b.company_id and b.company_id in self.company_ids.ids)
            if self.company_ids else user_allowed
        )
        domain = [('id', 'in', allowed_branches.ids)]
        if 'branch_id' in self._fields and self.branch_id and self.branch_id and self.branch_id not in allowed_branches:
            self.branch_id = False
        if 'branch_ids' in self._fields and self.branch_ids:
            self.branch_ids = self.branch_ids.filtered(lambda b: b in allowed_branches)
        return {'domain': {'branch_id': domain, 'branch_ids': domain}}