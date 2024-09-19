def calculate_families():
    # Meminta input jumlah keluarga di daerah tersebut
    num_families = int(input("Masukkan jumlah keluarga di daerah tersebut: "))

    total_members = 0

    # Loop untuk meminta jumlah anggota keluarga di setiap keluarga
    for family in range(1, num_families + 1):
        print(f"\nKeluarga ke-{family}:")

        # Meminta input jumlah anggota keluarga untuk keluarga ke-X
        num_members = int(input("Masukkan jumlah anggota keluarga: "))

        # Menambahkan jumlah anggota keluarga ke total
        total_members += num_members

    # Menghitung rata-rata jumlah anggota per keluarga
    average_members_per_family = total_members / num_families

    # Menampilkan hasil
    print("\nHasil Perhitungan:")
    print(f"Total keluarga: {num_families}")
    print(f"Total anggota keluarga: {total_members}")
    print(f"Rata-rata jumlah anggota per keluarga: {average_members_per_family:.2f}")


# Menjalankan fungsi
calculate_families()
