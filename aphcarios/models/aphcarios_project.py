from odoo import models, fields, api

class AphcariosProject(models.Model):
    _name = "aphcarios.project"
    _description = "Aphcarios Projects"

    name = fields.Char(string="Project Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    project_code = fields.Char(string="Project Code", required=True)
    project_description = fields.Text(string="Project Description")
    avatar_image = fields.Image(string="Project Image")
