#realtime assignation
    def _assign_lead_automatically(self):
        for lead in self:
            # Hanya proses lead yang belum memiliki user_id
            if not lead.user_id:
                if lead.team_id:
                    # Cari aturan yang aktif untuk tim penjualan lead
                    rules = self.env['crm.assignment.rule'].search([
                        ('active', '=', True),
                        ('team_id', '=', lead.team_id.id)
                    ])

                    for rule in rules:
                        salesperson = None
                        if rule.rule_type == 'round_robin':
                            # Dapatkan salesperson berikutnya
                            salesperson = lead._get_next_salesperson_round_robin(rule)
                        elif rule.rule_type == 'by_workload':
                            salesperson = lead._get_salesperson_by_workload(rule)
                        if salesperson:
                            lead.write({'user_id': salesperson.id})
                            lead._log_assignment_activity()
                            lead._notify_assigned_salesperson()

    def _get_next_salesperson_round_robin(self, rule):
        if not rule.salesperson_ids:
            raise ValidationError(_("No salespersons defined in the rule."))

        # Cari salesperson berikutnya berdasarkan last_assigned_salesperson_id
        if rule.last_assigned_salesperson_id:
            salesperson_list = list(rule.salesperson_ids)
            last_index = salesperson_list.index(rule.last_assigned_salesperson_id)
            next_index = (last_index + 1) % len(salesperson_list)
            next_salesperson = salesperson_list[next_index]
        else:
            # Jika belum ada yang ditugaskan, pilih salesperson pertama
            next_salesperson = rule.salesperson_ids[0]

        # Update last_assigned_salesperson_id di aturan
        rule.write({'last_assigned_salesperson_id': next_salesperson.id})
        return next_salesperson
    def _get_salesperson_by_workload(self, rule):
        """
        Mendapatkan salesperson dengan beban kerja paling ringan berdasarkan aturan yang diberikan.
        Args:
            rule (crm.assignment.rule): Aturan penugasan yang digunakan.
        Returns:
            res.users: Salesperson yang terpilih.
        """
        if not rule.salesperson_ids:
            raise ValidationError(_("No salespersons defined in the rule."))

        # Hitung jumlah lead yang sedang ditangani oleh masing-masing salesperson
        salesperson_workloads = {}
        for salesperson in rule.salesperson_ids:
            open_leads = self.search([
                ('user_id', '=', salesperson.id),
                ('stage_id.is_won', '!=', True),
                ('team_id', '=', rule.team_id.id)
            ])
            salesperson_workloads[salesperson.id] = len(open_leads)

        # Cari salesperson dengan beban kerja paling ringan
        min_workload = min(salesperson_workloads.values())
        salesperson_id_with_min_workload = [
            salesperson_id
            for salesperson_id, workload in salesperson_workloads.items()
            if workload == min_workload
        ]

        selected_salesperson_id = random.choice(salesperson_id_with_min_workload)
        return self.env['res.users'].browse(selected_salesperson_id)

    def _notify_assigned_salesperson(self):
        for record in self:
            if not record.user_id:
                raise ValidationError(_("Cannot send notification: No user assigned."))

            message = _("You have been assigned a new lead/opportunity: %s") % record.name
            print(f"Notification sent to: {record.user_id.name}")

            # Kirim notifikasi kepada user
            record.message_notify(
                subject=_("New Lead/Opportunity Assigned"),
                body=message,
                partner_ids=[record.user_id.partner_id.id],  # Partner yang akan menerima notifikasi
                notification_type='inbox'
            )

    def _log_assignment_activity(self):
        for record in self:
            if record.user_id:
                print(f"Assigned to: {record.user_id.name}")
            else:
                print("Unassigned")

    @api.onchange('user_id')
    def _onchange_user_id(self):
        for lead in self:
            if lead.user_id:
                lead._log_assignment_activity()
                lead._notify_assigned_salesperson()

    @api.onchange('team_id')
    def _onchange_team_id(self):
        if self.team_id and not self.user_id:
            self._assign_lead_automatically()

