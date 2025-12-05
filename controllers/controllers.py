# -*- coding: utf-8 -*-
# from odoo import http


# class G4Bank(http.Controller):
#     @http.route('/g4_bank/g4_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/g4_bank/g4_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('g4_bank.listing', {
#             'root': '/g4_bank/g4_bank',
#             'objects': http.request.env['g4_bank.g4_bank'].search([]),
#         })

#     @http.route('/g4_bank/g4_bank/objects/<model("g4_bank.g4_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('g4_bank.object', {
#             'object': obj
#         })
