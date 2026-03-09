from odoo import models, fields, api

class ActivityLogWizard(models.TransientModel):
    _name = 'activity.log.wizard'
    _inherit = ['mail.thread']
    _description = 'Wizard untuk menampilkan log aktivitas'

    lead_id = fields.Many2one('crm.lead', string='Lead', required=True)
    activity_ids = fields.One2many('mail.activity', 'res_id', domain=[('res_model', '=', 'crm.lead')], string='Activities')
    message_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'crm.lead')], string='Messages')
    log_content = fields.Html(string="Log History", readonly=True)

    def load_logs(self):
        self.message_ids = self.lead_id.message_ids

    @api.model
    def default_get(self, fields):
        res = super(ActivityLogWizard, self).default_get(fields)
        lead_id = self.env.context.get('active_id')
        lead = self.env['crm.lead'].browse(lead_id)
        res['log_content'] = lead.log_history
        return res