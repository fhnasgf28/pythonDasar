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
        activity_ids = []
        activity_ids.extend(self.env['mail.activity'].search([('res_model_id', '=', self.env['ir.model'].search([('model', '=', 'crm.journey.plan.line')], limit=1).id),('res_id','=',self.jpl_id.id)]))
        if self.jpl_id.opportunity_id:
            activity_ids.extend(self.env['mail.activity'].search([('res_model_id', '=', self.env['ir.model'].search([('model', '=', 'crm.lead')], limit=1).id),('res_id','=',self.jpl_id.opportunity_id.id)]))
        if activity_ids:
            for activity_id in activity_ids:
                activity_id.feedback = self.feedback
                activity_id._action_done()
                activity_id.write({
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