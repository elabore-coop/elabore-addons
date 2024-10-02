from odoo import fields, models

class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    mo_price = fields.Float("Prix de la MO", compute="compute_mo_price")
    employees_number = fields.Integer("Nombre d'employés", related="partner_id.employees_number")  
    installed_softwares = fields.Many2many("service", related="partner_id.installed_softwares", readonly=True)
    backup_size = fields.Float(related="partner_id.backup_size", readonly=True)

    def compute_mo_price(self):
        for sale_subscription in self:
            has_odoo = any([service.category == 'odoo' for service in sale_subscription.partner_id.installed_softwares])
            backup_size = sale_subscription.partner_id.backup_size
            employees_number = sale_subscription.partner_id.employees_number
            odoo_nb = len([service for service in sale_subscription.partner_id.installed_softwares if service.category == 'odoo'])
            cata_nb = len([service for service in sale_subscription.partner_id.installed_softwares if service.category == 'A'])
            catb_nb = len([service for service in sale_subscription.partner_id.installed_softwares if service.category == 'B'])
            catc_nb = len([service for service in sale_subscription.partner_id.installed_softwares if service.category == 'C'])
            mo_price = 0
            if has_odoo:
                mo_price = 40
                mo_price += 4 * employees_number
            else:
                mo_price = 15
                mo_price += 1 * employees_number
            mo_price += backup_size * 0.04
            mo_price += 20 * odoo_nb
            mo_price += 10 * cata_nb
            mo_price += 8 * catb_nb
            mo_price += 5 * catc_nb
            sale_subscription.mo_price = mo_price




