from odoo import models, fields, api

class PurchaseConfigSettings(models.TransientModel):
    _inherit = 'purchase.config.settings'

    is_print_report = fields.Boolean("Print Report")

class YourModel(models.Model):
    _name = 'your.model'  # Gantilah dengan model yang sesuai
    _inherit = 'purchase.order'  # Contoh jika menggunakan purchase.order

    config_id = fields.Many2one('purchase.config.settings', string="Purchase Config")
    is_print_tnc = fields.Boolean("Print TNC", compute="_compute_is_print_tnc", store=True)

    @api.depends('config_id.is_print_report')
    def _compute_is_print_tnc(self):
        for rec in self:
            rec.is_print_tnc = rec.config_id.is_print_report
