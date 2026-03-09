@api.depends('branch_id', 'company_id')
def compute_allowed_partner_ids(self):
    print("apakah inibagaiamana jadinya nih kia")
    for record in self:
        # Ambil semua vendor yang state-nya approved dan supplier_rank > 0
        approved_vendors = self.env['res.partner'].search([('state', '=', 'approved'), ('supplier_rank', '>', 0)])
        record.allowed_partner_ids = approved_vendors