from odoo import api, fields, models


class PengambilanKend(models.Model):
    _name = 'titipin.pengambilankend'
    _description = 'Daftar Pengambilan Kendaraan'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi Pengambilan Kendaraan')
    harga = fields.Integer(string='harga sewa')
    
    
