from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Menambahkan field baru untuk menyimpan harga per-unit yang telah dihitung
    unit_price = fields.Float(string='Unit Price', compute='_compute_unit_price', store=True)

    @api.depends('list_price', 'standard_price')
    def _compute_unit_price(self):
        for product in self:
            # Sebagai contoh, kita bisa menghitung harga per unit berdasarkan harga jual dan harga cost
            # Misalnya unit_price hanya setengah dari harga jual dan cost
            product.unit_price = (product.list_price + product.standard_price) / 2
