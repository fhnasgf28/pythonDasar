def action_feedback_schedule_next(self, feedback=False, attachment_ids=None):
    attachment_ids = attachment_ids or []

    # Simpan attachment ke log
    if attachment_ids:
        for attachment_id in attachment_ids:
            self.env['mail.message'].create({
                'body': f'Attachment uploaded: {attachment_id}',
                'model': 'crm.lead',
                'res_id': self.res_id,
                'message_type': 'comment',
                'subtype_id': self.env.ref('mail.mt_comment').id,
            })

    activity_type_id = self.activity_type_id.id if self.activity_type_id else False
    date_deadline = self.date_deadline or False
    ctx = dict(
        self.env.context.copy(),
        default_previous_activity_type_id=activity_type_id,
        activity_previous_deadline=date_deadline,
        default_res_id=self.res_id,
        default_res_model=self.res_model,
    )

    messages, next_activities = self._action_done(feedback=feedback)

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