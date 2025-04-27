allowed_partner_ids = fields.Many2many('res.partner', compute='compute_allowed_partner_ids', store=True)
filter_destination_warehouse = fields.Char(string="Filter Destination Warehouse", compute='_compute_filter_destination',
                                           store=False)

@api.depends('company_id', 'branch_id', 'partner_id')
def compute_allowed_partner_ids(self):
    print("gimana nih kondisi kamu saaat ini")
    for rec in self:
        rec.allowed_partner_ids = self.env['res.partner'].search([('state', '=', 'approved')])
        print("rec.allowed_partner_ids",rec.allowed_partner_ids)
