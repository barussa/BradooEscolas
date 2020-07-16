from odoo import models, fields, api


class BradooEscolasClass(models.Model):
    _name = 'bradooescolas.class'
    _description = 'class'

    name = fields.Char(string='Class Name')
    alumns = fields.Many2one('res.partner', string='Alunos')
    course_id = fields.Many2one('bradooescolas.courses', string='Curso')
    professor_id = fields.Many2one('res.partner', string='Professor')
    description = fields.Text()
