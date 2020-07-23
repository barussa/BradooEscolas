from odoo import models, fields, api

# Turma


class BradooEscolasClass(models.Model):
    _name = 'bradooescolas.classes'
    _description = 'class'

    name = fields.Char(string='Turma')
    alumns = fields.Many2many(
        comodel_name='res.partner', relation="qualquero",
        column1="class_id", column2="partner_id", string='Alunos')
    course_id = fields.Many2one('bradooescolas.courses', string='Curso')
    professor_id = fields.Many2one('res.partner', string='Professor', domain=[
        ('isprofessor', '=', True)])
    description = fields.Text()
