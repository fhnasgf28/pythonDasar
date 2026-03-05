from odoo import models, _
from odoo.exceptions import UserError

class ExternalIntegrationMixin(models.AbstractModel):
    _name = "external.integration.mixin"
    _description = "External API Integration Helper"

    def _get_external_config(self):
        ICP = self.env['ir.config_parameter'].sudo()

        base_url = (ICP.get_param('external_api.base_url') or '').rstrip('/')
        token = ICP.get_param('external_api.token') or ''

        if not base_url:
            raise UserError(_("Base URL belum diset (external_api.base_url)."))

        if not token:
            raise UserError(_("Token belum diset (external_api.token)."))

        return base_url, token
