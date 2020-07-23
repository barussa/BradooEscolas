from odoo import models, fields, api


class BradooEscolasLessons(models.Model):
    _name = 'bradooescolas.lessons'
    _description = 'lessons'

    name = fields.Char(string='Aula')
    class_id = fields.Many2one('bradooescolas.classes', string='Turma')
    professor_id = fields.Many2one(
        related='class_id.professor_id', string='Professor')
    date = fields.Date()
    attendances = fields.One2many(
        'bradooescolas.attendance', string='Presença',
        inverse_name='lesson_id')

    @api.onchange('class_id')
    def _onchange_class_id(self):
        attendances = [(5, 0, 0)]
        print('olaaaaaaaaaaaaaaaaa!!!!!!!!!!!!!!!!!!!!!!!!!', self)
        alumns = self.class_id.alumns
        for alumn in alumns:
            print('testeeeeeeeeeeeeeeaaaaaaaaaae', alumn)
            attendances.append((0, 0, {
                'alumn_id': alumn.id
            }))
        self.attendances = attendances
