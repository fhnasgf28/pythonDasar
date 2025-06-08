from odoo import fields, api, models, _
from odoo.exceptions import UserError
from odoo.tools import float_round

@api.model
def get_orders_without_invoice(self):
    """Get all orders without invoice"""
    orders = self.search([('state', '=', 'sale'), ('invoiced', '=', False)])
    return orders

def get_orders_with_invoice(self):
    """Get all orders with invoice"""
    orders = self.search([('state', '=', 'sale'), ('invoiced', '=', True)])
    return orders
def get_orders_with_invoice_and_payment(self):
    """Get all orders with invoice and payment"""
    orders = self.search([('state', '=', 'sale'), ('invoiced', '=', True), ('payment_state', '=', 'paid')])
    return orders
def get_orders_with_invoice_and_payment_not_paid(self):
    """Get all orders with invoice and payment not paid"""
    orders = self.search([('state', '=', 'sale'), ('invoiced', '=', True), ('payment_state', '=', 'not_paid')])
    return orders