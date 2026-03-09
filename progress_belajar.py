import json
import os

class LearningTracker:
    def __init__(self, filename='progress_belajar.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Memuat data dari file json jika ada."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        """Menyimpan data ke file json."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def tambah_topik(self, topik):
        if topik not in self.data:
            self.data[topik] = False
            print(f"Topik '{topik}' berhasil ditambahkan.")
            self.save_data()
        else:
            print("Topik sudah ada dalam daftar.")

    def selesaikan_topik(self, topik):
        if topik in self.data:
            self.data[topik] = True
            print(f"Selamat! Topik '{topik}' telah selesai.")
            self.save_data()
        else:
            print("Topik tidak ditemukan.")

    def tampilkan_progress(self):
        if not self.data:
            print("Daftar belajar masih kosong.")
            return

        total = len(self.data)
        selesai = sum(1 for status in self.data.values() if status)
        persentase = (selesai / total) * 100

        print("\n--- PROGRESS BELAJAR ---")
        for topik, status in self.data.items():
            check = "[X]" if status else "[ ]"
            print(f"{check} {topik}")
        
        # Membuat progress bar sederhana
        bar_length = 20
        filled_length = int(bar_length * selesai // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        print(f"\nProgress: |{bar}| {persentase:.2f}% ({selesai}/{total} topik)")
        print("------------------------\n")

def main():
    tracker = LearningTracker()
    
    while True:
        print("Menu:")
        print("1. Tampilkan Progress")
        print("2. Tambah Topik Belajar")
        print("3. Tandai Topik Selesai")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tracker.tampilkan_progress()
        elif pilihan == '2':
            t = input("Masukkan nama topik baru: ")
            tracker.tambah_topik(t)
        elif pilihan == '3':
            t = input("Masukkan nama topik yang sudah selesai: ")
            tracker.selesaikan_topik(t)
        elif pilihan == '4':
            print("Tetap semangat belajarnya!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
