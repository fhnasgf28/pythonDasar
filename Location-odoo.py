# -*- coding: utf-8 -*-
from odoo import models, fields, api
import requests

class ResPartner(models.Model):
    _inherit = 'res.partner'

    current_location = fields.Char(string="Current Location")

    @api.model
    def get_location_from_ip(self, ip_address):
        """
        Mendapatkan lokasi berdasarkan IP Address.
        """
        try:
            # Menggunakan API gratis ip-api.com
            response = requests.get(f'http://ip-api.com/json/{ip_address}')
            data = response.json()
            if data['status'] == 'success':
                city = data.get('city', '')
                region = data.get('regionName', '')
                country = data.get('country', '')
                location = f"{city}, {region}, {country}"
                return location
            return "Unknown"
        except Exception as e:
            return f"Error: {str(e)}"

    def update_current_location(self, ip_address):
        """
        Update field current_location untuk partner ini
        """
        location = self.get_location_from_ip(ip_address)
        self.current_location = location
        return location
