@api.depends('message_ids.attachment_ids')
    def _compute_has_attachment(self):
        print('farhanasegf method compute has attachment ini dieksekusi')
        for record in self:
            attachments = record.message_ids.mapped('attachment_ids')
            if attachments:
                record.has_attachment = True
                # Ambil file pertama yang bisa ditampilkan sebagai gambar
                img_attachment = next((att for att in attachments if att.mimetype and 'image' in att.mimetype), None)
                record.attachment_preview = img_attachment.datas if img_attachment else False
            else:
                record.has_attachment = False
                record.attachment_preview = False