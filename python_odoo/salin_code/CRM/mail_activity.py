from odoo import models, fields, api, tools
from datetime import datetime, date
from odoo.exceptions import ValidationError
import requests

headers = {'content-type': 'application/json'}
import logging
_logger = logging.getLogger(__name__)

class MailActivity(models.Model):
    _inherit = 'mail.activity'

    attachment_ids = fields.Many2many('ir.attachment', 'mail_activity_attachment_rel', 'message_id', 'attachment_id',string='Attachments')
    is_attachment_required = fields.Boolean(related='activity_type_id.is_attachment_required')

    def activity_format(self):
        res = super(MailActivity, self).activity_format()
        for line in res:
            if line.get('attachment_ids'):
                attachment_data = []
                attachment_ids = self.env['ir.attachment'].browse(line.get('attachment_ids'))
                for attachment in attachment_ids:
                    attachment_data.append({
                        'id': attachment.id,
                        'res_id': line.get('res_model'),
                        'mimetype': attachment.mimetype,
                        'filename': attachment.name,
                    })
                line['attachment_ids'] = attachment_data
            return res

    @api.model
    def create(self, values):
        res = super(MailActivity, self).create(values)
        if res.res_model == "crm.lead":
            if not res.calendar_event_id:
                if res.activity_type_id.attachment_required and not res.attachment_ids:
                    raise ValidationError('Attachments are Required!')
                try:
                    crm_lead = self.env['crm.lead'].browse(res.res_id)
                    number_of_repetition = self.env['ir.config_parameter'].sudo().get_param('equip3_crm_operation.number_of_repetition')
                    crm_lead.number_of_repetition = number_of_repetition
                except:
                    pass
        return res

    def write(self, vals):
        res = super(MailActivity).write(vals)
        for record in self:
            if record.res_model == 'crm.lead':
                if not record.calendar_event_id:
                    if record.activity_type_id.attachment_required and not record.attachment_ids:
                        raise ValidationError('Attachments are Required!')
        return res

    @api.model
    def auto_follow_up_leads_sales_team(self):
        today_date = date.today()
        activity_ids = self.search([
            ('res_model', '=', 'crm.lead'),
            ('date_deadline', '<', today_date)
        ])
        template_id = self.env.ref('equip3_crm_operation.email_template_leader_team')
        saleperson_template_id = self.env.ref('equip3_crm_operation.email_template_salesperson')
        action_id = self.env.ref('crm.crm_lead_action_pipeline')
        crm_leads = self.env['crm.lead'].search([('id', 'in', activity_ids.mapped('res_id'))])
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url = base_url + '/web#action=' + str(action_id.id) + '&view_type=list&model=crm.lead&id='
        leaders = crm_leads.mapped('team_id').mapped('user_id')
        for leader in leaders:
            break

    def recap_message_activity_wa(self, lead, activity,is_leader=False):
        judul = activity.activity_type_id.name
        if activity.summary:
            judul += " - {}".format(activity.summary)
            msg = " "
            if is_leader:
                msg += "Salesperson : {}\n".format(activity.user_id.name)
                msg += "Leads : {}\n".format(lead.name)
                msg += "Activity Type - Summary :{}\n".format(judul)
                msg += "Due Date : {}\n".format(activity.date_deadline)
                msg += "-------------------------\n"
                return msg

