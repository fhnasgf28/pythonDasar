def _compute_is_similar(self):
    print('assegaffarhanassegaf')
    for i in self:
        is_similar = False
        similar_leads_count = 0
        name = i.name
        if i.name:
            if "'" in i.name:
                name = name.replace("'", "''")
            if '"' in i.name:
                name = name.replace('"', '""')
        get_leads = self.find_leads_similar(name, i.website, i.email_from, i.phone, i.mobile,
                                            partner_name=i.partner_name, my_id=i.id)
        print("get leads", get_leads)
        if len(get_leads) > 0:
            is_similar = True
            similar_leads_count = len(get_leads)
            print('ini adalah get leads', similar_leads_count)
        i.is_similar = is_similar
        i.similar_leads_count = similar_leads_count