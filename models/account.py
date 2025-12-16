# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
    _name = 'g4_bank.account'
    _description = 'Account'
#El campo name es la description
    name = fields.Char(string="Description", required = True)
    balance = fields.Double(string="Current Balance",required = True)
    creditLine = fields.Double(required = True)
    beginBalance = fields.Double(string ="Begin Balance",required = True)
    beginBalanceTimestamp = fields.Date(string="Begin Balance Timestamp",required = True)
    typeAccount = fields.Selection(selection=TYPE_ACCOUNT_SELECTION,required = True)
    customer_ids = fields.Many2Many('g4_bank.customer')
    #movement_ids= fields.One2Many('g4_bank.movement','account_id')
    

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
