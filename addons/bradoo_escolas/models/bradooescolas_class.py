from odoo import models, fields, api


class BradooEscolasClass(models.Model):
    _name = 'bradooescolas.class'
    _description = 'class'

    name = fields.Char(string='Class Name')
    alumns = fields.Char(string='Alumns')
    professor = fields.Char(string='Professor')
    course = fields.Char(string='Course')
    course_id = fields.Integer()
    professor_id = fields.Integer()
    description = fields.Text()
