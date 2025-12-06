# -*- coding: utf-8 -*-

from odoo import models, api
from lxml import etree
import json

class PurchaseOrder(models.Model):
    """
    Mewarisi model Purchase Order untuk memodifikasi tampilan form secara dinamis.
    """
    _inherit = 'purchase.order'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        """
        Meng-override metode ini untuk menambahkan logika readonly pada field di form view.
        Tujuannya adalah membuat semua field menjadi readonly jika state bukan 'draft',
        sambil tetap mempertahankan kondisi readonly yang sudah ada.
        """
        # Panggil metode original (super) untuk mendapatkan struktur view dasar.
        res = super(PurchaseOrder, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

        # Proses ini hanya berlaku untuk 'form' view.
        if view_type == 'form':
            # Parse arsitektur view (XML) untuk dimanipulasi.
            doc = etree.XML(res['arch'])

            # Tentukan kondisi readonly baru yang ingin ditambahkan.
            # Dalam format domain Odoo, ini berarti ['field', 'operator', 'value']
            new_readonly_condition = ['state', '!=', 'draft']

            # Cari semua elemen '<field>' di dalam arsitektur view.
            for node in doc.xpath("//field"):
                # Ambil atribut 'modifiers' yang ada, defaultnya adalah string JSON kosong '{}'.
                modifiers = json.loads(node.get("modifiers", '{}'))

                # Dapatkan kondisi readonly yang sudah ada dari modifiers.
                existing_readonly = modifiers.get('readonly')

                if isinstance(existing_readonly, list):
                    # Jika sudah ada kondisi readonly dalam bentuk list (domain Odoo),
                    # gabungkan dengan kondisi baru menggunakan operator '|' (OR).
                    # Formatnya: ['|', [kondisi_lama], [kondisi_baru]]
                    # Ini akan membuat field readonly jika kondisi_lama ATAU kondisi_baru terpenuhi.
                    modifiers['readonly'] = ['|'] + [existing_readonly] + [new_readonly_condition]
                elif not existing_readonly:
                    # Jika tidak ada kondisi readonly (None, False, atau list kosong),
                    # langsung gunakan kondisi baru.
                    modifiers['readonly'] = new_readonly_condition
                # Jika existing_readonly adalah True, kita tidak melakukan apa-apa karena
                # field tersebut sudah diatur untuk selalu readonly, yang lebih kuat.

                # Setel kembali atribut 'modifiers' pada node field dengan nilai yang sudah diperbarui.
                node.set('modifiers', json.dumps(modifiers))

            # Konversi kembali struktur XML yang telah dimodifikasi menjadi string dan update arsitektur view.
            res['arch'] = etree.tostring(doc, encoding='unicode')

        return res
