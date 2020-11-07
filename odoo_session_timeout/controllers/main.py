# -*- coding: utf-8 -*-
# Part of Hadoopt Technologies Private Limited. See LICENSE file for full copyright and licensing details.

import odoo
from odoo import http
from odoo.addons.web.controllers.main import Home
import os
from odoo.http import request
class HomeExtended(Home):

    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        result = super(HomeExtended, self).web_client(s_action,**kw)
        request.uid = request.session.uid
        var = request.env['session.out'].sudo().search([('user_id','=',request.uid),('session_id','=',request.session.sid)])
        if len(var) == 0:
            request.env['session.out'].sudo().create({'user_id':request.uid,'session_id':request.session.sid})

        exist_rec = request.env['session.out'].sudo().search([('user_id', '=', request.uid)], order='id desc')

        count_path = 1
        for res in exist_rec:
            sess = 'werkzeug_'+res.session_id+'.sess'
            path_1 = odoo.tools.config.session_dir
            path = os.path.join(path_1, sess)
            if os.path.exists(path):
                if count_path > res.user_id.allow_session:
                    os.unlink(path)
                    res.unlink()
            count_path = count_path+1
        return result