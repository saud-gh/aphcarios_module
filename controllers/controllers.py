# -*- coding: utf-8 -*-
# from odoo import http


# class Now(http.Controller):
#     @http.route('/now/now', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/now/now/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('now.listing', {
#             'root': '/now/now',
#             'objects': http.request.env['now.now'].search([]),
#         })

#     @http.route('/now/now/objects/<model("now.now"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('now.object', {
#             'object': obj
#         })
