from datetime import timedelta

from odoo import models, fields, api,_

class modulEquip(models.Model):
    _inherit = 'maintenance.equipment'

    @api.depends('important_documents_line')
    def _compute_total_expired_documents(self):
        for rec in self:
            total_expired = 0
            rec.expired_type = False
            if rec.important_documents_line:
                for line in rec.important_documents_line:
                    if line.expiry_date < fields.Date.today() or line.expiry_date - timedelta(days=line.alert_notif) < fields.Date.today():
                        total_expired += 1

            expired_types = [x.expired_type for x in rec.important_documents_line if x]
            if 'expired' in expired_types and 'expired_soon' in expired_types:
                rec.expired_type = 'both'
                rec.color = 1
            elif 'expired' in expired_types:
                rec.expired_type = 'expired'
                rec.color = 1
            elif 'soon' in expired_types:
                rec.expired_type = 'soon'
                rec.color = 3
            rec.total_expired_document = total_expired

    def _get_product_domain(self):
        user = self.env.user
        EquipmentCategory = self.env['maintenance.equipment.category']
        user_categories = EquipmentCategory.search([
            ('pic_ids', 'in', user.id)
        ])
        unassigned_categories = EquipmentCategory.search([
            ('pic_ids', '=', False)
        ])
        allowed_category_ids = user_categories.ids + unassigned_categories.ids
        domain = [('type', '=', 'asset')]
        if allowed_category_ids:
            domain.append(('asset_control_category', 'in', allowed_category_ids))
        return domain