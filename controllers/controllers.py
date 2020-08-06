# -*- coding: utf-8 -*-
# from odoo import http


# class Asco(http.Controller):
#     @http.route('/asco/asco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asco/asco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asco.listing', {
#             'root': '/asco/asco',
#             'objects': http.request.env['asco.asco'].search([]),
#         })

#     @http.route('/asco/asco/objects/<model("asco.asco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asco.object', {
#             'object': obj
#         })
