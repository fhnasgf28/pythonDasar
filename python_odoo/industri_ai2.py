def update_industries_ai(self):
    batch_size = 200
    offset = 0
    while True:
        self.env.cr.execute("""
            SELECT id, partner_name 
            FROM crm_lead 
            WHERE (industry_ai_id IS NULL OR industry_ai_processed = FALSE) 
            LIMIT %s OFFSET %s
        """, (batch_size, offset))
        leads = self.env.cr.fetchall()

        if not leads:
            break

        for lead_id, partner_name in leads:
            industry_name = self.fetch_industry_from_ai(partner_name) or "Unknown"

            # Cari industry berdasarkan nama
            self.env.cr.execute(
                "SELECT id FROM crm_industry WHERE name = %s LIMIT 1",
                (industry_name,)
            )
            industry = self.env.cr.fetchone()
            if industry:
                industry_id = industry[0]
            else:
                # Kalau industry tidak ketemu, buat baru
                new_industry = self.env['crm.industry'].create({'name': industry_name})
                industry_id = new_industry.id
            self.env.cr.execute(
                """
                UPDATE crm_lead 
                SET industry_ai_id = %s, industry_ai_processed = TRUE
                WHERE id = %s
                """, (industry_id, lead_id)
            )

        offset += batch_size
        self.env.cr.commit()
    return True