from odoo import fields, models, _ 

class CrmLostReason(models.Model):
    _name = 'crm.lost.reason'
    _description = 'Alasan Kehilangan Peluang'

    name = fields.Char('Description', required=True)
    active = fields.Boolean('Active', default=True)
    leads_count = fields.Integer('Leads Count', compute='_compute_leads_count')

    def _compute_leads_count(self):
        lead_data = self.env['crm.lead'].with_context(active_test=False)._read_group(
            [('lost_reason_id', '!=', False)], ['lost_reason_id'], ['lost_reason_id']
        )