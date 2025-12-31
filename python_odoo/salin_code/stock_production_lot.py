from odoo import models, api, fields

class stock_production_lot(models.model):
    def write(self, vals):
        res = super(stock_production_lot, self).write(vals)
        if self.context.get('auto_confirm_import'):
            self._confirm_import(self.ids)
        
        return res
