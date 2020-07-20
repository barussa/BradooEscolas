from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'res.partner'
    _description = 'professor'

    professor_id = fields.Many2one('res.partner', string='Professor')
