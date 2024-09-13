def calculate_sales():
    # Meminta jumlah hari penjualan
    num_days = int(input("Masukkan jumlah hari penjualan: "))

    total_kg = 0
    total_revenue = 0.0
    total_price_per_kg = 0.0

    # Loop untuk setiap hari penjualan
    for day in range(1, num_days + 1):
        print(f"\nHari ke-{day}:")

        # Meminta jumlah kilogram mangga yang terjual
        kg_sold = float(input("Masukkan jumlah kilogram mangga yang terjual: "))

        # Meminta harga per kilogram mangga
        price_per_kg = float(input("Masukkan harga per kilogram mangga: "))

        # Menghitung pendapatan hari ini
        daily_revenue = kg_sold * price_per_kg

        # Mengupdate total penjualan dan pendapatan
        total_kg += kg_sold
        total_revenue += daily_revenue
        total_price_per_kg += price_per_kg

    # Menghitung rata-rata harga per kilogram
    average_price_per_kg = total_price_per_kg / num_days

    # Menampilkan hasil
    print("\nHasil Penjualan:")
    print(f"Total kilogram mangga terjual: {total_kg} kg")
    print(f"Total pendapatan: Rp {total_revenue}")
    print(f"Rata-rata harga per kilogram: Rp {average_price_per_kg:.2f}")


# Menjalankan fungsi
calculate_sales()
