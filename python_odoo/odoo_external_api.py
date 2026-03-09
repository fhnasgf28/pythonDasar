import xmlrpc.client

def search_and_read_from_odoo(url, db, username, password, model, domain, fields):
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    if not uid:
        raise Exception("Authentication failed.")
    
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    return models.execute_kw(db, uid, password, model, 'search_read', [domain], {'fields': fields})