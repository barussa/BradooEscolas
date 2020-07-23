from odoo import models, fields, api


class Attendance(models.Model):
    _name = 'bradooescolas.attendance'

    alumn_id = fields.Many2one('res.partner', string='Aluno')
    lesson_id = fields.Many2one('bradooescolas.lessons', string='Aula')
    ispresent = fields.Boolean(string='Is Present')
