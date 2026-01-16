# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'g4_bank.customer'
    _inherit = 'res.users'
    _description = 'Customer'
    
    firstName = fields.Text()
    lastName = fields.Text()
    middleInitial = fields.Text()
    street = fields.Text()
    city = fields.Text()
    state = fields.Text()
    email = fields.Text()
    password = fields.Text()
    
    account_ids = fields.Many2Many('g4_bank.account')
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
