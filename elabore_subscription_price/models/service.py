from odoo import fields, models

class Service(models.Model):
    _inherit = 'service'

    category = fields.Selection([('A','A'),('B','B'),('C','C'),('odoo','Odoo')], string="Catégorie")
