import logging
from odoo import models, fields, api,_
_logger = logging.getLogger(__name__)
from odoo.exceptions import ValidationError

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    is_lost_leads = fields.Boolean(string="Is Lost", default=False)
    lost_reason_id = fields.Many2one('crm.lost.reason', string='Lost Reason')
    description = fields.Text(string='Description')
    country_id = fields.Many2one('res.country', string='Country', required=True)
    approver_user_id = fields.Many2one('res.users', string='Approver', default=lambda self: self.env.user)
    state_lost_leads = fields.Selection([
        ('to_approve', 'To Approve'),
        ('approved', 'Approved')
    ], string="State", default='to_approve')

    def action_approve_lost(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.write(
                {'state_lost_leads': 'approved'},
            )
        else:
            raise ValidationError(_("You do not have access to perform approval."))

    @api.model
    def update_leads_quotation_count(self):
        """
        Updates the quotation_count field for all leads.
        Only considers sale orders in states 'draft' or 'send'.
        """
        query = """
            UPDATE crm_lead cl
            SET quotation_counts = (
                SELECT COUNT(so.id)
                FROM sale_order so
                WHERE so.opportunity_id = cl.id
                AND so.state IN ('draft', 'send')
            )
            WHERE cl.id IN (
                SELECT id FROM crm_lead WHERE quotation_counts = 0
            );
        """
        self.env.cr.execute(query)
        self.env.cr.commit()

    def find_leads_similar(self, name,website='',email_from='',phone='',mobile='',partner_name='',my_id=False):
        where_params = ''
        id_params = ''
        query = """
            SELECT id, name
            FROM crm_lead
            WHERE lower(name) = lower('{}'){}
        """
        if partner_name:
            where_params += " or name = '{}'".format(name)
        if email_from:
            where_params += " or email_from = '{}'".format(email_from)
        if phone:
            where_params += " or phone = '{}'".format(phone)
        if mobile:
            where_params += " or mobile = '{}'".format(mobile)
        if partner_name:
            where_params += " or partner_name = '{}'".format(partner_name)
        if my_id:
            id_params += " and id != {}".format(my_id)
        self.env.cr.execute(query.format(name, where_params, id_params))
        query_result = self.env.cr.dictfetchall()
        return query_result

    def _compute_activity_count(self):
        for res in self:
            self.env.cr.execute("""
                SELECT COUNT(*) FROM res_mail_activity
                WHERE res_id = %s
            """, (res.id,))
            res.activity_count = self.env.cr.fetchone()[0]

    def _compute_meeting_count(self):
        if not self.ids:
            return

        opportunity_ids = tuple(self.ids)
        self.env.cr.execute("""
            SELECT opportunity_id, COUNT(*) FROM
            calendar_event 
            WHERE state IN ('meeting', 'done') AND opportunity_id IN %s
            GROUP BY opportunity_id
        """, (opportunity_ids,))
        # hasil query dikonversi menjadi dictionary
        meeting_counts = dict(self.env.cr.fetchall())

        for res in self:
            count = meeting_counts.get(res.id, 0)
            res.sudo().meeting_count = count
            res.sudo().meeting_count_2 = count
        # panggil methode lainnya
        self.compute_bd_intern()
        self._compute_check_group_user()

    def _compute_user_id(self):
        query = """
            UPDATE crm_lead 
            SET user_id = %s
            WHERE user_id IS NULL
        """
        self.env.cr.execute(query, (2,))

    def schedule_activity(self):
        for res in self:
            context = dict(self.env.context) or {}
            self.env.cr.execute("""
                SELECT id FROM ir_model WHERE model = %s LIMIT 1
            """, ('crm.lead',))
            result = self.env.cr.fetchone()
            model_id = result[0] if result else False

            if model_id:
                context.update({'res_model_id': model_id})
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'Schedule Activity',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'mail.activity',
                    'context': context,
                    'target': 'new',
                }

    @api.depends('order_ids.state', 'order_ids.currency_id', 'order_ids.amount_untaxed', 'order_ids.date_order',
                 'order_ids.company_id')
    def _compute_sale_data(self):
        res = super(CRMLead, self)._compute_sale_data()
        quotation_amount_model = self.env['quotation.amount']
        for rec in self:
            order_ids = [order.id for order in rec.order_ids]
            if order_ids:
                self.env.cr.execute("""
                        SELECT order_id
                        FROM quotation_amount
                        WHERE order_id in %s
                        """, (tuple(order_ids),))

                existing_order_ids = {row[0] for row in self.env.cr.fetchall()}
                new_order_ids = set(order_ids) - existing_order_ids

                if new_order_ids:
                    quotation_amount_model.create([
                        {'order_id': order_id} for order_id in new_order_ids
                    ])

            rec.sudo().quotation_counts = rec.quotation_count
        return res

class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'
    _description = 'Get Lost Reason'

    description = fields.Text(string='Description', required=True)

    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        if not self.lost_reason_id or not self.description:
            raise ValidationError("Please fill in both the lost reason and description before applying.")

        for lead in leads:
            lead.write({
                'lost_reason_id': self.lost_reason_id.id,
                'description': self.description,
                'is_lost_leads': True,
            })

        return leads.action_set_lost(lost_reason=self.lost_reason_id.id)
