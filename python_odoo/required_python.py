new_potential = fields.Selection([
        ("potential", "Potential"),
        ("not_potential", "Not Potential"),
        ("not_updated", "Not Updated")
    ], string='Potential', compute='_compute_field', store=True, required=True)
    latest_follow_up_date = fields.Date("Latest Follow Up Date",required=True)
    remark = fields.Text("Latest Update",required=True)
    cannot_be_quoted = fields.Boolean(string='Cannot be Quoted', compute='_compute_field', store=True,required=True)
    quotation = fields.Selection([
        ("sent", "Sent"),
        ("not_sent", "Not Sent"),
    ], string="Quotation Sent Status", compute='_compute_field', store=True,required=True)
    challenges = fields.Text("Challenges", required=True)
    final_quotation = fields.Many2one('quotation.amount', string="Final Quotation Amount", compute='_compute_field', store=True,required=True)
