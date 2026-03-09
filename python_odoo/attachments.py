# def action_done_schedule_next(self, feedback=False, attachment_ids=None):
    #     if not self.exists():
    #         return {'warning': _('Error: This activity no longer exists.')}
    #
    #     # **Mark activity as 'done' & post message in CRM Lead**
    #     messages = self.env['mail.message']
    #
    #     # **Ambil semua attachments yang terkait dengan aktivitas**
    #     attachments = self.env['ir.attachment'].search_read([
    #         ('res_model', '=', 'mail.activity'),
    #         ('res_id', 'in', self.ids),
    #     ], ['id', 'res_id'])
    #
    #     activity_attachments = defaultdict(list)
    #     for attachment in attachments:
    #         activity_attachments[attachment['res_id']].append(attachment['id'])
    #
    #     for activity in self:
    #         record = self.env[activity.res_model].browse(activity.res_id)
    #
    #         # **Post message to CRM Lead with attachment**
    #         activity_message = record.message_post_with_view(
    #             'mail.message_activity_done',
    #             values={
    #                 'activity': activity,
    #                 'feedback': feedback,
    #                 'display_assignee': activity.user_id != self.env.user
    #             },
    #             subtype_id=self.env['ir.model.data'].xmlid_to_res_id('mail.mt_activities'),
    #             mail_activity_type_id=activity.activity_type_id.id,
    #             attachment_ids=[(4, attachment_id) for attachment_id in (attachment_ids or [])],
    #         )
    #
    #         # **Pindahkan attachment dari aktivitas ke log CRM Lead**
    #         message_attachments = self.env['ir.attachment'].browse(activity_attachments[activity.id])
    #         if message_attachments:
    #             message_attachments.write({
    #                 'res_id': activity_message.id,
    #                 'res_model': 'mail.message',
    #             })
    #             activity_message.attachment_ids = message_attachments
    #
    #         messages |= activity_message
    #
    #
    #     return self.action_feedback_schedule_next(feedback=feedback)