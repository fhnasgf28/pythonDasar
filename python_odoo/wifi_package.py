
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class WifiPackage(models.Model):
    _name = 'wifi.package'
    _description = 'WiFi Package'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Package Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('cancelled', 'Cancelled')
    ], default='draft', string='Status', tracking=True)
    price = fields.Float(string='Price', required=True, tracking=True)
    wifi_package_id = fields.Many2one('wifi.package', string='Parent Package')
    invoice_count = fields.Integer(compute='_compute_invoice_count', string='Invoice Count')

    @api.model
    def process_subscriptions(self):
        """Process subscriptions for WiFi packages."""
        # Logic to process subscriptions goes here
        return True
        @api.model
        def create(self, vals):
            if 'wifi_package_id' in vals:
                wifi_package = self.env['wifi.package'].browse(vals['wifi_package_id'])
                if not wifi_package:
                    raise UserError(_("The specified WiFi package does not exist."))
            return super(WifiPackage, self).create(vals)

        def _compute_invoice_count(self):
            for record in self:
                record.invoice_count = self.env['account.move'].search_count([
                    ('wifi_package_id', '=', record.id),
                    ('state', 'in', ['draft', 'posted'])
                ])
            return True

        @api.model
        def _cron_process_subscriptions(self):
            """Cron job to process WiFi package subscriptions."""
            packages = self.search([('state', '=', 'active')])
            for package in packages:
                package.process_subscriptions()
            return True
