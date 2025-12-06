# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.exceptions import UserError, ValidationError
import json
import logging
import re

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
                # First check for duplicate email/phone in res.partner
                if 'email_from' in kwargs and kwargs['email_from']:
                    partner_with_same_email = request.env['res.partner'].sudo().search([
                        ('email', '=ilike', kwargs['email_from'].strip()),
                        ('is_copy', '=', False)
                    ], limit=1)
                    if partner_with_same_email:
                        return json.dumps({
                            'error': _("Email (%s) is used, Email must be unique" % kwargs['email_from'])
                        })
                
                if 'phone' in kwargs and kwargs['phone']:
                    partner_with_same_phone = request.env['res.partner'].sudo().search([
                        ('phone', '=ilike', kwargs['phone'].strip().replace(' ', '')),
                        ('is_copy', '=', False)
                    ], limit=1)
                    if partner_with_same_phone:
                        return json.dumps({
                            'error': _("Phone (%s) is used, Phone must be unique" % kwargs['phone'])
                        })
                
                # Process the form data with custom logic
                return self._handle_crm_lead_form(model_name, **kwargs)
            except UserError as e:
                print(f"UserError in CRM lead form: {e}")
                # Extract error message and return it to the frontend
                error_message = str(e)
                # Check if it's a duplicate email/phone error
                if "is used" in error_message and ("Email" in error_message or "Phone" in error_message or "Mobile" in error_message):
                    return json.dumps({
                        'error': error_message
                    })
                return json.dumps({
                    'error': error_message
                })
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
        
        # Also check in res.partner for email and phone
        partner_exists = False
        partner_message = ""
        if field == 'email_from' and value.strip():
            partner = request.env['res.partner'].sudo().search([
                ('email', '=ilike', value.strip()),
                ('is_copy', '=', False)
            ], limit=1)
            if partner:
                partner_exists = True
                partner_message = _("Email (%s) is used, Email must be unique" % value)
        
        if field == 'phone' and value.strip():
            partner = request.env['res.partner'].sudo().search([
                ('phone', '=ilike', value.strip().replace(' ', '')),
                ('is_copy', '=', False)
            ], limit=1)
            if partner:
                partner_exists = True
                partner_message = _("Phone (%s) is used, Phone must be unique" % value)
        
        return {
            'exists': count > 0 or partner_exists,
            'count': count,
            'partner_exists': partner_exists,
            'partner_message': partner_message
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
        
        # Also check in res.partner for email and phone
        partner_exists = False
        partner_message = ""
        
        if 'email_from' in values and values['email_from'] and values['email_from'].strip():
            partner = request.env['res.partner'].sudo().search([
                ('email', '=ilike', values['email_from'].strip()),
                ('is_copy', '=', False)
            ], limit=1)
            if partner:
                partner_exists = True
                partner_message = _("Email (%s) is used, Email must be unique" % values['email_from'])
        
        if not partner_exists and 'phone' in values and values['phone'] and values['phone'].strip():
            partner = request.env['res.partner'].sudo().search([
                ('phone', '=ilike', values['phone'].strip().replace(' ', '')),
                ('is_copy', '=', False)
            ], limit=1)
            if partner:
                partner_exists = True
                partner_message = _("Phone (%s) is used, Phone must be unique" % values['phone'])
        
        return {
            'exists': len(matching_leads) > 0 or partner_exists,
            'count': len(matching_leads),
            'partner_exists': partner_exists,
            'partner_message': partner_message
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
                
        except UserError as e:
            print(f"UserError in _handle_crm_lead_form: {e}")
            # Extract error message
            error_message = str(e)
            return json.dumps({
                'error': error_message
            })
        except Exception as e:
            print(f"Error in _handle_crm_lead_form: {e}")
            return json.dumps({
                'error': str(e)
            })