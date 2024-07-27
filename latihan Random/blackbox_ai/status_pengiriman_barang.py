status_pengiriman = {
    "1": "Pengiriman sedang diproses",
    "2": "Pengiriman sedang dalam perjalanan",
    "3": "Pengiriman telah samapi",
    "4": "Pengiriman gagal",
}


def cek_status(no_resi):
    # simulasikan status pengiriman berdasarkan no resi
    if no_resi == '1234567':
        return status_pengiriman['2']
    elif no_resi == "780909":
        return status_pengiriman['3']
    else:
        return status_pengiriman['1']


def main():
    print("Selamat datang di sistem pelacakan pengiriman")
    no_resi = input("Masukkan nomor resi pengirimn: ")
    status = cek_status(no_resi)
    print(f"Status Pengiriman : {status}")


if __name__ == "__main__":
    main()
