from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.http import request

class mailActivity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def create(self, vals):
        if 'new_potential' in vals:
            if vals['new_potential'] == 'not_updated':
                raise ValidationError("Potential value is not allowed.")
        if 'res_model_id' in vals and 'calendar_event_id' not in vals:
            model = self.env['ir.model'].search([('id', '=', vals['res_model_id'])]).model
            if model == 'crm.lead':
                cs = request.env.user.has_group("crminternal_modifier.crm_group_cs_team")
                if not cs:
                    if not ('new_potential' in vals and 'cannot_be_quoted' in vals and 'quotation' in vals):
                        raise ValidationError("If you change any of the following data below, then you must change all of them.\n- Potential\n- Cannot be Quoted\n- Quotation Sent Status")
        res = super(mailActivity, self).create(vals)
        for activity in res:
            if activity.res_model == 'crm.lead' and activity.res_id:
                lead = self.env['crm.lead'].browse(activity.res_id)
                lead._get_leads_to_follow_up()
        if res.res_model == 'crm.lead':
            calendar_event_id = False
            if res.calendar_event_id:
                calendar_event_id = res.calendar_event_id.id
            res_activity_obj = self.env['res.mail.activity']
            res_activity_obj.create({
                'name': res.res_name,
                'summary': res.summary,
                'activity_type_id': res.activity_type_id.id,
                'date_deadline': res.date_deadline,
                'calendar_event_id': calendar_event_id,
                'state': res.state,
                'res_id': res.res_id,
                'act_id': res.id,
                'new_potential': res.new_potential,
                'cannot_be_quoted': res.cannot_be_quoted,
                'quotation': res.quotation,
                'final_quotation': res.final_quotation.id
            })
            lead = self.env[res.res_model].browse(res.res_id)
            lead.with_context(active_model_id=self._description).write({
                'new_potential': res.new_potential,
                'last_update': res.last_update,
                'challenges': res.challenges,
                'warm_focus_date': res.warm_focus_date,
                'cannot_be_quoted': res.cannot_be_quoted,
                'quotation': res.quotation,
                'remark': res.remark,
                'final_quotation': res.final_quotation.id,
                'quotation_feedback_id': res.quotation_feedback_id.id,
                'latest_follow_up_date': res.latest_follow_up_date,
            })
            lead.set_due_date_and_missed()
        return res

    def unlink(self):
        for rec in self:
            res_acts = self.env['res.mail.activity'].search([('act_id', '=', rec.id)])
            for res_act in res_acts:
                if res_act.state != 'done':
                    res_act.state = 'cancel'
                res_act.res_id.set_due_date_and_missed()
            #menggunakan super akan memunculkan error yang sama (singleton)
        return super(mailActivity, self).unlink()