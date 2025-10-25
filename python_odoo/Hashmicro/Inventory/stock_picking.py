from odoo import models, fields, api
import json

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    @api.model
    def _default_branch(self):
        default_branch_id = self.env.context.get('default_branch_id', False)
        if default_branch_id:
            return default_branch_id
        return self.env.company_branches[0].id if len(self.env.company_branches) == 1 else False

    @api.model
    def _domain_branch_warehouse(self):
        return [('branch_id',  'in', self.env.branches.ids), ('company_id', '=', self.env.company.id)]

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        domain  = domain or []
        domain.extend(['|', ('branch_id', '=', False), ('branch_id', 'in', self.env.branches.ids)])
        return super(StockPicking, self).search_read(domain, fields, offset, limit, order)

    @api.depends('location_id', 'location_dest_id')
    def _compute_filter_picking_type(self):
        self.filter_operation_picking_type = json.dumps([])
        for record in self:
            if self.env.context.get('picking_type_code') == 'outgoing':
                domain = [('code', '=', 'outgoing')]
            elif self.env.context.get('picking_type_code') == 'incoming':
                domain = [('code', '=', 'incoming')]
            elif self.env.context.get('picking_type_code') == 'internal':
                domain = [('code', '=', 'internal')]
            else:
                domain = []
            picking_types = self.env['stock.picking.type'].search(domain)
            record.filter_operation_picking_type = json.dumps([('id', 'in', picking_types.ids)])

    @api.depends('create_date', 'date_done')
    def _compute_lead_time(self):
        for rec in self:
            if rec.create_date and rec.date_done:
                diff_time = rec.date_done - rec.create_date
                days = diff_time.days
                hours, remainder = divmod(diff_time.seconds, 3600)
                minutes, _ = divmod(remainder, 60)

                parts = []
                if days:
                    parts.append(f"{days} Days")
                if hours:
                    parts.append(f"{hours} Hours")
                if minutes:
                    parts.append(f"{minutes} Minutes")
                rec.lead_time = ' '.join(parts)
            else:
                rec.lead_time = ""

    def _get_journal(self):
        for rec in self:
            account_move =  self.env['account.move'].search([('ref', 'ilike', rec.name)])
            if account_move:
                rec.journal_button = True
            else:
                rec.journal_button = False

