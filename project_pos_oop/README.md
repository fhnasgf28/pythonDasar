# Project POS OOP Python

Project ringan untuk latihan **Object-Oriented Programming (OOP)** dengan studi kasus **Point of Sale (POS)**.

## Konsep OOP yang Dipakai

- `Product` untuk menyimpan data barang.
- `CartItem` untuk item belanja di keranjang.
- `ShoppingCart` untuk mengelola tambah barang dan subtotal.
- `PercentageDiscount` untuk menghitung diskon persentase.
- `POSTransaction` untuk proses checkout dan pembuatan struk.

## Cara Menjalankan

Dari root repo:

```bash
python3 project_pos_oop/main.py
```

## Menjalankan Test

```bash
python3 -m unittest project_pos_oop.test_main
```

## Contoh Output

```text
========= STRUK POS =========
Kopi Susu x2        Rp 36,000
Roti Coklat x3      Rp 45,000
Air Mineral x1      Rp  5,000
-----------------------------
Subtotal            Rp 86,000
Diskon              Rp  8,600
Total               Rp 77,400
Bayar               Rp100,000
Kembalian           Rp 22,600
=============================
```
