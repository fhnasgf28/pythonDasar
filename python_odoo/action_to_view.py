def action_get_attachment_view(self):
    self.ensure_one()
    if not self.env.user.has_group('base.group_user'):
        raise ValidationError("Access Denied: You need to be a member of the 'Employee' group to access this feature.")

    domain = [
        ('res_model', '=', 'crm.lead'),
        ('res_id', '=', self.id),
        ('res_field', '=', 'activity_ids')  # Filter berdasarkan field activity_ids
    ]

    return {
        'name': 'Activities',
        'domain': domain,
        'res_model': 'mail.activity',
        'type': 'ir.actions.act_window',
        'view_id': False,
        'view_mode': 'tree,form',
        'view_type': 'form',
        'help': '''<p class="oe_view_nocontent_create">
                    Click to Log an activity
                </p>''',
        'limit': 80,
        'context': "{'default_res_model': '%s','default_res_id': %d, 'default_res_field': 'activity_ids'}" % (
            'crm.lead', self.id)
    }