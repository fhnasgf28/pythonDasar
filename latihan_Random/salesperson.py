
        def _domain_salesperson_id(self):
        print("domain_salesperson_id", self.env.companies)
        group = self.env.ref('equip3_crm_masterdata.group_team_member')
        print("company", self.env.companies)
        # Filter users based on selected companies
        if self.env.context.get('allowed_company_ids'):
            print("allowed_company_ids", self.env.context.get('allowed_company_ids'))
            if len(self.env.companies) == 1:
                # Single company selected: filter by exact company
                return [
                    ('groups_id', 'in', group.ids),
                    ('company_ids', 'in', [self.env.company.id])
                ]
                print("company_ids", [self.env.company.id])
            else:
                # Multiple companies selected: filter by companies in selection
                return [
                    ('groups_id', 'in', group.ids),
                    ('company_ids', 'in', self.env.companies.ids)
                ]
        
        # Default behavior if no company filtering context
        return [('groups_id', 'in', group.ids)]
