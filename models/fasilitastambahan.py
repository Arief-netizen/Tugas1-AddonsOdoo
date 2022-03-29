from odoo import api, fields, models


class FasilitasTambahan(models.Model):
    _name = 'titipin.fasilitastambahan'
    _description = 'Data Fasilitas Tambahan'

    name = fields.Char(string='Nama')
    harga = fields.Integer(string='Harga')
    
    
    
    
