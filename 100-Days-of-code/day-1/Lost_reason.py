from odoo import fields, models, _
from odoo.exceptions import ValidationError


class LostReason(models.Model):
    _inherit = "crm.lost.reason"

    def unlink(self):
        approval_ids = self.ids

        # Cek di partner
        self.env.cr.execute("""
            SELECT lost_reason
            FROM crm_lead
            WHERE lost_reason = ANY(%s)
        """, [approval_ids])
        used_ids = {row[0] for row in self.env.cr.fetchall()}

        if used_ids:
            raise ValidationError(_("This record cannot be deleted because it is already linked to existing transactions."))

        return super().unlink()
