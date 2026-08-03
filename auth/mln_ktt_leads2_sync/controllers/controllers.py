# -*- coding: utf-8 -*-

import json
import logging
from uuid import uuid4

import odoo
from odoo import SUPERUSER_ID, api, http
from odoo.http import db_monodb, request


_logger = logging.getLogger(__name__)


class KttLeads2SyncController(http.Controller):
    def _json_dump(self, payload):
        try:
            return json.dumps(payload or {}, ensure_ascii=False, default=str)
        except Exception:
            return '{}'

    def _safe_text(self, text, limit=4000):
        text = text or ''
        return text[:limit]

    def _create_sync_log(self, env, **vals):
        try:
            env['mln.sync.log'].sudo().create(vals)
        except Exception:
            _logger.exception('[KTT->MLN] Failed to create mln.sync.log')

    @http.route('/ktt/sync/ping', type='http', auth='public', csrf=False, methods=['GET'])
    def ktt_sync_ping(self, **kwargs):
        dbname = request.session.db or request.httprequest.args.get('db') or db_monodb(request.httprequest)
        body = json.dumps({'ok': True, 'db': dbname}, ensure_ascii=False)
        return request.make_response(body, [('Content-Type', 'application/json')])

    @http.route('/ktt/sync/leads2/sale_order', type='json', auth='public', csrf=False, methods=['POST'])
    def sync_leads2_sale_order(self, **payload):
        payload = payload or request.jsonrequest or {}
        payload_json = self._json_dump(payload)
        request_url = request.httprequest.url
        dbname = request.session.db or request.httprequest.args.get('db') or db_monodb(request.httprequest)
        if not dbname:
            _logger.warning('[KTT->MLN] Missing target database in request')
            return {'success': False, 'error': 'database not specified'}

        incoming_key = request.httprequest.headers.get('X-API-KEY')

        with odoo.registry(dbname).cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            params = env['ir.config_parameter'].sudo()
            expected_key = params.get_param('ktt_sync.api_key')
            if not expected_key:
                bootstrap_key = (incoming_key or '').strip() or ('KTTSYNC-%s' % uuid4().hex)
                params.set_param('ktt_sync.api_key', bootstrap_key)
                expected_key = bootstrap_key
                cr.commit()
                _logger.warning(
                    '[KTT->MLN] Auto-created missing ktt_sync.api_key for db=%s (from_request=%s)',
                    dbname,
                    bool((incoming_key or '').strip()),
                )

            if not expected_key or incoming_key != expected_key:
                _logger.warning('[KTT->MLN] Unauthorized sync request for db=%s', dbname)
                response_payload = {'success': False, 'error': 'unauthorized'}
                self._create_sync_log(
                    env,
                    ktt_leads2_id=str(payload.get('ktt_leads2_id') or ''),
                    url=request_url,
                    payload_json=payload_json,
                    status_code=401,
                    response_text=self._json_dump(response_payload),
                    error='unauthorized',
                )
                return response_payload

            _logger.info('[KTT->MLN] Incoming payload db=%s url=%s payload=%s', dbname, request_url, payload_json)

            try:
                ktt_id = str(payload.get('ktt_leads2_id') or '').strip()
                team_payload = payload.get('team') or {}
                team_name = (team_payload.get('name') or '').strip()
                team_code = (team_payload.get('code') or '').strip()
                salespersons = payload.get('salespersons') or []

                lead_payload = payload.get('lead') or {}
                partner_payload = payload.get('partner') or {}

                lead_name = (
                    (lead_payload.get('name') or '').strip()
                    or (payload.get('name') or '').strip()
                    or (partner_payload.get('name') or '').strip()
                )
                if not lead_name:
                    response_payload = {'success': False, 'error': 'lead.name is required'}
                    self._create_sync_log(
                        env,
                        ktt_leads2_id=ktt_id,
                        url=request_url,
                        payload_json=payload_json,
                        status_code=400,
                        response_text=self._json_dump(response_payload),
                        error='lead.name is required',
                    )
                    return response_payload

                team_model = env['crm.team'].sudo()
                team = False
                team_domain_used = []
                team_code_field = (params.get_param('mln_sync.team_code_field') or 'x_team_code').strip()

                if team_code and team_code_field in team_model._fields:
                    team_domain_used = [(team_code_field, '=', team_code)]
                    team = team_model.search(team_domain_used, limit=1)
                if not team and team_name:
                    team_domain_used = [('name', '=', team_name)]
                    team = team_model.search(team_domain_used, limit=1)

                missing_team = bool(team_name or team_code) and not bool(team)

                missing_users = []
                mapped_users = []
                for line in salespersons:
                    login = (line.get('login') or '').strip()
                    if not login:
                        continue
                    user = env['res.users'].sudo().search([('login', '=', login)], limit=1)
                    if not user:
                        missing_users.append(login)
                        continue
                    line_type = line.get('type') if line.get('type') in ('main_salesperson', 'salesperson') else 'salesperson'
                    mapped_users.append({'login': login, 'user_id': user.id, 'type': line_type})

                main_user_id = False
                for mapped in mapped_users:
                    if mapped.get('type') == 'main_salesperson':
                        main_user_id = mapped.get('user_id')
                        break
                if not main_user_id and mapped_users:
                    main_user_id = mapped_users[0].get('user_id')

                Lead = env['crm.lead'].sudo()
                lead_domain = []
                if ktt_id and 'x_ktt_leads2_id' in Lead._fields:
                    lead_domain = [('x_ktt_leads2_id', '=', ktt_id)]
                elif ktt_id:
                    lead_domain = [('name', '=', lead_name)]
                lead = Lead.search(lead_domain, limit=1) if lead_domain else False

                partner_name = (partner_payload.get('name') or '').strip()
                partner_email = (partner_payload.get('email') or '').strip()
                partner_phone = (partner_payload.get('phone') or '').strip()
                partner_mobile = (partner_payload.get('mobile') or '').strip()
                partner_vat = (partner_payload.get('vat') or '').strip()

                Partner = env['res.partner'].sudo()
                partner = False
                incoming_partner_id = partner_payload.get('partner_id')
                if incoming_partner_id:
                    try:
                        partner = Partner.browse(int(incoming_partner_id)).exists()
                    except Exception:
                        partner = False
                if not partner and partner_vat:
                    partner = Partner.search([('vat', '=', partner_vat)], limit=1)
                if not partner and partner_email:
                    partner = Partner.search([('email', '=', partner_email)], limit=1)
                if not partner and partner_phone:
                    partner = Partner.search([('phone', '=', partner_phone)], limit=1)
                if not partner and (partner_name or partner_email or partner_phone or partner_mobile):
                    partner_vals = {'name': partner_name or lead_name}
                    if partner_email:
                        partner_vals['email'] = partner_email
                    if partner_phone:
                        partner_vals['phone'] = partner_phone
                    if partner_mobile:
                        partner_vals['mobile'] = partner_mobile
                    if partner_vat:
                        partner_vals['vat'] = partner_vat
                    partner = Partner.create(partner_vals)

                write_vals = {
                    'name': lead_name,
                    'partner_name': partner_name,
                    'email_from': partner_email,
                    'phone': partner_phone,
                }
                if partner and 'partner_id' in Lead._fields:
                    write_vals['partner_id'] = partner.id
                if partner_payload.get('mobile') and 'mobile' in Lead._fields:
                    write_vals['mobile'] = (partner_payload.get('mobile') or '').strip()
                if lead_payload.get('description') and 'description' in Lead._fields:
                    write_vals['description'] = lead_payload.get('description')
                if lead_payload.get('type') in ('lead', 'opportunity') and 'type' in Lead._fields:
                    write_vals['type'] = lead_payload.get('type')
                if team and 'team_id' in Lead._fields:
                    write_vals['team_id'] = team.id
                if main_user_id and 'user_id' in Lead._fields:
                    write_vals['user_id'] = main_user_id
                if ktt_id and 'x_ktt_leads2_id' in Lead._fields:
                    write_vals['x_ktt_leads2_id'] = ktt_id

                if lead:
                    write_result = lead.write(write_vals)
                else:
                    lead = Lead.create(write_vals)
                    write_result = True

                cr.commit()

                response_payload = {
                    'success': True,
                    'lead_id': lead.id,
                    'missing_users': missing_users,
                    'missing_team': missing_team,
                    'matched_domain': repr(lead_domain),
                }

                _logger.info(
                    '[KTT->MLN] Synced Lead=%s team_domain=%s mapped_users=%s missing_users=%s missing_team=%s write_result=%s db=%s',
                    lead.id,
                    team_domain_used,
                    mapped_users,
                    missing_users,
                    missing_team,
                    write_result,
                    dbname,
                )
                self._create_sync_log(
                    env,
                    ktt_leads2_id=ktt_id,
                    url=request_url,
                    payload_json=payload_json,
                    status_code=200,
                    response_text=self._json_dump(response_payload),
                    lead_id=lead.id,
                    missing_users_json=self._json_dump(missing_users),
                    missing_team_value=(team_name or team_code) if missing_team else '',
                    matched_domain=repr(lead_domain),
                    mapped_team=(team.display_name if team else ''),
                    mapped_users_json=self._json_dump(mapped_users),
                    write_result=bool(write_result),
                )
                return response_payload
            except Exception as err:
                _logger.exception('[KTT->MLN] Failed processing payload db=%s url=%s', dbname, request_url)
                response_payload = {'success': False, 'error': str(err)}
                self._create_sync_log(
                    env,
                    ktt_leads2_id=str(payload.get('ktt_leads2_id') or ''),
                    url=request_url,
                    payload_json=payload_json,
                    status_code=500,
                    response_text=self._json_dump(response_payload),
                    error=self._safe_text(str(err)),
                )
                return response_payload
