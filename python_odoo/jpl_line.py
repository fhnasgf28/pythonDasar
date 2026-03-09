from odoo import models, fields, api
from odoo.exceptions import UserError

class CrmJourneyPlanFeedbackWizard(models.TransientModel):
    _name = "crm.journey.plan.feedback.wizard"
    _description = "Feedback for Journey Plan"

    jpl_id = fields.Many2one('crm.journey.plan.line', string="Journey Plan Line")
    feedback = fields.Text("Feedback", required=True)

    def action_confirm(self):
    # Update journey plan line dengan feedback
        self.jpl_id.write({
            'feedback': self.feedback,
            'feedback_created_by': self.env.user.id
        })
        # Proses aktivitas terkait
        self._process_jpl_activity()
        self._process_opportunity_activity()
        
        # Update status berdasarkan tipe aktivitas
        return self._update_status_by_activity_type()
    
    def _process_jpl_activity(self):
        """Proses aktivitas journey plan line"""
        if not self.jpl_id.activity_type_id:
            return
            
        jpl_activity = self.env['mail.activity'].search([
            ('res_model_id', '=', self._get_model_id('crm.journey.plan.line')),
            ('res_id', '=', self.jpl_id.id),
            ('activity_type_id', '=', self.jpl_id.activity_type_id.id)
        ], limit=1)
        
        if jpl_activity:
            jpl_activity.feedback = self.feedback
            jpl_activity._action_done(feedback=self.feedback)
            jpl_activity.write({'feedback': self.feedback})
    
    def _process_opportunity_activity(self):
        """Proses aktivitas opportunity jika ada"""
        if not (self.jpl_id.opportunity_id and self.jpl_id.activity_type_id):
            return
            
        opp_activity = self.env['mail.activity'].search([
            ('res_model_id', '=', self._get_model_id('crm.lead')),
            ('res_id', '=', self.jpl_id.opportunity_id.id),
            ('activity_type_id', '=', self.jpl_id.activity_type_id.id)
        ], limit=1)
        
        if opp_activity:
            opp_activity.feedback = self.feedback
            opp_activity._action_done()
            opp_activity.write({'feedback': self.feedback})
    
    def _update_status_by_activity_type(self):
        """Update status berdasarkan tipe aktivitas"""
        activity_name = self.jpl_id.activity_type_id.name if self.jpl_id.activity_type_id else False
        
        if activity_name == 'Call':
            self.jpl_id.write({
                'jpl_line_state': 'finished',
                'is_call': True
            })
        elif activity_name == 'Meeting':
            self.jpl_id.write({
                'check_out_datetime': Datetime.now(),
                'jpl_line_state': 'finished'
            })
            return {
                'type': 'ir.actions.client',
                'tag': 'get_location_action',
                'context': {
                    'active_id': self.jpl_id.id,
                    'check_out': True
                }
            }
        else:
            self.jpl_id.jpl_line_state = 'finished'
            return True

    
    def _get_model_id(self, model_name):
        """Helper untuk mendapatkan ID model"""
        return self.env['ir.model'].search([('model', '=', model_name)], limit=1).id