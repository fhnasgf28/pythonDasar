subtype_names = fields.Char(
        string="Subtype Names",
        compute="_compute_subtype_names",
        store=False
    )

    def _compute_subtype_names(self):
        for record in self:
            record.subtype_names = ', '.join(record.message_follower_ids.subtype_ids.mapped('name'))