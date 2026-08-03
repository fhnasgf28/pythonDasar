# -*- coding: utf-8 -*-
{
    'name': 'MLN KTT Leads2 Sync',
    'summary': 'Sync KTT leads2 sales team and salesperson composition into MLN Sale Orders',
    'description': 'Receives sync payload from KTT and updates/creates Sale Orders with team and salesperson split.',
    'author': 'HashMicro',
    'website': 'https://www.hashmicro.com',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['base', 'crm', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
