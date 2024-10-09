# Copyright 2020 Lokavaluto ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomCustomerPortal(CustomerPortal):
    @route(["/my/account"], type="http", auth="user", website=True)
    def account(self, redirect=None, **post):
        self.OPTIONAL_BILLING_FIELDS.append("employees_number") #unecessary save in res partner, but necessary to avoid error on form post

        response = super(CustomCustomerPortal, self).account(redirect, **post)
        
        if post and request.httprequest.method == "POST":
            error, error_message = self.details_form_validate(post)
            if not error:
                user = request.env.user
                if user.partner_id and post["employees_number"]:
                    user.partner_id.employees_number = post["employees_number"]
                    
        return response
    

    def details_form_validate(self, data):
        error, error_message = super(CustomCustomerPortal, self).details_form_validate(data)
        if data.get('employees_number') and not data['employees_number'].isdigit():
            error['employees_number'] = 'error'
            error_message.append("Le nombre d'employés doit être un chiffre entier")
        return error, error_message

