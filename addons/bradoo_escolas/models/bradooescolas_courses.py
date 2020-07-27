from odoo import models, fields, api


class BradooEscolasCourses(models.Model):
    _name = 'bradooescolas.courses'
    _description = 'courses'

    name = fields.Char(string='Nome do Curso', required=True)
    professor_id = fields.Many2one('res.partner', string='Professor', domain=[
        ('isprofessor', '=', True)])
    product_id = fields.Many2one(
        'product.template', string='Product', domain=[
            ('iscourse', '=', True)])
