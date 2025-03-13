
@api.onchange('client', 'lead_id')
    def _onchange_client_or_lead(self):
        """Mengisi field berdasarkan client atau lead_id."""
        if self.client:
            self.module_ids = self.client.module_ids if hasattr(self.client, 'module_ids') else False
            self.industry_id = self.client.industry_id if hasattr(self.client, 'industry_id') else False
            self.background = self.client.description if hasattr(self.client, 'description') else False
        elif self.lead_id:
            # Fallback dari lead_id (crm.lead) jika client kosong
            self.module_ids = self.lead_id.modules_ids if hasattr(self.lead_id, 'modules_ids') else False
            self.industry_id = self.lead_id.industry_ai if hasattr(self.lead_id, 'industry_ai') else False
            self.background = self.lead_id.description

def _get_won_record(self, model_name):
    """ Method Helper: Mengambil record yang sudah stage 'Won' dari model yang diberikan """
    return self.env[model_name].search([('stage_id', '=', 'won')], limit=1)


@api.depends('client')
def _compute_client(self):
    won_lead = self._get_won_record('crm.lead')
    for record in self:
        record.client = won_lead.partner_name if won_lead.partner_name else False
        record.background = won_lead.description if won_lead.description else False


@api.depends('module_ids')
def _compute_modules(self):
    won_modules = self._get_won_record('crm.lead')
    for record in self:
        record.module_ids = [(6, 0, won_modules.ids)]


@api.depends('module_ids')
def _compute_industry(self):
    won_industry = self._get_won_record('crm.lead')
    for record in self:
        record.industry_id = won_industry.id if won_industry else False

    def _get_won_partners_domain(self):
        won_partners = self.env['crm.lead'].search([('stage_id', '=', 'won')]).mapped('partner_id.id')
        return [('id', 'in', won_partners)]

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            # Cari lead yang terkait dengan partner dan stage_id = 'won'
            lead = self.env['crm.lead'].search([
                ('partner_id', '=', self.partner_id.id),
                ('stage_id', '=', 'won')
            ], limit=1)

            if lead:
                self.background = lead.description or ""
                self.module_ids = [(6, 0, lead.module_ids.ids)]
                self.industry_id = lead.industry_id.id if lead.industry_id else False
            else:
                self.background = ""
                self.module_ids = [(5,)]
                self.industry_id = False