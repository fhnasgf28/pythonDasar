{
    'name': 'AI Assistant',
    'version': '16.0.1.0.0',
    'summary': 'AI Assistant Integration with Odoo',
    'description': """
        This module integrates AI capabilities into Odoo.
        Features:
        - Text generation using AI
        - AI-powered suggestions
        - Customizable AI settings
    """,
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/ai_assistant_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
