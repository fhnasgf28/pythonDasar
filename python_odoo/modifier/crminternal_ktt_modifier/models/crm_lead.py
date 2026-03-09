import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def update_leads_quotation_count(self):
        """
        Updates the quotation_count field for all leads.
        Only considers sale orders in states 'draft' or 'send'.
        """
        update_query = """
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
        # Query to fetch updated results
        check_query = """
                    SELECT id, quotation_count
                    FROM crm_lead
                    WHERE quotation_count > 0;
                """
        try:
            # Execute update query
            self.env.cr.execute(update_query)
            self.env.cr.commit()

            # Fetch updated records for debugging
            self.env.cr.execute(check_query)
            updated_leads = self.env.cr.fetchall()

            # Print updated results for debugging
            print("Updated Leads:", updated_leads)
        except Exception as e:
            print(f"Error while updating quotation count: {str(e)}")
            raise

    def find_leads_similar(self, name,website='',email_from='',phone='',mobile='',partner_name='',my_id=False):
        print("Executing find_leads_similar method in CRMLead")
        where_params = ''
        id_params = ''
        query = """
            SELECT id, name
            FROM crm_lead
            WHERE lower(name) = lower('{}'){}
        """

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

    @api.model
    def create(self, vals):
        print("Executing create method in CRMLead")
        res = super(CRMLead, self).create(vals)
        print("Executing create method in CRMLead")
        print("Parameters for find_leads_similar:", {
            "name": vals.get('name', ''),
            "mobile": vals.get('mobile', ''),
            "phone": vals.get('phone', ''),
            "website": vals.get('website', ''),
            "email_from": vals.get('email_from', ''),
            "partner_name": vals.get('partner_name', ''),
            "my_id": res.id
        })
        # Call the find_leads_similar method with correct arguments
        similar_leads = res.find_leads_similar(
            name=vals.get('name', ''),
            phone=vals.get('phone', ''),
            mobile=vals.get('mobile', ''),
            email_from=vals.get('email_from', ''),
            partner_name=vals.get('partner_name', ''),
            website=vals.get('website', ''),
            my_id=res.id
        )
        print("Similar leads found:", similar_leads)
        return res

