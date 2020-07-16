from odoo import models, fields, api


class BradooEscolasCourses(models.Model):
    _name = 'bradooescolas.courses'
    _description = 'courses'

    courses_name = fields.Char(string='Course Name', required=True)
    professor_id = fields.Many2one('res.partner', string='Professor')
    product_id = fields.Many2one('product.template', string='Product')
