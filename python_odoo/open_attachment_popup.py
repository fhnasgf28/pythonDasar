def action_open_attachment_popup(self):
    print('bagaimana ini farhanasegaf')
    self._compute_attachment_ids()
    self.ensure_one()
    if not self.attachment_ids:
        raise ValidationError(_('No attachment found for this lead'))
    return {
        'name': _('Attachments'),
        'type': 'ir.actions.act_window',
        'res_model': 'ir.attachment',
        'view_mode': 'kanban',
        'view_id': False,
        'domain': [('id', 'in', self.attachment_ids.ids)],
        'context': {
            'default_res_model': 'crm.lead',
            'default_res_id': self.id,
        },
        'target': 'current',
    }

# @api.depends('partner_id', 'partner_name')
    # def _compute_attachment_ids(self):
    #     print('kodingan dari attachment ini dieksekusi')
    #     for record in self:
    #         record.attachment_ids = record.message_ids.mapped('attachment_ids')
    #         # Debugging
    #         print(f"\n=== DEBUG: Record {record.id} ===")
    #         print(f"Message IDs: {record.message_ids.ids}")
    #         print(f"Attachment IDs: {record.attachment_ids.ids}")
    #         print("=============================\n")

    def check_attachment(self):
        for lead in self:
            attachments = self.env['ir.attachment'].search([
                ('res_model', '=', 'crm.lead'),
                ('res_id', '=', lead.id)
            ])
            if attachments:
                # Jika ada attachment, log info
                print("Lead ID %d has %d attachment(s).", lead.id, len(attachments))
            else:
                # Jika tidak ada attachment, log info
                print("Lead ID %d has no attachments.", lead.id)