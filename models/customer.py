# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'g4_bank.customer'
    _description = 'Customer'

    first_name = fields.Char(required = True)
    last_name = fields.Char(required = True)
    middle_initial = fields.Char()
    street = fields.Char(required = True)
    city = fields.Char(required = True)
    state = fields.Char(required = True)
    zip_cp = fields.Integer(required = True)
    phone = fields.Integer(required = True)
    email  = fields.Char(required = True)
    password = fields.Char(required = True)
    account_ids = fields.Many2Many('g4_bank.account')
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
