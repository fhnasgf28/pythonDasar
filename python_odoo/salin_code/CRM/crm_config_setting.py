from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError, Warning

class CrmConfigSetting(models.Model):
    _name = 'crm.config.settings'
    _description = 'CRM Config Settings'

    name = fields.Char(string='Name')
    enable_sale_order_in_jpl = fields.Boolean(string='Enable Sale Order in JPL', company_dependent=True)

    @api.onchange('enable_fu_email_reminder')
    def _onchange_enable_fu_email_reminder(self):
        for rec in self:
            if rec.enable_fu_email_reminder:
                rec.fu_days_threshold = 7
            else:
                rec.fu_days_threshold = 0

    def save_config(self):
        self.write({
            'enable_sale_order_in_jpl': self.enable_sale_order_in_jpl,
            'is_sign_in_radius_validation': self.is_sign_in_radius_validation,
            'auto_create_customer': self.auto_create_customer,
            'enable_fu_email_reminder': self.enable_fu_email_reminder,
            'fu_days_threshold': self.fu_days_threshold
        })
        if self.fu_days_threshold:
            self.env['crm.stage'].search([]).filtered(lambda s: s.stages_fu_threshold_days == 0 and not s.is_lost and not s.is_won).write({'stages_fu_threshold_days': self.fu_days_threshold})

        return {
            'type': 'ir.actions.client',
            'res_model': 'crm.config.settings',
            'tag': 'reload',
            'view_id': self.env.ref('equip3_crm_operation.crm_config_setting_view_form').id,
            'view_mode': 'form',
            'target': 'inline',
        }