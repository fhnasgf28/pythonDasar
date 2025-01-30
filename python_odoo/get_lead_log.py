def get_lead_logs(self, lead_id=None):
    print('Fetching lead logs...')
    if not lead_id:
        raise UserError("Lead ID is required.")
    lead = self.browse(lead_id)
    if not lead.exists():
        raise UserError("Lead with ID %s does not exist." % lead_id)
    return lead.message_ids