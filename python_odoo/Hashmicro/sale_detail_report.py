from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime
from odoo import models, fields, api

class SalesDetailWizard(models.TransientModel):
    _inherit = "sh.sale.details.report.wizard"
    _description = "sh sale details report wizard model"

    @api.model
    def domain_company(self):
        return [('id', 'in', self.env.companies.ids)]

    @api.model
    def default_company_ids(self):
        is_allowed_companies = self.env.context.get(
            'allowed_company_ids', False)
        if is_allowed_companies:
            return is_allowed_companies
        return

    def _domain_branch(self):
        return [('id', 'in', self.env.user.branch_ids.ids)]

    def _domain_product_type_selection(self):
        # Use selection records of product.template field 'type'
        return [
            ('field_id.name', '=', 'type'),
            ('field_id.model', '=', 'product.template'),
        ]

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id)
    company_ids = fields.Many2many(
        'res.company', string='Companies', default=default_company_ids, domain=domain_company)
    branch_ids = fields.Many2many('res.branch', string='Branch', domain=_domain_branch,default=lambda self: self.env.user.branch_id)
    product_type_ids = fields.Many2many('ir.model.fields.selection', string='Product Type',domain=_domain_product_type_selection)
    product_categ_ids = fields.Many2many('product.category', string='Product Category')
    state = fields.Char("State")
    total_paid = fields.Float("Total")
    payments = fields.One2many('payment.sale.details.report', 'details_id', string="Payments")
    company_name = fields.Char("Company")
    taxes = fields.One2many('tax.sale.details.report', 'details_id', string="Tax")
    products = fields.One2many('product.sale.details.report', 'details_id', string="Product")
    currency_precision = fields.Integer("Currency Precision")