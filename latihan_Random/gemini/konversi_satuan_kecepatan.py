def km_to_ms(kecepatan_kmh):
    ''' Mengkonversi kecepatan dari'''
    return kecepatan_kmh * 1000 / 3600

def ms_to_kmh(kecepatan_ms):
    '''Mengkonversi keceptan dari m/s ke km/jam'''
    return kecepatan_ms * 3600 / 1000

pilihan = int(input("Pilih konversi:\n1. km/jam ke m/s\n2. m/s ke km/jam\nPilihan Anda: "))

if pilihan == 1:
    kecepatan_kmh = float(input("Masukkan kecepatan (km/jam): "))
    kecepatan_ms = km_to_ms(kecepatan_kmh)
    print("Kecepatan dalam m/s:", kecepatan_ms)
elif pilihan == 2:
    kecepatan_ms = float(input("Masukan kecepatan (m/s): "))
    kecepatan_kmh = ms_to_kmh(kecepatan_ms)
    print("Kecepatan dalam km/jam", kecepatan_ms)
else:
    print("Pilihan tidak valid")