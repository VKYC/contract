from datetime import date
from odoo import models, fields


class MPContractFutureIndicators(models.Model):
    _name = "mp.contract.future.indicators"
    _rec_name = "date"

    date = fields.Date(string="Fecha del Indicador", default=lambda self: date.today())
    currency_id = fields.Many2one(comodel_name="res.currency", string="Moneda", domain=[('active', '=', True)])
    value = fields.Monetary(string="Valor de moneda")


