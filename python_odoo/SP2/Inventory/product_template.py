from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    def _raise_if_duplicate_barcode(self, exclude_current= True):
        msg = _('Barcode has been used in another product, please use a unique barcode!')
        for record in self:
            if record.barcode:
                domain_product = [('barcode', '=', record.barcode)]
                if exclude_current:
                    domain_product.append(('id', '!=', record.id))
                duplicate = self.env['product.template'].search(domain_product, limit=1)
                if duplicate:
                    raise ValidationError(msg)
                domain_multi_barcode = [('name', '=', record.barcode)]
                if exclude_current:
                    domain_multi_barcode.append(('id', '!=', record.id))
                duplicate_multi_barcode = self.env['product.template.barcode'].search(domain_multi_barcode, limit=1)
                if duplicate_multi_barcode:
                    raise ValidationError(msg)

    @api.constrains('barcode')
    def _check_barcode(self):
        for record in self:
            record._raise_if_duplicate_barcode(exclude_current= False)