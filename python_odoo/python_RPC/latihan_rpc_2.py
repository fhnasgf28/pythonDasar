import xmlrpc.client

# configuration

url = "http://localhost:8069"
db = "odoo19"
username = "admin"
password = ""

# authentication
print("menghubungkan ke odoo...")
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print('Terhubung ke odoo versi', version)
uid = common.authenticate(db, username, password, {})
print('User ID:', uid)
if not uid:
    print('Authentication failed')
    exit()

print(f"User ID: {uid}")

# --- 3. EXECUTE (ACTION) ---
# Menghubungkan ke endpoint 'object' untuk manipulasi data
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Data Dummy Mahasiswa yang mau diinput
list_mahasiswa = [
    {'name': 'Budi Santoso (RPC)', 'email': 'budi.rpc@kampus.id', 'phone': '0812345678'},
    {'name': 'Siti Aminah (RPC)', 'email': 'siti.rpc@kampus.id', 'phone': '0898765432'},
    {'name': 'Joko Anwar (RPC)', 'email': 'joko.rpc@kampus.id', 'phone': '0856789123'}
]

print("\nMulai proses input data...")

for data in list_mahasiswa:
    # PERINTAH CREATE
    # Structure: execute_kw(db, uid, password, 'nama.model', 'nama_method', [list_values])
    try:
        new_id = models.execute_kw(db, uid, password,
                                   'res.partner', 'create', [data])

        print(f"Sukses! Created Partner: {data['name']} (ID: {new_id})")
    except Exception as e:
        print(f"Gagal create {data['name']}: {e}")

print("\nSelesai    ! Cek menu Contacts di Odoo kamu.")