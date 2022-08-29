
from odoo import models, fields


class ExtendedProduct(models.Model):
    _inherit = "product.template"

    associated_projects = fields.Many2many("aphcarios.project")