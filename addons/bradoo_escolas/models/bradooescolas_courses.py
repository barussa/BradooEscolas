from odoo import models, fields, api


class BradooEscolasCourses(models.Model):
    _name = 'bradooescolas.courses'
    _description = 'courses'
    # _inherit = 'product.template'

    name = fields.Char(string='Course Name', required=True)
    professor_id = fields.Many2one('res.partner', string='Professor', domain=[
        ('isprofessor', '=', True)])
    # iscourse = fields.Boolean(string='Product')
    product_id = fields.Many2one(
        'product.template', string='Product', domain=[
            ('iscourse', '=', True)])
