{
    'name': "crminternal_ktt_modifier",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'crminternal_modifier', 'sale', 'calendar', 'ks_dashboard_ninja'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/ks_crm_data.xml',
        # 'views/assets.xml',
        'views/crm_lead_lost.xml',
        'views/crm_lead.xml',
        'views/calendar_event.xml',
        'views/sale_order.xml',
        'views/crm_assignment_rule.xml',
        # 'views/res_config_settings.xml',
        'wizard/crm_lead_wizard.xml',
        # 'data/crm_stage_data.xml',
    ],
}
# -*- coding: utf-8 -*-
