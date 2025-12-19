from odoo import models, fields, api

class ProcessBarcode(models.Model):
    _name = 'process.barcode'
    _description = 'Process Barcode'


    def process_barcode(self, barcode):
        """Proses scan barcode dan otomatis isi lot_id di move_line"""
        print("\n" + "=" * 50)
        print("🔄  DEBUG SCAN BARCODE - MULAI PROSES  🔄")
        print(f"📋 Barcode yang discan: {barcode}")
        print("=" * 50)

        # Simpan barcode sementara
        self.sh_stock_barcode_mobile = barcode
        print(f"💾 Barcode disimpan ke field sementara")

        # Cari lot berdasarkan barcode
        print(f"\n🔍 Mencari lot dengan barcode: {barcode}")
        lot = self.env['stock.production.lot'].search([('name', '=', barcode)], limit=1)

        if not lot:
            print("\n" + "❌" * 10 + " ERROR " + "❌" * 10)
            print(f"🚨 LOT TIDAK DITEMUKAN! 🚨")
            print(f"🔍 Barcode: {barcode}")
            print("ℹ️  Kemungkinan penyebab:")
            print("   - Barcode belum terdaftar di sistem")
            print("   - Terjadi kesalahan penulisan barcode")
            print("   - Produk belum memiliki lot number")
            print("   - Izin akses tidak mencukupi")
            print("❌" * 25)
            print("🔄 Silakan coba lagi dengan barcode yang valid")

            return

        print(f"\n✅ LOT DITEMUKAN")
        print(f"   - Nama Lot: {lot.name}")
        print(f"   - ID Lot: {lot.id}")
        print(f"   - Produk: {lot.product_id.display_name}")

        found_moves = False
        print("\n🔎 Mencari move lines yang sesuai...")

        for move in self.move_lines:
            if move.product_id.tracking == 'lot':
                empty_lines = move.move_line_nosuggest_ids.filtered(
                    lambda r: r.lot_name == False)

                if empty_lines:
                    found_moves = True
                    print(f"\n📦 Move ID: {move.id}")
                    print(f"   - Produk: {move.product_id.display_name}")
                    print(f"   - Jumlah line kosong: {len(empty_lines)}")

                    for line in empty_lines:
                        vals_line = {'lot_id': lot.id}
                        print(f"\n   🏷️  Menambahkan lot ke move line {line.id}")
                        print(f"   📝 Update data: {vals_line}")

                        move.update({
                            'move_line_nosuggest_ids': [(1, line.id, vals_line)]
                        })
                        line.lot_id = lot.id

                        print(f"   ✅ Berhasil menambahkan lot {lot.name}")
                        print(f"   📌 Status terbaru:")
                        print(f"      - Lot ID: {line.lot_id.id if line.lot_id else 'None'}")
                        print(f"      - Lot Name: {line.lot_name or 'None'}")
                else:
                    print(f"\nℹ️  Tidak ada line kosong di move ID {move.id}")
            else:
                print(f"\nℹ️  Produk {move.product_id.display_name} tidak memerlukan tracking lot")

        if not found_moves:
            print("\n" + "⚠️" * 15)
            print("TIDAK ADA MOVE LINE YANG COCOK")
            print("TIDAK ADA YANG DIPROSES")
            print("⚠️" * 15)

        print("\n" + "=" * 50)
        print("🏁  PROSES SCAN BARCODE SELESAI  🏁")
        print("=" * 50 + "\n")
        print("percobaan ke 100 kali")