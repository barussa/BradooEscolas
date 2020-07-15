from odoo import models, fields, api


class BradooEscolasLessons(models.Model):
    _name = 'bradooescola_lessons'
    _description = 'lessons'

    courses_name = fields.Char(string='Course Name', required=True)
    professor_name = fields.Char(string='Professor')
    product = fields.Char(string='Product')
    date = fields.Datetime()
    class_id = fields.Integer()
