from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    lead_source = fields.Selection([
        ('website', 'Website'),
        ('social_media', 'Social Media'),
        ('referral', 'Referral'),
        ('other', 'Reverral')
    ])

    is_high_priority = fields.Boolean('High Priority', compute='_compute_is_high_priority', store=True)

    def create_sample_lead(self):
        return self.create({
            'name': 'Lead Baru dari Python',
            'partner_name': 'Lead Baru dari Python',
            'email_from': 'lead@python.com',
            'description': 'Lead Baru dari Python mantap wak',
            'lead_source':'website'
        })

    def action_mark_as_qualified(self):
        self.ensure_one()
        return self.write({
                'stage_id': self.env.ref('crm.stage_lead_qualified').id,
                'probability':100
            })

    @api.depends('probability', 'expected_revenue')
    def _compute_is_high_priority(self):
        for lead in self:
            if lead.probability >= 70 and lead.expected_revenue >= 1000000:
                lead.is_high_priority = True
            else:
                lead.is_high_priority = False

    def write(self, vals):
        tot_weightage = 0
        status_main = 0
        for rec in self:
            if 'stage_id' in vals:
                if rec.type == 'opportunity':
                    if rec.stage_id.is_won or rec.stage_id.is_lost:
                        if not self.env.context.get('from_wizard_restore'):
                            if rec.stage_id.id != vals['stage_id']:
                                raise ValidationError('You cannot change the stage of an opportunity to a non-won or non-lost stage.')

            if vals.get('user_id'):
                sp_recs = self.env['crm.lead.salesperson.lines'].search([('lead_id', '=', rec.id)], limit=1)
                sp_recs.write({'salesperson_id': vals.get('user_id')})

            vals_list = vals.get('salesperson_lines')
            if vals_list:
                for index, line in enumerate(vals_list):
                    if line[0] == 4:
                        stored_rec = self.env['crm.lead.salesperson.lines'].search([('id', '=', line[1])])
                        tot_weightage = tot_weightage + stored_rec.weightage
                        if stored_rec.status == 'main':
                            status_main = status_main + 1
                    else:
                        if line[0] == 0:
                            if line[2].get('weightage'):
                                tot_weightage = tot_weightage + line[2]['weightage']
                                if line[2].get('status') == 'main':
                                    status_main = status_main + 1
            res = super(CrmLead, self).write(vals)
            if rec.partner_id:
                if rec.partner_id.name == rec.partner_name:
                    fields_to_update = {}
                    if rec.partner_id.street != rec.street:
                        fields_to_update['street'] = rec.street
                    if rec.partner_id.street2 != rec.street2:
                        fields_to_update['street2'] = rec.street2
                    if rec.partner_id.city != rec.city:
                        fields_to_update['city'] = rec.city
                    if rec.partner_id.state_id != rec.state_id if rec.state_id else None:
                        fields_to_update['state_id'] = rec.state_id if rec.state_id else False
                    if rec.partner_id.zip != rec.zip:
                        fields_to_update['zip'] = rec.zip
                    if rec.partner_id.country_id != rec.country_id:
                        fields_to_update['country_id'] = rec.country_id
                    if fields_to_update:
                        rec.partner_id.write(fields_to_update)

                    if fields_to_update:
                        rec.partner_id.write(fields_to_update)

                    return res



