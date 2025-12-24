from odoo import models, api, _
from odoo.exceptions import ValidationError

class BiProductPack(models.Model):
    _name = 'bi.product.pack'
    _description = "product pack line"

    bi_product_template = fields.Many2one('product.template', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', required=True)

    @api.constrains('product_id', 'bi_product_template')
    def _check_duplicate_product_in_pack(self):
        for line in self:
            template = line.bi_product_template

            if not template or not template.is_pack:
                continue

            duplicate_lines = template.bi_pack_ids.filtered(
                lambda l: l.product_id == line.product_id and l.id != line.id
            )
            if duplicate_lines:
                raise ValidationError(
                    _("product '%s' already exists in this bundle please choose a different product")
                    % line.product_id.display_name
                ) 