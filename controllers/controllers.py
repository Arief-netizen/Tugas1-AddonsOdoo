# -*- coding: utf-8 -*-
# from odoo import http


# class TitipinGarage(http.Controller):
#     @http.route('/titipingarage/titipingarage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/titipingarage/titipingarage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('titipingarage.listing', {
#             'root': '/titipingarage/titipingarage',
#             'objects': http.request.env['titipingarage.titipingarage'].search([]),
#         })

#     @http.route('/titipingarage/titipingarage/objects/<model("titipingarage.titipingarage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('titipingarage.object', {
#             'object': obj
#         })
