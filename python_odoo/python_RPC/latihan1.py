import xmlrpc.client

# detail koneksi ke server
url = "http://localhost:8069"
db = "odoo"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')

# melakukan autentikasi
uid = common.authenticate(db, username, password, {})
if not uid:
    raise Exception("Authentication failed.")
else:
    print("Authentication successful.")