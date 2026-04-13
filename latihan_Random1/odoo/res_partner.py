from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _compute_purchase_order_count(self):
        self.purchase_order_count = 0
        if not self.env.user._has_group('purchase.group_purchase_user'):
            return
        all_partners = self.with_context(active_test=False).search_fetch(
            [('id', 'child_of', self.ids),
             ('parent_id')],
        )
        purchase_order_groups = self.env['purchase.order']._read_group(
            domain=[('partner_id', 'in', all_partners.ids)],
            groupby=['partner_id'],
        )
        self_ids = set(self.ids)
        for partner, count in purchase_order_groups:
            while partner:
                if partner.id in self_ids:
                    partner.purchase_order_count += count
                partner = partner.parent_id