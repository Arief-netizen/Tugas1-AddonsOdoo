from odoo import http, fields, models
from odoo.http import request
import json

class KursiTamuCon(http.Controller):
    
    #GET
    @http.route(['/kursitamu','/kursitamu/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getKursiTamu(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            kursi = request.env['titipin.kursitamu'].search([])            
            for k in kursi:
                value.append({"id": k.id,
                            "namakursi" : k.name,
                            "tipe_bahan" : k.tipe,
                            "stok_tersedia" : k.stok,
                            "harga_sewa" : k.harga})
            return json.dumps(value)
        else:
            kursiid = request.env['titipin.kursitamu'].search([('id','=',idnya)])
            for k in kursiid:
                value.append({"id": k.id,
                            "namakursi" : k.name,
                            "tipe_bahan" : k.tipe,
                            "stok_tersedia" : k.stok,
                            "harga_sewa" : k.harga})

    #POST
    @http.route('/createkursi', auth='user', type='json', methods=['POST'])
    def createKursi(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals = {
                    'name' : kw['name'],
                    'tipe' : kw['tipe'],
                    'stok' : kw['stok'],
                    'harga' : kw['harga']
                }
                kursibaru = request.env['titipin.kursitamu'].create(vals)
                args = {'succeed':True, "ID":kursibaru.id}
                return args

    #DELETE
    