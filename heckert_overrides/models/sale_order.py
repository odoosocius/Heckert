
from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError


class SaleOrderInheritHeckert(models.Model):
    _inherit = 'sale.order'
    preline_text = fields.Text("Textblock")
    postline_text = fields.Text("Textblock")
    text_block_id = fields.Many2one('text.block')
    is_need_template_pre = fields.Boolean()
    is_need_template_post = fields.Boolean()

    @api.onchange('text_block_id')
    def _template_change(self):
        self.ensure_one()
        if self.text_block_id:
            preline_text = ''
            postline_text = ''
            if self.partner_id:
                self.text_block_id.partner_id = self.partner_id.id
                if self.text_block_id.body_html_preline:
                    preline_text = self.text_block_id.body_html_preline
                if self.text_block_id.body_html_postline:
                    postline_text = self.text_block_id.body_html_postline
                mail_template = self.env['mail.template']
                if preline_text is not '':
                    preline_text_return = mail_template._render_template(preline_text, 'text.block',
                                                                         [self.text_block_id.id])
                    self.preline_text = preline_text_return.get(self.text_block_id.id)
                    self.is_need_template_pre = True
                if postline_text is not '':
                    postline_text_return = mail_template._render_template(postline_text, 'text.block',
                                                                          [self.text_block_id.id])
                    self.postline_text = postline_text_return.get(self.text_block_id.id)
                    self.is_need_template_post = True

            else:
                raise UserError(_("Please select a partner"))

        else:
            self.is_need_template_post = False
            self.is_need_template_pre = False
