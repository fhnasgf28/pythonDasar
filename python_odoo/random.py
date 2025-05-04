@api.depends('is_a_subcontracting', 'subcon_production_id', 'company_id')
    def _compute_allowed_partners(self):
        domain = self._domain_partner()
        partner_sudo = self.env['res.partner'].sudo()
        partner_ids = partner_sudo.search(domain)
        for record in self:
            allowed_partner_ids = partner_ids.ids
            if record.is_a_subcontracting:
                subcon_partner_ids = record.subcon_production_id.bom_id.subcontractor_ids.ids
                allowed_partner_ids = partner_ids.filtered(lambda p: p.id in subcon_partner_ids).ids
            record.allowed_partner_ids = [(6, 0, allowed_partner_ids)]