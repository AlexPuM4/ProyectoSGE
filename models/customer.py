# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'g4_bank.customer'
    _inherit = 'res.users'
    _description = 'Customer'

    account_ids = fields.Many2Many('g4_bank.account')
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
