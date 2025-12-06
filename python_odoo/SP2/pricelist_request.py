from odoo import models, fields, api, _
from pydantic import ValidationError


class ProductPricelistRequest(models.Model):
    _inherit = 'product.pricelist.request'

    def unlink(self):
        allowed_states = ('draft', 'rejected')
        invalid = self.filtered(lambda x: x.state not in allowed_states)
        if invalid:
            msg = _("You can only delete draft or rejected pricelist request")
            if len(self) > 1 or len (invalid) >= 1:
                msg += msg + _(", check your selection")
            raise ValidationError(msg)
        return super(ProductPricelistRequest, self).unlink()