# -*- coding: utf-8 -*-
# Part of Hadoopt Technologies Private Limited. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class Session(models.Model):
    _name = "session.out"
    _description = "Sessions Out"

    session_id = fields.Char("Session")
    user_id = fields.Many2one('res.users', string="User ID")


class Users(models.Model):
    _inherit = "res.users"

    @api.model
    def _load_default_user(self):
        return [self.env.user.id]

    session_ids = fields.One2many('session.out', 'user_id', string="Session List", default=_load_default_user)
    allow_session = fields.Integer(string='Allowed Session', default=1)
