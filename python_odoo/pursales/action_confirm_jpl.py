from odoo import models, fields, api

class CrmJourneyPlanFeedbackWizard(models.TransientModel):
    _name = "crm.journey.plan.feedback.wizard"
    _description = "Feedback for Journey Plan"    

    jpl_id = fields.Many2one('crm.journey.plan.line', string="Journey Plan Line")
    feedback = fields.Text("Feedback", required=True)

    def action_confirm(self):
        self.jpl_id.write({
            'feedback': self.feedback,
            'feedback_created_by': self.env.user.id
        })

        # Cari aktivitas spesifik untuk journey plan line yang terkait dengan activity_type_id
        jpl_activity = False
        if self.jpl_id.activity_type_id:
            jpl_activity = self.env['mail.activity'].search([
                ('res_model_id', '=',
                 self.env['ir.model'].search([('model', '=', 'crm.journey.plan.line')], limit=1).id),
                ('res_id', '=', self.jpl_id.id),
                ('activity_type_id', '=', self.jpl_id.activity_type_id.id)
            ], limit=1)

        # Tandai aktivitas journey plan line sebagai selesai jika ditemukan
        if jpl_activity:
            jpl_activity.feedback = self.feedback
            jpl_activity._action_done()
            jpl_activity.write({
                'feedback': self.feedback,
            })

        # Jika ada opportunity, cari aktivitas spesifik untuk opportunity
        opp_activity = False
        if self.jpl_id.opportunity_id and self.jpl_id.activity_type_id:
            opp_activity = self.env['mail.activity'].search([
                ('res_model_id', '=', self.env['ir.model'].search([('model', '=', 'crm.lead')], limit=1).id),
                ('res_id', '=', self.jpl_id.opportunity_id.id),
                ('activity_type_id', '=', self.jpl_id.activity_type_id.id)
            ], limit=1)

            # Tandai aktivitas opportunity sebagai selesai jika ditemukan
            if opp_activity:
                opp_activity.feedback = self.feedback
                opp_activity._action_done()
                opp_activity.write({
                    'feedback': self.feedback,
                })

        if self.jpl_id.activity_type_id and self.jpl_id.activity_type_id.name == 'Call':
            self.jpl_id.jpl_line_state = 'finished'
            self.jpl_id.is_call = True
            return True
        return {
            'type': 'ir.actions.client',
            'tag': 'get_location_action',
            'context': {
                'active_id': self.jpl_id.id,
                'check_out': True
            }
        }