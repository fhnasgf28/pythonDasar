def hitung_ukuran_baju_v2(lingkar_dada, lingkar_pinggang, tinggi_badan):
    """
    Menghitung ukuran baju dengan sistem scoring.
    """
    
    ukuran_data = {
        'XS': {'dada': 78.5, 'pinggang': 63.5, 'tinggi': 160},
        'S': {'dada': 83.5, 'pinggang': 68.5, 'tinggi': 165},
        'M': {'dada': 91, 'pinggang': 76, 'tinggi': 170},
        'L': {'dada': 101, 'pinggang': 86, 'tinggi': 175},
        'XL': {'dada': 111, 'pinggang': 96, 'tinggi': 180},
        'XXL': {'dada': 121, 'pinggang': 106, 'tinggi': 185}
    }
    
    # Hitung selisih dan score
    scores = {}
    for ukuran, data in ukuran_data.items():
        selisih = abs(data['dada'] - lingkar_dada) + \
                  abs(data['pinggang'] - lingkar_pinggang) + \
                  abs(data['tinggi'] - tinggi_badan)
        scores[ukuran] = selisih
    
    # Ukuran dengan score terendah adalah yang paling sesuai
    ukuran_terbaik = min(scores, key=scores.get)
    return ukuran_terbaik


# Contoh penggunaan v2
lingkar_dada = 90
lingkar_pinggang = 75
tinggi_badan = 172

print(f"Ukuran baju: {hitung_ukuran_baju_v2(lingkar_dada, lingkar_pinggang, tinggi_badan)}")
