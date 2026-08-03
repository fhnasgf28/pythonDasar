# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMoveSalesperson(models.Model):
    _name = 'account.move.salesperson'
    _description = 'Invoice Salesperson Composition'
    _order = 'weightage desc, id desc'

    move_id = fields.Many2one('account.move', required=True, ondelete='cascade', index=True)
    user_id = fields.Many2one('res.users', required=True, index=True)
    weightage = fields.Float(default=0.0)
    type = fields.Selection([
        ('main_salesperson', 'Main Salesperson'),
        ('salesperson', 'Salesperson'),
    ], default='salesperson')


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_sales_team_id = fields.Many2one('crm.team', string='Sales Team (KTT)')
    x_salesperson_line_ids = fields.One2many('account.move.salesperson', 'move_id', string='Salespeople (KTT)')
