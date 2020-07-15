# -*- coding: utf-8 -*-
# from odoo import http


# class BradooEscolas(http.Controller):
#     @http.route('/bradoo_escolas/bradoo_escolas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bradoo_escolas/bradoo_escolas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bradoo_escolas.listing', {
#             'root': '/bradoo_escolas/bradoo_escolas',
#             'objects': http.request.env['bradoo_escolas.bradoo_escolas'].search([]),
#         })

#     @http.route('/bradoo_escolas/bradoo_escolas/objects/<model("bradoo_escolas.bradoo_escolas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bradoo_escolas.object', {
#             'object': obj
#         })
