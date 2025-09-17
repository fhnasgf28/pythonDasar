from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    openai_api_key = fields.Char('OpenAI API Key',
        config_parameter='openai.api_key',
        help="API key for OpenAI services")
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        # This is automatically handled by the config_parameter field
        pass

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            openai_api_key=self.env['ir.config_parameter'].sudo().get_param('openai.api_key', default=''),
        )
        return res
