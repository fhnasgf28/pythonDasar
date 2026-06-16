from odoo import _, api, models
from odoo.exceptions import UserError


class AccountMoveLineModifier(models.Model):
    _inherit = 'account.move.line'

    # Improved error message for forced currency mismatch
    @api.constrains('account_id', 'journal_id')
    def _check_constrains_account_id_journal_id(self):
        for line in self.filtered(lambda x: x.display_type not in ('line_section', 'line_note')):
            account_currency = line.account_id.currency_id
            if account_currency and account_currency != line.company_currency_id and account_currency != line.currency_id:
                raise UserError(_(
                    "Account '%s' requires transactions in %s currency. "
                    "Please change the document Currency to %s, "
                    "or manually enter the %s value in the Amount in Currency column on each line."
                ) % (
                    line.account_id.name,
                    account_currency.name,
                    account_currency.name,
                    account_currency.name,
                ))
        return super()._check_constrains_account_id_journal_id()

    # Real-time hint when account with forced currency is selected
    @api.onchange('account_id')
    def _onchange_account_id_currency_hint(self):
        if not self.account_id:
            return
        account_currency = self.account_id.currency_id
        move_currency = self.move_id.currency_id
        company_currency = self.move_id.company_currency_id
        if account_currency and account_currency != company_currency and account_currency != move_currency:
            return {
                'warning': {
                    'title': _('Currency Mismatch'),
                    'message': _(
                        "Account '%s' requires transactions in %s.\n"
                        "The document is currently set to %s.\n\n"
                        "Please either:\n"
                        "  - Change the document Currency to %s, or\n"
                        "  - Manually enter the %s value in the 'Amount in Currency' column on each line."
                    ) % (
                        self.account_id.name,
                        account_currency.name,
                        move_currency.name,
                        account_currency.name,
                        account_currency.name,
                    )
                }

            }
