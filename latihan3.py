def hitung_konversi_suhu(suhu_input, satuan_asal, satuan_target):
    if satuan_asal == "C" and satuan_target == "F":
        return suhu_input * 9 / 5 + 32
    elif satuan_asal == "C" and satuan_target == "R":
        return suhu_input * 4 / 5
    elif satuan_asal == "C" and satuan_target == "K":
        return suhu_input + 273
    elif satuan_asal == "F" and satuan_target == "C":
        return (suhu_input - 32) * 5 / 9
    elif satuan_asal == "F" and satuan_target == "R":
        return (suhu_input - 32) * 4 / 9 + 273
    elif satuan_asal == "F" and satuan_target == "K":
        return (suhu_input - 32) * 5 / 9 + 273
    elif satuan_asal == "R" and satuan_target == "C":
        return suhu_input * 5 / 4 - 273
    elif satuan_asal == "R" and satuan_target == "F":
        return suhu_input * 9 / 4 - 460
    elif satuan_asal == "R" and satuan_target == "K":
        return suhu_input * 5 / 4
    elif satuan_asal == "K" and satuan_target == "C":
        return suhu_input - 273
    elif satuan_asal == "K" and satuan_target == "F":
        return (suhu_input - 273) * 9 / 5 + 32
    elif satuan_asal == "K" and satuan_target == "R":
        return (suhu_input - 273) * 4 / 5 + 273


def main():
    suhu_input = float(input("Masukan suhu:"))
    satuan_asal = input("Dari satuan:")
    satuan_target = input("Ke satuan:")

    konversi = hitung_konversi_suhu(suhu_input, satuan_asal, satuan_target)

    print("Suhu {} adalah {} {}".format(suhu_input, konversi, satuan_target))


if __name__ == "__main__":
    main()
