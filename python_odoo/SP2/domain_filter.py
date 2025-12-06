from odoo import fields, models, api, _

class ApprovalMatrix(models.AbstractModel):
    _name = 'approval.matrix.domain.filter.mixin'
    _description = 'Approval Matrix'

    @api.model
    def search(self, args, offset=0, limit=None, count=False):
        config = self.env['purchase.config.settings'].search([], limit=1, order='id desc')
        is_good_services_order = config.is_good_services_order if config else False
        if is_good_services_order:
            args = args + [('order_type', '!=', False)]
        else:
            args = args + [('order_type_comb', '!=', False)]
        return super(ApprovalMatrix, self).search(args, offset=offset, limit=limit, count=count)


