@api.depends('website', 'phone', 'email_from', 'mobile')
    def _compute_is_similar(self):
        for i in self:
            is_similar = False
            similar_leads_count = 0
            i.is_similar = is_similar
            i.similar_leads_count = similar_leads_count