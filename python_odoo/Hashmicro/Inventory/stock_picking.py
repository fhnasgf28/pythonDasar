from email.policy import default
from odoo.exceptions import ValidationError

from odoo import models, fields, api, _
import json

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    driver_name = fields.Char(string="Driver Name")
    vehicle_plate = fields.Char(string="Vehicle Plate")
    is_urgent = fields.Boolean(string="Is Urgent", default=False)


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

    @api.constrains('is_urgent', 'driver_name')
    def _check_driver_info(self):
        for rec in self:
            if rec.driver_name and not rec.driver_name:
                raise ValidationError(_("Driver name is required for urgent picking."))

    @api.onchange('partner_id')
    def get_partner_location(self):
        context = dict(self.env.context)
        if context.get('picking_type_code') == 'incoming':
            self.location_dest_id = self.partner_id.preferred_location.id
        if context.get('picking_type_code') == 'outgoing':
            self.location_id = self.partner_id.preferred_location.id

    # def action_put_in_pack(self):
    #     self.ensure_one()
    #     if self.state not in ('done', 'cancel'):
    #         picking_move_lines = self.move_line_ids
    #         if (
    #             not self.picking_type_id.show_reserved
    #             and not self.immediate_transfer
    #             and not self.env.context.get('barcode_view')
    #         ):
    #             picking_move_lines = self.move_line_nosugges_ids
    #         move_line_ids = picking_move_lines.filtered(lambda ml:)
    def _get_current_user(self):
        self.current_user = False
        for e in self:
            if e.purchase_id or e.sale_id:
                e.current_user = True
                break
            else:
                if e.env.user.id == e.user_id.id:
                    e.current_user = True
                else:
                    e.current_user = False

    def _build_product_domain(self, barcode):
        company = self.env.company
        barcode_type = company.sh_stock_barcode_mobile_type
        if self._is_lot_serial_scan_scenario():
            lot = self.env['stock.production.lot'].search([('name', '=', barcode)], limit=1)
            if lot:
                return [('id', 'in', lot.product_id.ids)]
        domain_parts = {
            'barcode': ['|', ('barcode', '=', barcode), ('barcode_line_ids.name', '=', barcode)],
            'int_ref': [('default_code', '=', barcode)],
            'sh_qr_code': [('sh_qr_code', '=', barcode)],
            'all': ['|', '|', ('barcode', '=', barcode), ('default_code', '=', barcode),
                    ('barcode_line_ids.name', '=', barcode)]
        }

        if barcode_type not in domain_parts:
            self._notify_user(False, 'Incorrect Configuration', 'Invalid mobile barcode type.')
            return []
        return domain_parts[barcode_type]

    def _is_lot_serial_scan_scenario(self):
        ir_config = self.env['ir.config_paramter'].sudo()
        if self.transfer_id:
            it_barcode_type = ir_config.get_param('equip3_inventory_scanning.sh_it_mobile_barcode_type', 'sku')
            if it_barcode_type == 'lot_serial':
                return True
        if self.picking_type_code == 'outgoing' or self.is_transfer_out:
            stock_barcode_type = ir_config.get_param('equip3_inventory_scanning.sh_stock_mobile_barcode_type', 'sku'
                                                     )
            if stock_barcode_type ==  'lot_serial':
                return  True
            return False

    def _get_previous_moves_delivered(self, picking):
        result = {}
        for picking in self:
            is_pack = 'PACK' in picking.name
            is_out_3step = (
                picking.picking_type_code == 'outgoing'
                and 'Output' in (picking.locationn_id.display_name or '')
            )
            if is_pack:
                search_pattern = 'PICK'
                step_name = 'PICK'
            elif is_out_3step:
                search_pattern = 'PACK'
                step_name = 'PACK'
            else:
                continue

            previous_pickings = self.env['stock.picking'].search([
                ('name', 'ilike', search_pattern),
                ('origin', '=', picking.origin),
                ('state', '=', 'done'),
            ])
            for previous_picking in previous_pickings:
                for move in previous_picking.move_ids_without_package:
                    if move.quantity_done > 0:
                        result[move.product_id.id] = result.get(move.product_id.id, 0)  + move.quantity_done

            return result

    def _reset_sequence(self):
        for rec in self:
            current_sequence = 1
            for line in rec.move_ids_without_package:
                line.sequence = current_sequence
                current_sequence += 1
            current_sequence = 1
            for line in rec.move_line_ids_without_package:
                line.move_line_sequence = current_sequence
                current_sequence += 1

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(StockPicking, self).onchange_partner_id()
        self._compute_is_mba_on_transfer_operations()
        return res

    def _compute_is_mba_on_transfer_operations(self):
        is_mbs_on_transfer_operations = self.env['ir.config_parameter'].sudo().get_param('is_mbs_on_transfer_operation', False)
        for record in self:
            record.is_mbs_on_transfer_operation = is_mbs_on_transfer_operations


    def action_serialize(self):
        self.ensure_one()
        if self.env.context.get('skip_serializer', False):
            for move in self.move_lines.filtered(lambda o:o.product_id._is_auto() and o._get_fullfillment_serialize() < 100):
                move._generate_serial_number()
                self.action_assign()
                return True

    def action_assign(self):
        self.ensure_one()
        res = super(StockPicking, self).action_assign()
        if self.transfer_id and self.is_transfer_in:
            picking_id = self.env['stock.picking'].search(
                [('transfer_id', '=', self.transfer_id.id), ('is_transfer_out', '=', True), ('state','=', 'done')]
            )
            if not picking_id:
                raise Warning (
                    "You can only validate Operation IN if the Operation OUT is validated")

        return res

    def _check_product_limit(self):
        self._check_limits(
            picking_type_code='incoming',
            limit_type_attrs='product_limit',
            min_qty_attr = 'min_val',
            max_qty_attr='max_val',
            action_verb='received'
        )

    def _check_delivery_limits(self):
                self._check_limits(
            picking_type_code='outgoing',
            limit_type_attrs='delivery_limit',
            min_qty_attr= 'delivery_limit_min_val',
            max_qty_attr='delivery_limit_max_val',
            action_verb='delivered'
        )

    def _check_missing_account_itr(self):
        # is_interwarehouse_transfer_journal = eval(self.env['ir.config_parameter'].get_param('interwarehouse_transfer_journal', 'False'))
        is_interwarehouse_transfer_journal = self.env['inventory.config.settings'].search([],
                                                                                          limit=1).interwarehouse_transfer_journal
        if not is_interwarehouse_transfer_journal:
            return

        for rec in self:
            if rec.transfer_id:
                for line in rec.move_ids_without_package:
                    if line.product_id.valuation == 'real_time' and not line.product_id.categ_id.stock_transfer_transit_account_id:
                        raise Warning(
                            _('Please set up stock transfer transit account in product category for category {line.product_id.categ_id.display_name}'))

    def _assign_analytic_groups(self):
        for picking in self:
            picking.move_ids_without_package.analytic_account_group_ids = [
                (6, 0, picking.analytic_account_group_ids.ids)]

    @api.onchange('analytic_account_group_ids')
    def _onchange_assign_analytic_groups(self):
        for picking in self:
            picking.move_ids_without_package.update({
                'analytic_account_group_ids': [(6, 0, picking.analytic_account_group_ids.ids)]
            })

    def action_view_purchase_request_picking(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.request',
            'name': 'Purchase Request',
            'domain': [('picking_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context':  {'create':0}
        }


