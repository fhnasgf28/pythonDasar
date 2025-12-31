{
    'name': "IT Service Request",
    'summary': """
        Modul untuk mengelola permintaan layanan IT dari karyawan.""",
    'description': """
        Modul kustom Odoo ini memungkinkan karyawan untuk membuat permintaan layanan IT,
        dan departemen IT untuk mengelola alur kerja dari penugasan hingga penyelesaian.
    """,
    'author': "Nama Anda",
    'website': "http://www.contohperusahaan.com",
    'category': 'Services/IT',
    'version': '1.0',
    'depends': ['base'], # Modul dasar yang dibutuhkan
    'data': [
        'security/it_layanan_groups.xml',
        'security/ir.model.access.csv',
        'views/it_service_request_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}