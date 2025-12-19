from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    internal_order_count = fields.Integer(string='Internal Orders', compute='_compute_order_counts')
    external_order_count = fields.Integer(string='External Orders', compute='_compute_order_counts')


    def _compute_order_counts(self):
        maintenance_order = self.env['maintenance.order']
        user_branch_ids = self.env.user.branch_ids.ids
        branch_domain_ids = user_branch_ids + ([0] if len(user_branch_ids) == 1 else [])
        company_domain = []
        if self.env.context.get('allowed_company_ids'):
            if len(self.env.companies) == 1:
                company_domain = [('company_id', '=', self.env.company.id)]
            else:
                company_domain = [('company_id', 'in', self.env.companies.ids)]
        for rec in self:
            base = [('task_check_list_ids.equipment_id', '=', rec.id), ('branch_id', 'in', branch_domain_ids)] + company_domain
            rec.internal_order_count = maintenance_order.search_count(base + [('type', '=', 'internal')])
            rec.external_order_count = maintenance_order.search_count(base + [('type', '=', 'external')])

    def view_order_external(self):
        self.ensure_one()
        action = self.env.ref('equip3_asset_fms_operation.maintenance_order_external_action').read()[0]
        action['view_mode'] = 'tree, form'
        action['domain'] = [('mo_type_code', '=', 'external'),('task_check_list_ids.equipment_id', '=', self.id)]
        ctx = action.get('context') or {}
        if isinstance(ctx, str):
            try:
                ctx = safe_eval(ctx)
            except Exception:
                ctx = {}
        else:
            ctx = dict(ctx)
        ctx.update({
            'default_mo_type_code': 'external',
            'default_task_check_list_ids': [(0, 0, {'equipment_id': self.id})]
        })
        action['context'] = ctx
        return action

    def view_order_internal(self):
        self.ensure_one()
        action = self.env.ref('equip3_asset_fms_operation.maintenance_order_internal_action').read()[0]
        action['view_mode'] = 'tree, form'
        action['domain'] = [('mo_type_code', '=', 'internal'),('task_check_list_ids.equipment_id', '=', self.id)]
        ctx = action.get('context') or {}
        if isinstance(ctx, str):
            try:
                ctx = safe_eval(ctx)
            except Exception:
                ctx = {}
        else:
            ctx = dict(ctx)
        ctx.update({
            'default_mo_type_code': 'internal',
            'default_task_check_list_ids': [(0, 0, {'equipment_id': self.id})]
        })
        action['context'] = ctx
        return action

    def action_account_asset(self):
        context = dict(self.env.context) or {}
        context.update({
            'default_equipment_id': self.id
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.asset.asset',
            'target': 'current',
            'context': context,
            'res_id': self.account_asset_id.id,
        }

    def breakdown_action(self):
        self.write({'state': 'breakdown'})

    def scrapped_action(self):
        self.write({'state': 'scrapped'})

    def _compute_work_order_count(self):
        work_order_obj = self.env['maintenance.work.order']
        work_order_ids = work_order_obj.search([('facility', '=', self.id)])
        for book in self:
            book.update({
                'wo_count': len(work_order_ids)
            })

    def _compute_is_enable_mwo_mro(self):
        for rec in self:
            try:
                module_installed = self.env['ir.module.module'].search([
                    ('name', '=', 'equip3_asset_fms_additional_config'),
                    ('state' '=', 'installed')
                ], limit=1)
                if not module_installed:
                    rec.is_enable_mwo_mro = False
                else:
                    if 'asset.config.settings' in self.env:
                        config = self.env['asset.config.settings'].search([], limit=1, order='id desc')
                        rec.is_enable_mwo_mro = config.is_enable_mwo_mro if config else False
                    else:
                        rec.is_enable_mwo_mro = False
            except Exception:
                rec.is_enable_mwo_mro = False

    def _compute_is_sale_dispose(self):
        self.is_sale_dispose = False
        is_sale_dispose = self.env['ir.config_parameter'].sudo().get_param('equip3_asset_fms_operation.is_disposable_asset')
        if is_sale_dispose == 'True':
            self.is_sale_dispose = True
        else:
            self.is_sale_dispose = False

    def _compute_assignment_history_count(self):
        for equipment in self:
            equipment.assignment_history_count = self.env['asset.employee.management.line'].search_count([('asset_id', '=', equipment.id)])

    @api.model
    def create(self, vals):
        res = super(MaintenanceEquipment, self).create(vals)
        if vals.get('account_asset_id'):
            query = "UPDATE account_asset_asset SET equipment_id=%s WHERE id=%s"
            self.env.cr.execute(query, (res.id, vals.get('account_asset_id')))
        return res