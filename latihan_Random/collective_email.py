import re

from odoo import models, fields, api

class NewCalendar(models.Model):
    _inherit = 'calendar.new'

    _INVITE_EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def collective_invite_emails(self):
        self.ensure_one()
        raw_invites = (self.invite_email or "").strip()
        if not raw_invites:
            return [], []

        valid_emails = []
        invalid_emails = []
        seen_emails = set()

        tokens = [token.strip() for token in re.split(r"[,;\n\r]+",raw_invites) if token.strip()]
        for token in tokens:
            normalized = token.lower()
            if normalized in seen_emails:
                continue
            seen_emails.add(normalized)
            if self._INVITE_EMAIL_RE.match(normalized):
                valid_emails.append(normalized)
        return valid_emails, invalid_emails
