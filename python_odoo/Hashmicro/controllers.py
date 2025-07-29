# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
import json
import logging

_logger = logging.getLogger(__name__)

class Equip3WebsiteForm(WebsiteForm):
    """
    Extends WebsiteForm controller to handle contact form submissions
    and create CRM leads with custom logic
    """
    
    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def website_form(self, model_name, **kwargs):
        """
        Override website_form method to add custom logic for crm.lead creation
        """
        # Log the form submission for debugging
        print(f"Form submission received for model: {model_name}")
        print(f"Form data: {kwargs}")
        # If the form is for crm.lead, apply custom logic
        if model_name == 'crm.lead':
            try:
                # Process the form data with custom logic
                return self._handle_crm_lead_form(model_name, **kwargs)
            except Exception as e:
                print(f"Error processing CRM lead form: {e}")
                return json.dumps({
                    'error': _("An error occurred while processing your request.")
                })
        
        # For other models, use the standard form handling
        return super(Equip3WebsiteForm, self).website_form(model_name, **kwargs)
    
    @http.route('/contactus/check_duplicate', type='json', auth="public", website=True)
    def check_duplicate(self, field, value):
        """
        Check if a value already exists in the database for a specific field
        
        :param field: Field name to check (email_from, phone, contact_name)
        :param value: Value to check for duplicates
        :return: JSON with exists: boolean
        """
        if not field or not value or value.strip() == '':
            return {'exists': False}
        
        # Map frontend field names to model field names if needed
        field_mapping = {
            'contact_name': 'contact_name',
            'email_from': 'email_from',
            'phone': 'phone',
        }
        
        model_field = field_mapping.get(field, field)
        
        # Search for duplicates in crm.lead model
        Lead = request.env['crm.lead'].sudo()
        domain = [(model_field, '=ilike', value.strip())]
        
        # Count duplicates
        count = Lead.search_count(domain)
        
        return {
            'exists': count > 0,
            'count': count
        }
    
    @http.route('/contactus/check_all_duplicates', type='json', auth="public", website=True)
    def check_all_duplicates(self, values):
        """
        Check if multiple values already exist in the database
        
        :param values: Dictionary with field names as keys and values to check
        :return: JSON with exists: boolean and matches: list of matching records
        """
        if not values:
            return {'exists': False}
        
        # Map frontend field names to model field names if needed
        field_mapping = {
            'contact_name': 'contact_name',
            'email_from': 'email_from',
            'phone': 'phone',
        }
        
        # Build domain for search
        domain = []
        for field, value in values.items():
            if value and value.strip() != '':
                model_field = field_mapping.get(field, field)
                domain.append('|')
                domain.append((model_field, '=ilike', value.strip()))
        
        # Remove the first OR operator if it exists
        if domain and domain[0] == '|':
            domain.pop(0)
        
        if not domain:
            return {'exists': False}
        
        # Search for duplicates in crm.lead model
        Lead = request.env['crm.lead'].sudo()
        matching_leads = Lead.search(domain)
        
        return {
            'exists': len(matching_leads) > 0,
            'count': len(matching_leads)
        }
    
    def _handle_crm_lead_form(self, model_name, **kwargs):
        """
        Custom handler for crm.lead form submissions
        """
        # Check CSRF token when user is authenticated
        csrf_token = kwargs.pop('csrf_token', None)
        if request.session.uid and not request.validate_csrf(csrf_token):
            return json.dumps({
                'error': _("Session expired (invalid CSRF token)")
            })
        
        # Get the model record
        model_record = request.env['ir.model'].sudo().search([
            ('model', '=', model_name), 
            ('website_form_access', '=', True)
        ])
        
        if not model_record:
            return json.dumps({
                'error': _("The form's specified model does not exist")
            })
        
        try:
            # Extract data from the form
            data = self.extract_data(model_record, kwargs)
            
            # Add custom fields or modify existing fields
            record_data = data['record']

            record_data.update({
                'type': 'lead',
                'medium_id': request.env.ref('utm.utm_medium_website').id,
            })
            
            # Create the lead
            id_record = self.insert_record(request, model_record, record_data, data['custom'], data.get('meta'))
            
            if id_record:
                # Process attachments if any
                self.insert_attachment(model_record, id_record, data['attachments'])
                
                # Store session data
                request.session['form_builder_model_model'] = model_record.model
                request.session['form_builder_model'] = model_record.name
                request.session['form_builder_id'] = id_record
                
                # Log success
                print(f"Successfully created CRM lead with ID: {id_record}")
                
                return json.dumps({'id': id_record})
            else:
                return json.dumps({
                    'error': _("Failed to create lead")
                })
                
        except Exception as e:
            print(f"Error in _handle_crm_lead_form: {e}")
            return json.dumps({
                'error': str(e)
            })

# class MyModule(http.Controller):
#     @http.route('/my_module/my_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module/my_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module.listing', {
#             'root': '/my_module/my_module',
#             'objects': http.request.env['my_module.my_module'].search([]),
#         })

#     @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module.object', {
#             'object': obj
#         })