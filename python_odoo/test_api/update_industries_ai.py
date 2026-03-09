def update_industries_ai(self):
    batch_size = 200
    offset = 0
    while True:
        self.env.cr.execute("""
            SELECT id, partner_name 
            FROM crm_lead 
            WHERE industry_ai IS NULL 
            LIMIT %s OFFSET %s
        """, (batch_size, offset))
        leads = self.env.cr.fetchall()

        if not leads:
            break

        for lead_id, partner_name in leads:
            if partner_name:
                industry_ai = self.fetch_industry_from_ai(partner_name) or "Unknown"
                self.env.cr.execute(
                    "UPDATE crm_lead SET industry_ai = %s WHERE id = %s",
                    (industry_ai, lead_id)
                )

        offset += batch_size
        self.env.cr.commit()
    return True