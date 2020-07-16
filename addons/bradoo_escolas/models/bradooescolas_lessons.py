from odoo import models, fields, api


class BradooEscolasLessons(models.Model):
    _name = 'bradooescolas.lessons'
    _description = 'lessons'

    course_id = fields.Many2one('bradooescolas.courses', string='Curso')
    professor_id = fields.Many2one('res.partner', string='Professor')
    date = fields.Date()
    class_id = fields.Many2one('bradooescolas.class', string='Salas')
