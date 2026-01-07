import json
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ReceivingNotesApprovalMatrix(models.Model):
    _name = 'rn.approval.matrix'
    _description = "Receiving Notes Approval Matrix"
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)
    company_id = fields.Many2one('res.company', 'Company',required=True, tracking=True, readonly=True, default=lambda self: self.env.company)
    branch_id = fields.Many2one('res.branch', 'Branch', tracking=True, default=lambda self: self.env.brach)
    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse', tracking=True, required='1')
    create_date = fields.Datetine('Create On', tracking=True, readonly='1')
    create_uid = fields.Many2one('res.users', 'Created by', tracking=True, readonly='1')
    rn_approval_matrix_line_ids = fields.One2many('rn.approval_matrix_line', 'rn_approval_matrix_id1', string='Approver Line')
    rn_approval_matrix_details_id = fields.One2many('rn.approval_matrix_detail', 'rn_approval_matrix_id2', string='Details')
    location_child_ids = fields.Many2many('stock.location', 'locattion_matrix_rel_id', 'loc_id', string='Locations')
    level = fields.Integer('Level', compute='compute_level')
    warehouse_id_domain = fields.Char(string='Warehouse Domain', compute='_compute_warehouse_domain')
    branch_id_domain = fields.Char(string='Branch Domain', compute='_compute_branch_domain')

    @api.depends('company_id')
    def _compute_branch_domain(self):
        for record in self:
            branch_ids = self.env['res.branch'].search([
                ('company_id','=', record.company_id.id)
            ]).ids
            record.branch_id_domain = json.dumps([('id', '=', branch_ids)])

    @api.onchange('branch_id')
    def _onchange_branch_id(self):
        self.ensure_one()
        if self.warehouse_id.branch_id != self.branch_id:
            self.warehouse_id = False

    @api.depends('branch_id')
    def _compute_warehouse_domain(self):
        for record in self:
            if not record.branch_id:
                record.warehouse_id_domain = json.dumps([('id', 'in', [])])
            else:
                warehouse_ids = self.env['stock.warehouse'].search([
                    ('branch_id', '=', record.branch_id.id)
                ]).ids
                record.warehouse_id_domain = json.dumps([('id', 'in', warehouse_ids)])

    def compute_level(self):
        for record in self:
            record.level = len(record.rn_approval_matrix_line_ids)

    @api.constrains('warehouse_id')
    def check_if_location_exists(self):
        current_model = self.env['rn.approval.matrix'].search(
            [('warehouse_id', '=', self.warehouse_id.id)], limit=1
        )
        if current_model and current_model.id != self.id:
            raise ValidationError("%s exists in %s" % (self.warehouse_id.name, current_model.name))

    @api.constrains('rn_approval_matrix_line_ids')
    def _check_has_approver_lines(self):
        for rec in self:
            if not rec.rn_approval_matrix_line_ids:
                raise ValidationError("You must define at least one approver line.")

    @api.onchange('warehouse_id')
    def onchange_warehouse(self):
        location_ids = []
        if self.warehouse_id:
            location_obj = self.env['stock.location']
            store_location_id = self.warehouse_id.view_location_id.id
            additional_ids = location_obj.search(
                [('location_id', 'child_of', store_location_id)]
            )
            for location in additional_ids:
                if location.location_id.id not in additional_ids.ids:
                    location_ids.append(location.id)
            child_location_ids = self.env['stock.location'].search(
                [('id', 'child_of', location_ids), ('id', 'not in', location_ids)]
            ).ids
            final_location = child_location_ids + location_ids
            self.location_child_ids = [(6, 0, final_location)]
        else:
            self.location_child_ids = [(6, 0, [])]

















