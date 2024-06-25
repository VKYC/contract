from odoo import models, fields


class CustomContractLine(models.Model):
    _inherit = 'contract.line'

    def _prepare_invoice_line(self, move_form):
        invoice_line_vals = super()._prepare_invoice_line(move_form)
        invoice_line_vals.update({
            "tax_ids": None if self.contract_id.generation_type == "invoice" else False,
        })
        return invoice_line_vals
