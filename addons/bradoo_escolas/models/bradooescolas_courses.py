from odoo import models, fields, api


class BradooEscolasCourses(models.Model):
    _name = 'bradooescolas.courses'
    _description = 'courses'

    courses_name = fields.Char(string='Course Name', required=True)
    professor_name = fields.Char(string='Professor')
    product = fields.Char(string='Product')
