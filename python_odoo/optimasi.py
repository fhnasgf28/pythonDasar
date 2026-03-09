attachment_preview_html = fields.Html(
        string='Attachment Preview',
        compute='_compute_attachment_preview_html',
        store=True,  # Penting
        sanitize=False,  # Sangat Penting,
    )

    @api.depends('activity_ids.attachment_ids')
    def _compute_attachment_preview_html(self):
        for lead in self:
            html = ''
            # Kumpulkan semua attachment dari semua activity lead ini.
            attachments = lead.activity_ids.mapped('attachment_ids')
            for attachment in attachments:
                if attachment.mimetype.startswith('image'):
                    # Tampilkan gambar dengan link ke versi full-size (lightbox)
                    preview_url = f"/web/image/{attachment.id}?width=200&height=200"  # Thumbnail
                    full_url = f"/web/image/{attachment.id}"  # Gambar full-size

                    html += f'<a href="{full_url}" data-toggle="lightbox" data-gallery="lead-gallery-{lead.id}"><img src="{preview_url}" alt="{attachment.name}" style="max-width: 180px; max-height: 180px; margin-right: 5px;"/></a>'
                else:
                    # Tampilkan ikon dan link download
                    if attachment.mimetype:
                        icon_url = f'/web/static/src/img/mimetypes/{attachment.mimetype.replace("/", "-")}.png'

                    html += f'<a href="/web/content/{attachment.id}?download=true" target="_blank"><img src="{icon_url}" title="{attachment.name}" style="width: 48px; height: 48px;"> {attachment.name}</a><br/>'
            lead.attachment_preview_html = html

    @api.depends('attachment_ids',
                 'name', 'partner_id',
                 'activity_ids.attachment_ids')
    def _compute_attachment_ids(self):
        for lead in self:
            self._cr.execute("""
                SELECT id
                FROM ir_attachment
                WHERE res_model = %s AND res_id = %s
            """, ('crm.lead', lead.id))
            attachment_ids = [row for row in self._cr.fetchall()]
            lead.attachment_ids = [(6, 0, attachment_ids)]


    def _compute_attachment_ids(self):
    for lead in self:
        direct_attachments = self.env['ir.attachment'].search([
            ('res_model', '=', 'crm.lead'),
            ('res_id', '=', lead.id),
        ])
        lead.attachment_ids = direct_attachments