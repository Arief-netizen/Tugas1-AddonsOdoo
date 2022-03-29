from odoo import api, fields, models

class DetailPembayaran(models.Model):
    _name = 'titipin.detailpembayaran'
    _description = 'Detail Pembayaran'

    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Customer')
    order_id = fields.Many2one(comodel_name='titipin.order', string='No. Order')
    
    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['titipin.order'].search([('id', '=', record.order_id.id)]).mapped('pemesan').name
    
    tgl_detailpembayaran = fields.Date(string='Tanggal Pembayaran', default=fields.Date.today())
    
    tagihan = fields.Char(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total            
     
    #create centang sudah dibayar (object)
    @api.model
    def create(self,vals):
        record = super(DetailPembayaran, self).create(vals) 
        if record.tgl_detailpembayaran:
            self.env['titipin.order'].search([('id','=',record.order_id.id)]).write({'sudah_bayar':True})

            #menghubungkan ke model akunting
            self.env['titipin.akunting'].create({'kredit' : record.tagihan, 'name':record.name})
            return record

    #unlink centang data detailpembayaran yang dihapus (boolean)
    def unlink(self):
        for arief in self:
            self.env['titipin.order'].search([('id', '=', arief.order_id.id)]).write({'sudah_bayar':False})           
        record = super(DetailPembayaran, self).unlink()