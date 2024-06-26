from datetime import date
from odoo import models, fields


class MPContractFutureIndicators(models.Model):
    _name = "mp.contract.future.indicators"

    date = fields.Date(string="Fecha del Indicador", default=lambda self: date.today())
    currency_id = fields.Many2one(comodel_name="res.currency", domain=[('active', '=', True)])
    valor = fields.Monetary(string="Valor de moneda")


