# Di dalam file Python model 'sale.order' Anda

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # ... field-field Anda yang lain, termasuk field untuk approval matrix ...

    def action_multi_confirm_or_approve(self):
        # 'self' adalah 'records' yang dikirim dari server action
        if not self:
            raise ValidationError("Please select a sale order first!")

        config = self.env['sales.config.settings'].search([], limit=1, order="id desc")
        approval_matrix = config.is_customer_approval_matrix

        # ======================================================================
        # ALUR A: JIKA APPROVAL MATRIX AKTIF (True)
        # ======================================================================
        if approval_matrix:
            _logger.info("Alur Approval Matrix Aktif...")
            allowed_state = 'waiting_for_sale_order_approval'  # Sesuaikan nama state jika perlu
            orders_to_confirm = self.env['sale.order']  # Menampung SO yang siap di-confirm

            for record in self:
                # POIN #1: Cek state, jika salah langsung hentikan
                if record.state != allowed_state:
                    raise ValidationError(
                        "Can't approve quotation when state not in waiting for sale order approval"
                    )

                # POIN #2: Cek keamanan, pastikan user adalah approver yang ditunjuk
                # Asumsi: Anda punya field 'next_approver_user_id'
                if record.next_approver_user_id != self.env.user:
                    raise ValidationError(
                        "You are not the current approver for quotation %s." % (record.name)
                    )

                # --- Proses Approval ---
                # Tambahkan user saat ini ke daftar yang sudah approve
                # Asumsi: Anda punya field Many2many 'approved_user_ids'
                record.write({'approved_user_ids': [(4, self.env.user.id)]})
                _logger.info("User %s has approved order %s.", self.env.user.name, record.name)

                # POIN #3: Cek apakah ini approval terakhir
                # Asumsi: Anda punya field Many2many 'approver_user_ids' (semua yg harus approve)
                required_approvers = set(record.approver_user_ids.ids)
                current_approvers = set(record.approved_user_ids.ids)

                if required_approvers and required_approvers == current_approvers:
                    _logger.info("Final approval reached for %s. Adding to confirmation queue.", record.name)
                    orders_to_confirm += record
                # else:
                # Opsional: Jika belum selesai, panggil method untuk mencari approver selanjutnya
                # record._find_next_approver()

            # Setelah loop selesai, konfirmasi semua SO yang sudah mencapai approval final
            if orders_to_confirm:
                _logger.info("Auto-confirming %s orders.", len(orders_to_confirm))
                orders_to_confirm.action_confirm()

        # ======================================================================
        # ALUR B: JIKA APPROVAL MATRIX NONAKTIF (False)
        # ======================================================================
        else:
            _logger.info("Alur Konfirmasi Standar (Approval Matrix Nonaktif)...")
            allowed_states = ['draft', 'sent']

            for record in self:
                if record.state not in allowed_states:
                    raise ValidationError(
                        "Can't confirm quotation when state is not 'Quotation' or 'Quotation Sent'. "
                        "Please check the status of order %s." % (record.name)
                    )

            self.action_confirm()
            _logger.info("Berhasil menjalankan method confirm untuk %s record(s).", len(self))

        return True