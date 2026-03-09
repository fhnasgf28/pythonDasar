from datetime import timedelta
from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    first_meeting_date = fields.Datetime(string="First Meeting Date", help="Date of the first meeting linked to this opportunity")
    tracking_duration = fields.Integer(string="Tracking Duration (Days)", compute="_compute_tracking_duration", store=True, help="Time duration (in days) from first meeting to stage change")

    @api.depends('stage_id', 'first_meeting_date')
    def _compute_tracking_duration(self):
        stage_ids = [
            self.env.ref('your_module_name.stage_lead17').id,  # (BD)WARM
            self.env.ref('your_module_name.stage_lead18').id,  # (BD)FOCUS
        ]
        for lead in self:
            if lead.stage_id.id in stage_ids and lead.first_meeting_date:
                duration = (fields.Datetime.now() - lead.first_meeting_date).days
                lead.tracking_duration = duration
            else:
                lead.tracking_duration = 0

    def write(self, vals):
        stage_ids = [
            self.env.ref('your_module_name.stage_lead17').id,  # (BD)WARM
            self.env.ref('your_module_name.stage_lead18').id,  # (BD)FOCUS
        ]
        for lead in self:
            previous_stage = lead.stage_id.id
            new_stage = vals.get('stage_id', previous_stage)
            if previous_stage == self.env.ref('your_module_name.stage_lead2').id and new_stage in stage_ids:
                if lead.first_meeting_date:
                    duration = (fields.Datetime.now() - lead.first_meeting_date).days
                    lead.tracking_duration = duration
        return super(CrmLead, self).write(vals)
