import json 

# nama file untk menyimpan daftar kontak 
filename = "daftar_kontak.json"

# fungsi untuk memuat kontak dari file JSON
def load_contacts():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# fungsi untuk menyimpan kontak ke file JSON 
def save_contacts(contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# fungsi untuk menambahkan kontak baru
def add_contact(contacts):
    name = input("Masukkan nama kontak: ")
    phone = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    address = input("Masukkan alamat: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print(f"Kontak {name} berhasil ditambahkan.")

def display_contacts(contacts):
    if not contacts:
        print("Daftar kontak kosong.")
        return
    
    for contact in contacts:
        print(f"Nama: {contact['name']}")
        print(f"Telepon: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Alamat: {contact['address']}")

def search_contacts(contacts):
    search_term = input("Masukkan kata kunci pencarian: ")
    results = [c for c in contacts if search_term.lower() in c["name"].lower() or search_term in c["phone"]]

    if results:
        print("Kontak ditemukan:")
        for contact in results:
            print(f"Nama: {contact['name']}")
            print(f"Telepon: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Alamat: {contact['address']}")
    else:
        print("Kontak tidak ditemukan.")

# fungsi untuk menghapus kontak berdasarkan nama
def delete_contact(contacts):
    name = input("Masukkan nama kontak yang ingin dihapus: ")
    initial_len = len(contacts)
    contacts = [c for c in contacts if c["name"].lower() != name.lower()]

    if len(contacts) < initial_len:
        save_contacts(contacts)
        print(f"Kontak {name} berhasil dihapus.")
    else:
        print(f"Kontak {name} tidak ditemukan.")
    return contacts


# fungsi utama program
def main():
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Lihat Daftar Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            contacts = delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    
# menjalankan program
if __name__ == "__main__":
    main()