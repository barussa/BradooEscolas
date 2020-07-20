from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'courses'

    iscourse = fields.Boolean(string='Is Course')
