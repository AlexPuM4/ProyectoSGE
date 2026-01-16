# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
    _name = 'g4_bank.account'
    _description = 'Account'
#El campo name es la description
    name = fields.Char(string="Description", required = True)
    balance = fields.Float(string="Current Balance",required = True)
    creditLine = fields.Float(required = True)
    beginBalance = fields.Float(string ="Begin Balance",required = True)
    beginBalanceTimestamp = fields.Date(string="Begin Balance Timestamp",required = True)
    typeAccount = fields.Selection([('STANDART', 'Standart'),('CREDIT','Credit')],required = True)
    customer_ids = fields.Many2many('g4_bank.customer')
    #movement_ids= fields.One2Many('g4_bank.movement','account_id')
    

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
