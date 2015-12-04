# -*- coding: utf-8 -*-
from openerp import http

# class TiendaMascota(http.Controller):
#     @http.route('/tienda_mascota/tienda_mascota/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tienda_mascota/tienda_mascota/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tienda_mascota.listing', {
#             'root': '/tienda_mascota/tienda_mascota',
#             'objects': http.request.env['tienda_mascota.tienda_mascota'].search([]),
#         })

#     @http.route('/tienda_mascota/tienda_mascota/objects/<model("tienda_mascota.tienda_mascota"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tienda_mascota.object', {
#             'object': obj
#         })