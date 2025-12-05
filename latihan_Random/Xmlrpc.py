import xmlrpc.client

# --- Konfigurasi koneksi ---
url = "http://localhost:8069"   # ganti dengan URL Odoo kamu
db = "nama_database"            # ganti dengan nama database Odoo
username = "admin@example.com"  # ganti dengan user Odoo
password = "admin"              # ganti dengan password Odoo

# --- Endpoint XML-RPC ---
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})

if not uid:
    raise Exception("Login gagal, cek username/password/database!")

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# --- Contoh: baca data partner ---
partners = models.execute_kw(
    db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', True]]],   # domain filter
    {'fields': ['id', 'name', 'email'], 'limit': 5}
)
print("Partner:", partners)

# --- Contoh: buat partner baru ---
new_partner_id = models.execute_kw(
    db, uid, password,
    'res.partner', 'create',
    [{
        'name': "Partner Baru via XMLRPC",
        'email': "partnerbaru@example.com",
    }]
)
print("Partner baru ID:", new_partner_id)

# --- Contoh: update partner ---
models.execute_kw(
    db, uid, password,
    'res.partner', 'write',
    [[new_partner_id], {'phone': '08123456789'}]
)
print("Partner berhasil diupdate")

# --- Contoh: hapus partner ---
models.execute_kw(
    db, uid, password,
    'res.partner', 'unlink',
    [[new_partner_id]]
)
print("Partner berhasil dihapus")
