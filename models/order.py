from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'titipin.order'
    _description = 'New Description'

    ordergarasidetail_ids = fields.One2many(
        comodel_name='titipin.ordergarasidetail', 
        inverse_name='order_id', 
        string='Order Garasi')
    
    orderfasilitastambahandetail_ids = fields.One2many(
        comodel_name='titipin.orderfasilitastambahandetail', 
        inverse_name='orderk_id', 
        string='Order Fasilitas Tambahan')
    
    
    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Order',default=fields.Datetime.now())
    tanggal_pengiriman = fields.Date(string='Tanggal Konfirmasi', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya','=', True)],store=True)
    
    
    
    total = fields.Integer(compute='_compute_total', string='Total Harga', store=True)
    
    @api.depends('ordergarasidetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['titipin.ordergarasidetail'].search([('order_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['titipin.orderfasilitastambahandetail'].search([('orderk_id', '=', record.id)]).mapped('harga'))
            record.total = a + b
    
    sudah_bayar = fields.Boolean(string='Status Bayar', default=False)
    def bayar_order(self):
        pass
    

class OrderGarasiDetail(models.Model):
    _name = 'titipin.ordergarasidetail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='titipin.order', string='Order')
    garasi_id = fields.Many2one(comodel_name='titipin.garasi', string='Nama Customer')   
    
         
    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='Total Harga')
    qty = fields.Integer(string='Durasi (hari)')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Per Hari')
    
    @api.depends('garasi_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.garasi_id.harga
    
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty
           
class OrderFasilitasTambahanDetail(models.Model):
    _name = 'titipin.orderfasilitastambahandetail'
    _description = 'New Description'
    
    orderk_id = fields.Many2one(comodel_name='titipin.order', string='Order Fasilitas Tambahan')
    fasilitastambahan_id = fields.Many2one(
        comodel_name='titipin.fasilitastambahan', 
        string='Fasilitas Tambahan')
    
    name = fields.Char(string='Name')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga')
    
    @api.depends('fasilitastambahan_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.fasilitastambahan_id.harga
    
    qty = fields.Integer(string='Quantity')
    

    
    harga = fields.Integer(compute='_compute_harga', string='Total Harga')
    
    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty
