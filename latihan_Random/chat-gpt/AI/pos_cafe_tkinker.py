import tkinter as tk
from tkinter import messagebox

# Data menu
menu = {
    'Kopi Hitam': 15000,
    'Cappuccino': 20000,
    'Latte': 22000,
    'Roti Bakar': 18000,
    'Pisang Goreng': 15000,
    'Air Mineral': 8000
}

# Variabel global
pesanan = []
total_harga = 0

# Fungsi menambah pesanan
def tambah_pesanan(nama_item, harga_item):

    try:
        qty = int(entry_qty.get())
        if qty <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Salah", "Masukkan jumlah yang valid (angka > 0).")
        return

    subtotal = harga_item * qty
    pesanan.append((nama_item, harga_item, qty, subtotal))
    total_harga += subtotal

    list_pesanan.insert(tk.END, f"{nama_item} x{qty} = Rp{subtotal:,}")
    label_total.config(text=f"Total: Rp{total_harga:,}")
    entry_qty.delete(0, tk.END)

# Fungsi selesai
def selesai_transaksi():
    global total_harga
    if not pesanan:
        messagebox.showinfo("Kosong", "Belum ada pesanan.")
        return

    struk = "\n=== STRUK ===\n"
    for item in pesanan:
        struk += f"{item[0]} ({item[2]} x Rp{item[1]:,}) = Rp{item[3]:,}\n"
    struk += f"\nTotal Bayar: Rp{total_harga:,}\n"
    messagebox.showinfo("Pembayaran", struk)

    # Reset
    list_pesanan.delete(0, tk.END)
    pesanan.clear()
    global total_harga
    total_harga = 0
    label_total.config(text="Total: Rp0")

# UI setup
root = tk.Tk()
root.title("POS Kafe Sederhana")

# Input jumlah
tk.Label(root, text="Jumlah:").grid(row=0, column=0, padx=5, pady=5)
entry_qty = tk.Entry(root)
entry_qty.grid(row=0, column=1, padx=5, pady=5)

# Tombol menu
row = 1
col = 0
for nama, harga in menu.items():
    btn = tk.Button(root, text=f"{nama}\nRp{harga:,}", width=15, command=lambda n=nama, h=harga: tambah_pesanan(n, h))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        row += 1
        col = 0

# List pesanan
list_pesanan = tk.Listbox(root, width=40)
list_pesanan.grid(row=row+1, column=0, columnspan=3, padx=5, pady=10)

# Label total
label_total = tk.Label(root, text="Total: Rp0", font=("Arial", 12, "bold"))
label_total.grid(row=row+2, column=0, columnspan=2, pady=5)

# Tombol selesai
btn_selesai = tk.Button(root, text="Selesai & Cetak Struk", bg="green", fg="white", command=selesai_transaksi)
btn_selesai.grid(row=row+2, column=2, pady=5)

# Run
root.mainloop()
