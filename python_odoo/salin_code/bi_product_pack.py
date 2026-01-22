from odoo import models, api, _, fields
from odoo.exceptions import ValidationError

class BiProductPack(models.Model):
    _name = 'bi.product.pack'
    _description = "product pack line"

    bi_product_template = fields.Many2one('product.template', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', required=True)
    proportion = fields.Float(string='Proportion(%)')
    product_template = fields.Many2one('product.template', string='Product', domain=[('type', '=', 'product')])

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

    @api.onchange('product_template')
    def _onchange_product_template(self):
        if self.product_template:
            self.product_id = self.env['product.product'].search([('product_tmpl_id', '=', self.product_template.id)], limit=1)

    @api.model
    def _initial_stock_bundle(self):
        parent_bundles = self.env['product.product'].search(
            [('is_pack', '=', True), ('bi_pack_ids', '!=', False)]
        )
        warehouses = self.env['stock.warehouse'].search([])
        existing_records = self.env['bundle.stock'].search_read(

        )