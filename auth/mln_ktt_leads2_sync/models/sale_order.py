# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderSalesperson(models.Model):
    _name = 'sale.order.salesperson'
    _description = 'Sale Order Salesperson Composition'
    _order = 'weightage desc, id desc'

    order_id = fields.Many2one('sale.order', required=True, ondelete='cascade', index=True)
    user_id = fields.Many2one('res.users', required=True, index=True)
    weightage = fields.Float(default=0.0)
    type = fields.Selection([
        ('main_salesperson', 'Main Salesperson'),
        ('salesperson', 'Salesperson'),
    ], default='salesperson')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_ktt_leads2_id = fields.Char(index=True, copy=False)
    x_sales_team_id = fields.Many2one('crm.team', string='Sales Team (KTT)')
    x_salesperson_line_ids = fields.One2many('sale.order.salesperson', 'order_id', string='Salespeople (KTT)')

    def _prepare_invoice(self):
        vals = super()._prepare_invoice()
        vals.update({
            'x_sales_team_id': self.x_sales_team_id.id,
            'x_salesperson_line_ids': [(0, 0, {
                'user_id': line.user_id.id,
                'weightage': line.weightage,
                'type': line.type,
            }) for line in self.x_salesperson_line_ids],
        })
        return vals
