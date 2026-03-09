from odoo import models, fields, api

class KontakPelanggan(models.Model):
    _name = 'crm.kontak.pelanggan'
    _description = 'Kontak Pelanggan'

    name = fields.Char(string="Nama Pelanggan", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Nomor Telepon")
    notes = fields.Text(string="Catatan")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('kontak.pelanggan') or 'New'
        return super(KontakPelanggan, self).create(vals)

    @api.model
    def cari_pelanggan(self, name):
        return self.search([('name', 'ilike', name)])

    def tambah_catatan(self, catatan_baru):
        for record in self:
            record.write({'notes': record.notes + '\n' + catatan_baru})
