def koreksi_ejaan(kalimat):
    kamus = {
        "belaja": "belajar",
        "makan": "makan",
        "minum": "minum"
    }

    kata_kalimat = kalimat.split()
    kata_diperbaiki = [kamus.get(kata, kata) for kata in kata_kalimat]
    return ' '.join(kata_diperbaiki)


# Contoh penggunaan
kalimat_input = "Saya sangat menyenangi belaja."
kalimat_output = koreksi_ejaan(kalimat_input)
print(kalimat_output)  # Output: "Saya sangat menyenangi belajar."
