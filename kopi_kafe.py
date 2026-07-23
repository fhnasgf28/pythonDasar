"""
Sistem Takaran Kopi Kafe
Program untuk menghitung takaran kopi dan biaya di kafe
"""

class TakaranKopi:
    """Kelas untuk mengelola takaran kopi dan perhitungan biaya"""
    
    def __init__(self):
        # Harga per gram kopi
        self.harga_per_gram = 500  # Rp per gram
        
        # Takaran standar kopi (dalam gram)
        self.takaran_standar = {
            'espresso': 18,
            'americano': 18,
            'cappuccino': 18,
            'latte': 18,
            'flat_white': 20,
            'macchiato': 10,
            'cortado': 15,
            'custom': None
        }
        
        # Harga per jenis kopi
        self.harga_kopi = {
            'espresso': 25000,
            'americano': 20000,
            'cappuccino': 30000,
            'latte': 32000,
            'flat_white': 35000,
            'macchiato': 22000,
            'cortado': 24000,
            'custom': None
        }
    
    def hitung_biaya_kopi(self, jenis_kopi, gram_kopi=None):
        """
        Menghitung biaya kopi berdasarkan jenis atau takaran custom
        
        Args:
            jenis_kopi (str): Jenis kopi yang dipesan
            gram_kopi (float): Takaran kopi dalam gram (untuk custom)
        
        Returns:
            dict: Dictionary berisi informasi takaran dan biaya
        """
        jenis_kopi = jenis_kopi.lower()
        
        if jenis_kopi not in self.takaran_standar:
            return {
                'status': 'error',
                'pesan': f'Jenis kopi "{jenis_kopi}" tidak tersedia'
            }
        
        # Jika custom, gunakan gram yang diberikan
        if jenis_kopi == 'custom':
            if gram_kopi is None:
                return {
                    'status': 'error',
                    'pesan': 'Untuk custom, harus menyertakan takaran gram'
                }
            takaran = gram_kopi
            harga = gram_kopi * self.harga_per_gram
        else:
            takaran = self.takaran_standar[jenis_kopi]
            harga = self.harga_kopi[jenis_kopi]
        
        return {
            'status': 'sukses',
            'jenis_kopi': jenis_kopi,
            'takaran_gram': takaran,
            'harga': harga,
            'biaya_kopi': takaran * self.harga_per_gram
        }
    
    def hitung_biaya_multiple(self, pesanan_list):
        """
        Menghitung biaya untuk multiple pesanan
        
        Args:
            pesanan_list (list): List berisi dict pesanan
                                 {'jenis': 'cappuccino', 'jumlah': 2}
        
        Returns:
            dict: Dictionary berisi detail pesanan dan total biaya
        """
        total_biaya = 0
        detail_pesanan = []
        
        for pesanan in pesanan_list:
            jenis = pesanan.get('jenis', 'custom')
            jumlah = pesanan.get('jumlah', 1)
            gram_custom = pesanan.get('gram', None)
            
            hasil = self.hitung_biaya_kopi(jenis, gram_custom)
            
            if hasil['status'] == 'sukses':
                biaya_item = hasil['harga'] * jumlah
                total_biaya += biaya_item
                
                detail_pesanan.append({
                    'jenis_kopi': hasil['jenis_kopi'],
                    'takaran': hasil['takaran_gram'],
                    'jumlah': jumlah,
                    'harga_satuan': hasil['harga'],
                    'subtotal': biaya_item
                })
            else:
                detail_pesanan.append({
                    'status': 'error',
                    'pesan': hasil['pesan']
                })
        
        return {
            'detail_pesanan': detail_pesanan,
            'total_biaya': total_biaya,
            'diskon': 0,
            'total_pembayaran': total_biaya
        }
    
    def hitung_diskon(self, total_biaya, persen_diskon=0, nominal_diskon=0):
        """
        Menghitung diskon dari total biaya
        
        Args:
            total_biaya (float): Total biaya
            persen_diskon (float): Diskon dalam persen
            nominal_diskon (float): Diskon dalam nominal
        
        Returns:
            dict: Dictionary berisi detail perhitungan diskon
        """
        diskon_persen_nominal = (total_biaya * persen_diskon) / 100
        total_diskon = diskon_persen_nominal + nominal_diskon
        total_pembayaran = total_biaya - total_diskon
        
        return {
            'total_biaya': total_biaya,
            'diskon_persen': persen_diskon,
            'diskon_nominal_persen': diskon_persen_nominal,
            'diskon_nominal': nominal_diskon,
            'total_diskon': total_diskon,
            'total_pembayaran': max(0, total_pembayaran)
        }
    
    def tampilkan_menu(self):
        """Menampilkan menu kopi yang tersedia"""
        print("\n" + "="*50)
        print("MENU KOPI KAFE")
        print("="*50)
        print(f"{'Jenis Kopi':<20} {'Takaran':<12} {'Harga':<15}")
        print("-"*50)
        
        for jenis, harga in self.harga_kopi.items():
            if jenis != 'custom':
                takaran = self.takaran_standar[jenis]
                print(f"{jenis:<20} {takaran}g{'':<8} Rp {harga:>10,.0f}")
        
        print("-"*50)
        print(f"{'Custom':<20} {'Custom':<12} Rp 500/gram")
        print("="*50 + "\n")


def main():
    """Fungsi utama untuk menjalankan program"""
    kopi = TakaranKopi()
    
    # Tampilkan menu
    kopi.tampilkan_menu()
    
    # Contoh 1: Pesanan single
    print("\n--- CONTOH 1: Pesanan Single ---")
    hasil1 = kopi.hitung_biaya_kopi('cappuccino')
    print(f"Jenis: {hasil1['jenis_kopi']}")
    print(f"Takaran: {hasil1['takaran_gram']}g")
    print(f"Harga: Rp {hasil1['harga']:,.0f}")
    
    # Contoh 2: Pesanan custom
    print("\n--- CONTOH 2: Pesanan Custom (25 gram) ---")
    hasil2 = kopi.hitung_biaya_kopi('custom', 25)
    print(f"Jenis: Custom")
    print(f"Takaran: {hasil2['takaran_gram']}g")
    print(f"Harga: Rp {hasil2['harga']:,.0f}")
    
    # Contoh 3: Multiple pesanan
    print("\n--- CONTOH 3: Multiple Pesanan ---")
    pesanan = [
        {'jenis': 'cappuccino', 'jumlah': 2},
        {'jenis': 'americano', 'jumlah': 1},
        {'jenis': 'latte', 'jumlah': 3}
    ]
    
    hasil3 = kopi.hitung_biaya_multiple(pesanan)
    print(f"{'Pesanan':<20} {'Qty':<5} {'Harga':<15} {'Subtotal':<15}")
    print("-"*55)
    
    for item in hasil3['detail_pesanan']:
        if 'jenis_kopi' in item:
            print(f"{item['jenis_kopi']:<20} {item['jumlah']:<5} "
                  f"Rp {item['harga_satuan']:>10,.0f}  "
                  f"Rp {item['subtotal']:>10,.0f}")
    
    print("-"*55)
    print(f"Total Biaya: Rp {hasil3['total_biaya']:,.0f}")
    
    # Contoh 4: Dengan diskon
    print("\n--- CONTOH 4: Dengan Diskon (10%) ---")
    total = hasil3['total_biaya']
    hasil4 = kopi.hitung_diskon(total, persen_diskon=10)
    print(f"Total Biaya: Rp {hasil4['total_biaya']:,.0f}")
    print(f"Diskon (10%): Rp {hasil4['diskon_nominal_persen']:,.0f}")
    print(f"Total Pembayaran: Rp {hasil4['total_pembayaran']:,.0f}")


if __name__ == "__main__":
    main()
