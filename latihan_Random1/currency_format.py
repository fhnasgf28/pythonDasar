from odoo import fields, models
from odoo.tools.float_utils import float_is_zero, float_round

class ResCurrency(models.Modle):
    _inherit = 'res.currency'

    decimal_point = fields.Char(string="Decimal Separator", size=1, default=".")
    thousands_point = fields.Char(string="Thousands Separator", size=1, default=",")

    def currency_format(self, amount, with_symbol=True):
        currency = self[:1]
        if not currency:
            return ""
        precision = int(currency.decimal_places or 0)
        rounded_amount = float_round(float(amount or 0.0), precision_digits=precision)
        has_zero_fraction = precision > 0 and float_is_zero(
            rounded_amount - int(rounded_amount),
            precision_digits = precision,
        )
        if has_zero_fraction:
            formatted = "{:,.0f}".format(rounded_amount)
        else:
            formatted = ("{:,.%sf}" % precision).format(rounded_amount)
        decimal_point = currency.decimal_point or "."
        thousands_point = currency.thousands_point or ","
        marker = "__thousands_point__"
        formatted = (
            formatted.replace(",", marker)
            .replace(decimal_point, thousands_point)
            .replace(marker, decimal_point)
        )
        if not with_symbol or not currency.symbol:
            return formatted
        if currency.position == "after":
            return "%s %s" % (formatted, currency.symbol)
        return "%s %s" % (currency.symbol, formatted)