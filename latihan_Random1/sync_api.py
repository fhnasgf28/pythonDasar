import requests
import xmlrpc.client

API_URL = "https://jsonplaceholder.typicode.com/posts/1"
ODOO_URL = "https://alamat-odoo-anda.com"
DB = "nama_database"
USERNAME = "email@anda.com"
PASSWORD = "api_key_atau_password"

def get_external_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def push_to_odoo(data):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    if not uid:
        print("gagal Login ke odoo")
        return

    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    vals = {
        'name': data.get('title'),
        'description': data.get('body'),
        'type': 'opportunity'
    }

    new_id = models.execute_kw(DB, uid, PASSWORD, 'crm.lead', 'create', [vals])
    return new_id

# eksekusi
data_api = get_external_data()
if data_api:
    print(f"Data API didapat: {data_api['title']}")
    record_id = push_to_odoo(data_api)
    print(f"Push to Odoo API didapat: {record_id}")
else:
    print("gagal mengambil data dari API")