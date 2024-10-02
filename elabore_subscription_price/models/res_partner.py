from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    employees_number = fields.Integer("Nombre d'employés")
    installed_softwares = fields.Many2many("service", compute="_compute_installed_softwares", readonly=True)
    backup_size = fields.Float()
    
    def _compute_installed_softwares(self):
        # list all installed services for a partner=
        for partner in self:
            services = []
            equipments = self.env['maintenance.equipment'].search([('project_id.partner_id','=',partner.id)])
            for service_instance in equipments.service_ids:
                if service_instance.service_id:
                    services.append(service_instance.service_id.id)
            partner.installed_softwares = services

    