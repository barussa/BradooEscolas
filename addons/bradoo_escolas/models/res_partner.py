from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'res.partner'
    _description = 'professor'

    isprofessor = fields.Boolean(string='Professor')
