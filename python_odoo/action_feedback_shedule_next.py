def action_feedback_schedule_next(self, feedback=False, attachment_ids=None):
    if not self.exists():
        return {'warning': _('Error: This activity no longer exists.')}

    activity_type_id = self.activity_type_id.id if self.activity_type_id else False
    date_deadline = self.date_deadline or False
    ctx = dict(
        self.env.context.copy(),
        default_previous_activity_type_id=activity_type_id,
        activity_previous_deadline=date_deadline,
        default_res_id=self.res_id,
        default_res_model=self.res_model,
    )

    if not self.res_id or not self.res_model:
        return {'warning': _('Error: CRM Lead ID is missing.')}

    # Selesaikan aktivitas
    messages, next_activities = self._action_done(feedback=feedback)

    # Simpan attachments ke CRM Lead dan tambahkan log
    if attachment_ids:
        attachments = self.env['ir.attachment'].browse(attachment_ids)
        attachments.write({'res_id': self.res_id, 'res_model': self.res_model})

        lead = self.env['crm.lead'].browse(self.res_id)
        if lead.exists():
            lead.message_post(
                body=_("Uploaded files: %s") % ', '.join(attachments.mapped('name')),
                attachment_ids=attachment_ids
            )

    if next_activities:
        return False

    return {
        'name': _('Schedule an Activity'),
        'context': ctx,
        'view_mode': 'form',
        'res_model': 'mail.activity',
        'views': [(False, 'form')],
        'type': 'ir.actions.act_window',
        'target': 'new',
    }