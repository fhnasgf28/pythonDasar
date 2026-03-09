from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ApprovalMatrix(models.Model):
    _name = 'approval.matrix'
    _description = 'approval matrix'

    name = fields.Char(string='Request Name', required=True)
    amount_total = fields.Float(string='Total Amount', required=True)
    requester_id = fields.Many2one('res.users', string='Requester', default=lambda self: self.env.user)
    manager_id = fields.Many2one('res.users', string='Manager Approver')
    department_head_id = fields.Many2one('res.users', string='Department Head Approver')
    director_id = fields.Many2one('res.users', string='Director Approver')
    approval_stage = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_manager', 'Waiting Manager'),
        ('waiting_head', 'Waiting Department Head'),
        ('waiting_director', 'Waiting Director'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        res = super(ApprovalMatrix, self).create(vals)
        res._set_initial_stage()
        return res

    def _set_initial_stage(self):
        for rec in self:
            if rec.amount_total < 5000000:
                rec.approval_stage = 'waiting_manager'
            elif rec.amount_total <= 50000000:
                rec.approval_stage = 'waiting_head'
            else:
                rec.approval_stage = 'waiting_director'
    
    def action_approve(self):
        for rec in self:
            if rec.approval_stage == 'waiting_manager':
                rec.approval_stage = 'waiting_head'
            elif rec.approval_stage == 'waiting_head':
                rec.approval_stage = 'approved'
            elif rec.approval_stage == 'waiting_director':
                rec.approval_stage = 'approved'
            else:
                raise UserError("Cannot approve in current stage: %s" % rec.approval_stage)
    
    def action_reject(self):
        for rec in self:
            rec.approval_stage = 'rejected'

            