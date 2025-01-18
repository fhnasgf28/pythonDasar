def unlink(self):
    print("unlink")
    for rec in self:
        print(f"Processing record ID: {rec.id}")

        # Cari semua record terkait
        res_acts = self.env['res.mail.activity'].search([('act_id', '=', rec.id)])
        print(f"Found {len(res_acts)} activities for record ID {rec.id}")

        # Filter hanya record dengan kondisi tertentu
        res_acts_to_process = res_acts.filtered(lambda r: r.state != 'done')
        print(f"{len(res_acts_to_process)} activities to process for record ID {rec.id}")

        # Iterasi dan proses setiap record yang memenuhi kondisi
        for res_act in res_acts:
            if res_act in res_acts_to_process:
                print(f"Processing activity ID: {res_act.id}, State: {res_act.state}")
                res_act.state = 'cancel'
                if res_act.res_id:
                    print(f"Updating related record (res_id: {res_act.res_id.id}) for activity ID: {res_act.id}")
                    res_act.res_id.set_due_date_and_missed()
            else:
                print(f"Skipping activity ID: {res_act.id}, State: {res_act.state}")

    return super(mailActivity, self).unlink()