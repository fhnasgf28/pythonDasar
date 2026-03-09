from odoo import models, fields, api

class ActivityLogWizard(models.TransientModel):
    _name = 'activity.log.wizard'
    _inherit = ['mail.thread']
    _description = 'Wizard untuk menampilkan log aktivitas'

    lead_id = fields.Many2one('crm.lead', 'Lead', default=lambda self: self._context.get('active_id'))
    activity_ids = fields.One2many('mail.activity', compute='_compute_activity_ids')
    message_follower_ids = fields.One2many(
        'mail.followers', 'res_id', string='Followers',
        domain=lambda self: [('res_model', '=', self._name)])
    message_ids = fields.One2many(
        'mail.message', 'res_id', string='Messages',
        domain=lambda self: [('res_model', '=', self._name)])

    @api.depends('lead_id')
    def _compute_activity_ids(self):
        for wizard in self:
            wizard.activity_ids = wizard.lead_id.activity_ids

    @api.depends('lead_id')
    def _compute_message_ids(self):
        for wizard in self:
            wizard.message_ids = wizard.lead_id.message_ids

    @api.model
    def default_get(self, fields):
        res = super(ActivityLogWizard, self).default_get(fields)
        lead_id = self.env.context.get('active_id')
        if lead_id:
            lead = self.env['crm.lead'].browse(lead_id)
            res['message_ids'] = [(0, 0, {
                'author_id': msg.author_id.id,
                'body': msg.body,
                'date': msg.date,
                'message_type': msg.message_type,
                'subtype_id': msg.subtype_id.id,
            }) for msg in lead.message_ids]
        return res