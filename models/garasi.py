from odoo import api, fields, models


class Garasi(models.Model):
    _name = 'titipin.garasi'
    _description = 'New Description'

    name = fields.Many2one(
        comodel_name='res.partner', 
        string='Nama Customer', 
        domain=[('is_customernya','=', True)], store=True, required=True)
    jenis = fields.Selection(string='Jenis Kendaraan', selection=[('motor', 'Motor'), ('mobil', 'Mobil')], required=True)
    kendaraan = fields.Char(string='Nama Kendaraan', required=True)
    warna = fields.Char(string='Warna', required=True)
    tahun = fields.Char(string='Tahun Pembuatan Kendaraan', required=True)
    plat = fields.Char(string='Nomor Plat', required=True)

    garasi_id = fields.Many2one(comodel_name='titipin.tipegarasi', 
                                string='Tipe Garasi', 
                                required=True)

    durasi = fields.Char(string='Durasi Inap', required=True)
    

    pengambilankend_id = fields.Many2one(comodel_name='titipin.pengambilankend', 
                                        string='Pengambilan Kendaraan', 
                                        required=True)
    
    
    harga = fields.Integer(compute='_compute_harga', string='Harga Per Hari')


    @api.depends('garasi_id','pengambilankend_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.garasi_id.harga + record.pengambilankend_id.harga
    
    
    
    des_tipegarasi = fields.Char(compute='_compute_des_tipegarasi', string='Deskripsi Tipe Garasi')
    
    @api.depends('garasi_id')
    def _compute_des_tipegarasi(self):
        for record in self:
            record.des_tipegarasi = record.garasi_id.deskripsi
    
    des_pengambilankend = fields.Char(compute='_compute_des_pengambilankend', string='Deskripsi Pengambilan Kendaraan')
    
    @api.depends('pengambilankend_id')
    def _compute_des_pengambilankend(self):
        for record in self:
            record.des_pengambilankend = record.pengambilankend_id.deskripsi
    
