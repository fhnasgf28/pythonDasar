from odoo import api, fields, models, _
from lxml import etree
from odoo.exceptions import ValidationError


class PricelistsApprovalMatrix(models.Model):
    _name = "approval.customer.pricelist"
    _description = "Approval Matrix Customer"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    name = fields.Char(string='Name', tracking=True, required=True)
    company_id = fields.Many2one("res.company", string="Company", tracking=True, required=True, readonly=True,
                                 default=lambda self: self.env.company.id)
    branch_id = fields.Many2one("res.branch", string="Branch", tracking=True, required=True, )
    config = fields.Selection([
        ('total_amt', 'Total Amount'),
        # ('margin_amt', 'Margin Amount'),
        ('pargin_per', 'Margin Percentage'),
        ('discount_amt', 'Discount Amount'),
        # ('discount_Pet', 'Discount Percentage')
    ], 'Configuration', store=True, required=True, default="total_amt", tracking=True)
    minimum_amt = fields.Float(string='Minimum Amount', required=True, tracking=True)
    maximum_amt = fields.Float(string='Maximum Amount', required=True, tracking=True)
    approver_matrix_line_ids = fields.One2many('approval.customer.pricelist.lines', 'approval_matrix',
                                               string="Approver Name")
    description = fields.Text(
        default="Margin configuration will check the margin total from margin in each order line.", readonly=True)
    filter_branch = fields.Char(string="Filter Branch", compute='_compute_filter_branch', store=False)


class ApprovalMatrixSaleOrderLines(models.Model):
    _name = 'approval.customer.pricelist.lines'
    _description = "Approval Matrix Sale Order Lines"

    user_name_ids = fields.Many2many('res.users', string="Users", required=True)
    sequence = fields.Integer(required=True, index=True, help='Use to arrange calculation sequence')
    sequence2 = fields.Integer(
        string="No.",
        related="sequence",
        readonly=True,
        store=True
    )
    minimum_approver = fields.Integer(string="Minimum Approver", required=True, default=1)
    state_char = fields.Text(string='Approval Status')
    time_stamp = fields.Datetime(string='Timestamp')
    feedback = fields.Char(string='Rejected Reason')
    last_approved = fields.Many2one('res.users', string='Users')
    approved = fields.Boolean('Approved')
    # approved_users = fields.Many2many('res.users', 'approved_users_sale_patner_rel', 'order_id', 'user_id',
    #                                   string='Users')
    signature = fields.Binary(related="last_approved.digital_signature", string="Signature", store=True)
    approval_type = fields.Selection(
        [('total_amt', 'Total Amount'), ('margin_amt', 'Margin Amount'), ('pargin_per', 'Margin Percentage'),
         ('discount_amt', 'Discount Amount')])
    approver_state = fields.Selection([('draft', 'Draft'), ('pending', 'Pending'), ('approved', 'Approved'),
                                       ('refuse', 'Refused')], default='draft', string="State")
    approval_matrix = fields.Many2one('approval.customer.pricelist', 'Approval Matrix')
