from odoo import models, fields, api, _ 
from odoo.exceptions import UserError 
import datetime

class ITServicerequest(models.Model):
    _name = 'it.service.request'
    _description = 'IT Service request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Judul permintaan',required= True,tracking=True)
    description = fields.Text(string='Deskripsi Detail',tracking=True)
    requester_id = fields.Many2one(
        'res.partner',
        string="Pemohon",
        required=True,
        default=lambda self: self.env.user.partner_id,
        tracking=True
    )
    assigned_to_id = fields.Many2one(
        'res.users',
        string='Ditugaskan kepada',
        tracking=True
    )
    requested_date = fields.Date(
        string="Tanggal Permintaan",
        default=fields.Date.today,
        readonly=True,
        tracking=True
    )
    deadline_date = fields.Date(string='Batas Waktu', tracking=True)
    status = fields.Selection([
        ('draft', 'draft'),
        ('submitted', 'dikirim'),
        ('in_progress', 'Dalam Pengerjaan'),
        ('resolved', 'Selesai'),
        ('cancelled', 'Dibatalkan'),
    ], string='Status', default='draft', readonly=True,tracking=True)
    priority = fields.Selection([
        ('0', 'Rendah'),
        ('1', 'Sedang'),
        ('2', 'Tinggi'),
    ], string='Prioritas', default=0, tracking=True)
    resolution_notes = fields.Text(string='Catatan Penyelesaian',tracking=True)
    resolved_date = fields.Datetime(string='Tanggal Selesai', readonly=True,tracking=True)
    # metode untuk transisi status(business logik)

    def action_submit_request(self):
        for record in self:
            if record.status != 'draft':
                raise UserError(_("Permintaan hanya bisa dikirim dari status 'Draft"))
            record.write({'status':'submitted'})
    
    def action_assign_request(self):
        for record in self:
            if record.status != 'submitted':
                raise UserError("Permintaan hanya bisa ditugaskan dari status 'Dikirim'")
            if not record.assigned_to_id:
                raise UserError(_("Anda harus menugaskan permintaan ini kepada seseorang terlebih dahulu"))
            record.write({'status':'in_progress'})
    
    def action_cancel_request(self):
        for record in self:
            if record.status in ['resolved', 'cancelled']:
                raise UserError(_("Hanya permintaan 'Selesai' atau 'dibatalkan' yang dibuka kembali"))
            record.write({'status': 'cancelled'})
    
    def action_reopen_request(self):
        for record in self:
            if record.status not in ['resolved', 'cancelled']:
                raise UserError(_("Hanya Permintaan 'Selesai' atau 'dibatalkan' yang bisa dibuka kembali"))
            record.write({
                'status': 'in_progress' if record.assigned_to_id else 'submitted',
                'resolved_date': False,
                'resolution_notes': False,
            })

    @api.constrains('deadline', 'request_date')
    def _check_deadline_date(self):
        for record in self:
            if record.deadline_date and record.request_date and record.deadline_date < record.request_date:
                raise UserError(_("Batas Waktu tidak boleh sebelum tanggal permintaan"))
