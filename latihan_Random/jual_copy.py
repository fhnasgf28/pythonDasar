def hitung_harga_jual_copy(modal_kertas, modal_tinta, biaya_operasional, margin_keuntungan_persen):
    """
    Menghitung harga jual per lembar fotokopi.

    Args:
        modal_kertas (float): Harga modal per lembar kertas.
        modal_tinta (float): Harga modal tinta/toner per lembar.
        biaya_operasional (float): Estimasi biaya listrik, sewa, tenaga kerja, dan penyusutan mesin per lembar.
        margin_keuntungan_persen (float): Persentase keuntungan yang diinginkan (contoh: 50 untuk 50%).

    Returns:
        float: Harga jual yang disarankan.
    """
    total_modal = modal_kertas + modal_tinta + biaya_operasional
    keuntungan = total_modal * (margin_keuntungan_persen / 100)
    harga_jual = total_modal + keuntungan

    return harga_jual

# Contoh Penggunaan
if __name__ == "__main__":
    # Misalkan:
    # 1 rim (500 lembar) kertas harganya Rp 50.000 -> 50.000 / 500 = Rp 100 per lembar
    # 1 cartridge toner Rp 200.000 bisa untuk 2000 lembar -> 200.000 / 2000 = Rp 100 per lembar
    # Listrik, penyusutan mesin, sewa dll per lembar kira-kira Rp 50
    # Kita ingin untung 100% (dua kali lipat dari total modal)
    
    kertas = 100.0
    tinta = 100.0
    operasional = 50.0
    margin = 100.0 # dalam persen
    
    total_modal_per_lembar = kertas + tinta + operasional
    harga_jual = hitung_harga_jual_copy(kertas, tinta, operasional, margin)
    
    print("-" * 40)
    print("KALKULATOR HARGA JUAL FOTOKOPI")
    print("-" * 40)
    print(f"Modal Kertas       : Rp {kertas}")
    print(f"Modal Tinta/Toner  : Rp {tinta}")
    print(f"Biaya Operasional  : Rp {operasional}")
    print("-" * 40)
    print(f"Total Modal/Lembar : Rp {total_modal_per_lembar}")
    print(f"Margin Keuntungan  : {margin}%")
    print(f"Harga Jual/Lembar  : Rp {harga_jual}")
    
    # Biasanya harga fotokopi dibulatkan ke atas, misalnya kelipatan Rp 50 atau Rp 100
    # Contoh pembulatan ke kelipatan Rp 100 terdekat ke atas
    harga_jual_bulat = ((int(harga_jual) + 99) // 100) * 100
    print(f"Harga Jual Bulat   : Rp {harga_jual_bulat}")
    print("-" * 40)
