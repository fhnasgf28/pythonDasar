class CrmLead(models.Model):
    _inherit = 'crm.lead'

    first_meeting_date = fields.Datetime(
        string="First Meeting Date",
        compute="_compute_first_meeting_date",
        store=True,
        help="Date of the first meeting linked to this opportunity"
    )

    @api.depends('meeting_ids', 'meeting_ids.state')
    def _compute_first_meeting_date(self):
        for lead in self:
            if lead.meeting_ids:
                # Filter meetings with state 'done'
                done_meetings = lead.meeting_ids.filtered(lambda m: m.state == 'done')
                if len(done_meetings) == 1:
                    lead.first_meeting_date = done_meetings.create_date
                else:
                    lead.first_meeting_date = False
            else:
                lead.first_meeting_date = False
