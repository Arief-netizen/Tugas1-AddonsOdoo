from odoo import api, fields, models


class TipeGarasi(models.Model):
    _name = 'titipin.tipegarasi'
    _description = 'Daftar Tip'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi Tipe Garasi')
    harga = fields.Integer(string='Harga Sewa')
    
