from odoo import api, fields, models, _


class TextBlockTemplate(models.Model):
    _name = 'text.block'
    name = fields.Char("Name")
    body_html_preline = fields.Text('Pre Line')
    body_html_postline = fields.Text('Post lIne')
    partner_id = fields.Many2one('res.partner')



