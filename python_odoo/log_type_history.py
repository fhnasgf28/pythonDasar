log_history = fields.Html(string='Log History', compute='_compute_log_history', store=False)

    @api.depends('message_ids.date', 'message_ids.body')
    def _compute_log_history(self):
        for lead in self:
            messages = self.env['mail.message'].search([
                ('model', '=', 'crm.lead'),
                ('res_id', '=', lead.id)
            ], order='date DESC')

            log_content = """
                    <style>
                        .log-container {
                            font-family: Arial, sans-serif;
                            background-color: #f9f9f9;
                            border: 1px solid #ddd;
                            border-radius: 8px;
                            padding: 15px;
                            max-height: 300px;
                            overflow-y: auto;
                        }
                        .log-item {
                            margin-bottom: 10px;
                            padding: 10px;
                            background-color: #fff;
                            border: 1px solid #eee;
                            border-radius: 4px;
                            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                        }
                        .log-date {
                            font-size: 12px;
                            color: #888;
                            margin-bottom: 5px;
                        }
                        .log-body {
                            font-size: 14px;
                            color: #333;
                        }
                    </style>
                    <div class="log-container">
                    """

            if messages:
                for msg in messages:
                    log_content += f"""
                            <div class="log-item">
                                <div class="log-date">{msg.date}</div>
                                <div class="log-body">{html2plaintext(msg.body)}</div>
                            </div>
                            """
            else:
                log_content += "<div class='log-item'>Tidak ada log.</div>"

            log_content += "</div>"
            lead.log_history = log_content

