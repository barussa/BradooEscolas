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

    # @api.depends('course_id')
    @api.onchange('alumns', 'course_id')
    def _onchange_alumns(self):
        values = []
        account_move = self.env['account.move'].search([
            ('invoice_payment_state', '=', 'paid')
        ])
        for move in account_move:
            for line in move.line_ids:
                if line.product_id.id == self.course_id.product_id.id:
                    values.append(move.partner_id.id)
        return {'domain': {'alumns': [('id', 'in', values)]}}

    @api.onchange('course_id')
    def _onchange_course(self):
        self.alumns = None
