from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SetWarehouse(models.Model):
    _inherit = 'sale.order'
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')

    @api.onchange('branch_id', 'company_id')
    def set_warehouse_id(self):
        for res in self:
            stock_warehouse = False
            allowed_warehouse_ids = self.env.user.warehouse_ids.ids
            if not allowed_warehouse_ids:
                raise ValidationError("You need to set up the allowed warehouse.")
            if res.company_id and res.branch_id:
                self.env.cr.execute("""
                    SELECT id
                    FROM stock_warehouse
                    WHERE company_id = %s AND branch_id = %s AND id IN (%s) AND active = True ORDER BY sequence LIMIT 1
                """) % (res.company_id.id, res.branch_id.id, str(allowed_warehouse_ids)[1:-1] if allowed_warehouse_ids else 'NULL')
                stock_warehouse = self.env.cr.fetchall()
                if not stock_warehouse:
                    self.env.cr.execute("""
                        SELECT id
                        FROM stock_warehouse
                        WHERE company_id = %s AND branch_id is null AND active = True ORDER BY sequence LIMIT 1
                    """ % (res.company_id.id))
                    stock_warehouse = self.env.cr.fetchall()
            res.destination_warehouse_id = stock_warehouse[0][0] if stock_warehouse else False
