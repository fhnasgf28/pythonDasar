import xmlrpc.client
import random
from datetime import datetime, timedelta

# ================= KONFIGURASI ODOO =================
URL = 'http://localhost:8069'
DB = 'mln_new'  # Ganti dengan nama DB Anda
USER = 'admin'  # Ganti dengan email login Anda
PASSWORD = 'admin'  # Ganti dengan password Anda


# ====================================================

def main():
    try:
        print("Mulai proses autentikasi...")
        common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
        uid = common.authenticate(DB, USER, PASSWORD, {})

        if not uid:
            print("❌ Login gagal! Cek kembali konfigurasi Anda.")
            return

        print(f"✅ Login berhasil! UID: {uid}")
        models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

        # --- 0. AMBIL COMPANY ID ---
        print("\n[0/5] Mengambil data Perusahaan (Company)...")
        user_data = models.execute_kw(DB, uid, PASSWORD, 'res.users', 'read', [[uid]], {'fields': ['company_id']})
        company_id = user_data[0]['company_id'][0]

        # --- 1. SETUP PRICELIST ---
        print("\n[1/5] Mengecek/Membuat Pricelist...")
        pricelist_ids = models.execute_kw(DB, uid, PASSWORD, 'product.pricelist', 'search',
                                          [[('company_id', 'in', [False, company_id])]], {'limit': 1})
        if not pricelist_ids:
            pricelist_id = models.execute_kw(DB, uid, PASSWORD, 'product.pricelist', 'create',
                                             [{'name': 'Dummy Pricelist', 'company_id': company_id}])
        else:
            pricelist_id = pricelist_ids[0]

        # --- 2. SETUP WAREHOUSE ---
        print("\n[2/5] Mengecek/Membuat Warehouse (Gudang)...")
        warehouse_ids = models.execute_kw(DB, uid, PASSWORD, 'stock.warehouse', 'search',
                                          [[('company_id', '=', company_id)]], {'limit': 1})
        if not warehouse_ids:
            warehouse_id = models.execute_kw(DB, uid, PASSWORD, 'stock.warehouse', 'create',
                                             [{'name': 'Dummy Warehouse', 'code': 'DWH', 'company_id': company_id}])
        else:
            warehouse_id = warehouse_ids[0]

        # --- 3. CREATE CUSTOMERS ---
        print("\n[3/5] Mengecek/Membuat 10 Data Customer dummy...")
        partner_ids = models.execute_kw(DB, uid, PASSWORD, 'res.partner', 'search',
                                        [[('company_id', 'in', [False, company_id]), ('customer_rank', '>', 0)]],
                                        {'limit': 10})
        if len(partner_ids) < 10:
            for i in range(1, 11 - len(partner_ids)):
                p_id = models.execute_kw(DB, uid, PASSWORD, 'res.partner', 'create', [{
                    'name': f'Dummy PT Customer {i}', 'is_company': True, 'company_id': company_id, 'customer_rank': 1
                }])
                partner_ids.append(p_id)

        # --- 4. CREATE PRODUCTS ---
        print("\n[4/5] Mengecek/Membuat 10 Data Product dummy...")
        product_ids = models.execute_kw(DB, uid, PASSWORD, 'product.product', 'search',
                                        [[('company_id', 'in', [False, company_id]), ('type', '=', 'consu')]],
                                        {'limit': 10})
        if len(product_ids) < 10:
            for i in range(1, 11 - len(product_ids)):
                prod_id = models.execute_kw(DB, uid, PASSWORD, 'product.product', 'create', [{
                    'name': f'Dummy Product {i}', 'type': 'consu', 'company_id': company_id,
                    'list_price': random.randint(10, 100) * 10000
                }])
                product_ids.append(prod_id)

        # --- 5. CREATE SALES ORDERS ---
        print("\n[5/5] Membuat 100 Data Sales Order dummy...")
        success_so = 0
        for i in range(1, 101):
            partner_id = random.choice(partner_ids)
            validity_date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')

            # === PERBAIKAN LOGIC ORDER LINE DI SINI ===
            order_lines = []
            jumlah_baris = random.randint(1, 3)

            # Ambil produk secara acak tapi PASTI UNIK, tidak akan ada yang dobel
            selected_products = random.sample(product_ids, jumlah_baris)

            for prod_id in selected_products:
                order_lines.append((0, 0, {
                    'product_id': prod_id,
                    'product_uom_qty': random.randint(1, 5),
                    'company_id': company_id
                }))
            # ==========================================

            so_data = {
                'partner_id': partner_id,
                'partner_invoice_id': partner_id,
                'partner_shipping_id': partner_id,
                'validity_date': validity_date,
                'pricelist_id': pricelist_id,
                'warehouse_id': warehouse_id,
                'company_id': company_id,
                'client_order_ref': f'DUMMY-SO-{i:03d}',
                'order_line': order_lines
            }

            try:
                models.execute_kw(DB, uid, PASSWORD, 'sale.order', 'create', [so_data])
                success_so += 1
                if success_so % 10 == 0:
                    print(f"   ➜ Progress: {success_so}/100 SO dibuat...")
            except Exception as e:
                print(f"⚠️ Gagal membuat SO ke-{i}: {e}")
                break

        if success_so > 0:
            print(f"\n🎉 SELESAI! {success_so} data dummy SO berhasil di-import ke Odoo.")
        else:
            print("\n❌ Gagal membuat Sales Order. Silakan cek pesan error di atas.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan fatal: {e}")


if __name__ == "__main__":
    main()