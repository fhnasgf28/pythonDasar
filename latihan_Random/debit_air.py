def hitung_debit_air(volume, waktu):
    """
    Menghitung debit air dengan rumus Q = V / t
    
    Args:
        volume: Volume air dalam liter
        waktu: Waktu dalam detik
    
    Returns:
        Debit air dalam liter/detik
    """
    if waktu == 0:
        return "Error: Waktu tidak boleh 0"
    
    debit = volume / waktu
    return debit

# Contoh penggunaan
volume = 100  # liter
waktu = 50    # detik

debit = hitung_debit_air(volume, waktu)
print(f"Volume: {volume} liter")
print(f"Waktu: {waktu} detik")
print(f"Debit air: {debit} liter/detik")
print(f"Debit air: {debit * 60} liter/menit")
print(f"Debit air: {debit * 3600} liter/jam")
