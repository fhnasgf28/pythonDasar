def action_close_dialog(self):
    print('farhanasegaf kodingan ini di eksekusi')
    for activity in self:
        if not activity.res_model_id:
            activity.res_model_id = self.env['ir.model'].search([], limit=1).id

    return {'type': 'ir.actions.act_window_close'}


feedback_form = fields.Html(string="Feedback Form")
first_attachment_id = fields.Many2one(
    'ir.attachment',
    string='First Attachment',
    compute='_compute_first_attachment',
    store=True,  # Penting: Simpan hasil komputasi
)
first_attachment_is_image = fields.Boolean(
    string='Is Image',
    compute='_compute_first_attachment',
    store=True,
)
attachment_preview_html = fields.Html(
    string='Attachment Preview',
    compute='_compute_attachment_preview_html',
    store=True,  # Penting
    sanitize=False,  # Sangat Penting,
)

first_attachment_mimetype = fields.Char(related='first_attachment_id.mimetype', store=True)


@api.depends('attachment_ids')
def _compute_attachment_preview_html(self):
    for activity in self:
        html = ''
        for attachment in activity.attachment_ids:
            if attachment.mimetype.startswith('image'):
                # Tampilkan gambar dengan link ke versi full-size (lightbox)
                preview_url = f"/web/image/{attachment.id}?width=200&height=200"  # Thumbnail
                full_url = f"/web/image/{attachment.id}"  # Gambar full-size

                html += f'<a href="{full_url}" data-toggle="lightbox" data-gallery="activity-gallery-{activity.id}"><img src="{preview_url}" alt="{attachment.name}" style="max-width: 180px; max-height: 180px; margin-right: 5px;"/></a>'

            else:
                if attachment.mimetype:
                    icon_url = f'/web/static/src/img/mimetypes/{attachment.mimetype.replace("/", "-")}.png'

                html += f'<a href="/web/content/{attachment.id}?download=true" target="_blank"><img src="{icon_url}" title="{attachment.name}" style="width: 48px; height: 48px;"> {attachment.name}</a><br/>'
        activity.attachment_preview_html = html


@api.depends('attachment_ids')
def _compute_first_attachment(self):
    for activity in self:
        if activity.attachment_ids:
            activity.first_attachment_id = activity.attachment_ids[0]
            activity.first_attachment_is_image = activity.first_attachment_id.mimetype.startswith(
                'image') if activity.first_attachment_id.mimetype else False
        else:
            activity.first_attachment_id = False