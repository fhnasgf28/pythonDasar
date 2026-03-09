    def action_open_similar_leads(self):
        self.check_hold()
        name = self.name
        if self.name:
            if "'" in self.name:
                name = name.replace("'","''")
            if '"' in self.name:
                name = name.replace('"','""')
        get_leads = self.find_leads_similar(name, self.website,self.email_from,self.phone,self.mobile,my_id=self.id,)
        leads_ids = []
        for leads in get_leads:
            leads_ids.append(leads['id'])
        action = {
            'name': _('Similar Leads'),
            'view_mode': 'tree,form',
            'views': [(self.env.ref('equip3_crm_operation.crm_similar_leads_view_tree').id, 'tree'), (False, 'form')],
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', leads_ids)],
        }
        return action
