attachment_ids = fields.One2many(
        comodel_name="ir.attachment",
        inverse_name="res_id",
        domain=[("res_model", "=", "crm.lead")],
        string="Attachments"
    )

    def action_open_attachment_popup(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attachments',
            'res_model': 'crm.lead',
            'view_mode': 'form',
            'res_id': self.id,
            'view_id': self.env.ref('crminternal_ktt_modifier.view_crm_lead_attachment_form').id,
            'target': 'new',
        }