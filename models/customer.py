# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'g4_bank.customer'
    _description = 'Customer'

    first_name = fields.Char()
    last_name = fields.Char()
    middle_initial = fields.Char()
    street = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Integer()
    phone = fields.Integer()
    email  = fields.Char()
    password = fields.Char()
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
