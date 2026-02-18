from datetime import datetime, timedelta

class Roadmap:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.tasks = []
    
    def tambah_task(self, judul, kategori, deadline_hari):
        deadline = datetime.now() + timedelta(days=deadline_hari)
        self.tasks.append({
            "judul": judul,
            "kategori": kategori,
            "deadline": deadline,
            "selesai": False
        })
    
    def tandai_selesai(self, judul):
        for task in self.tasks:
            if task["judul"] == judul:
                task["selesai"] = True
    
    def tampilkan_progress(self):
        print(f"📌 Roadmap {self.nama} (umur {self.umur} tahun)")
        for t in self.tasks:
            status = "✅ Selesai" if t["selesai"] else "⌛ Belum"
            sisa_hari = (t["deadline"] - datetime.now()).days
            print(f"- {t['judul']} | {t['kategori']} | {status} | Deadline: {t['deadline'].strftime('%d-%m-%Y')} (sisa {sisa_hari} hari)")
        print()

# Contoh penggunaan
if __name__ == "__main__":
    roadmap = Roadmap("Farhan", 25)

    # Tambahkan task berdasarkan roadmap hidup 1 minggu
    roadmap.tambah_task("Shalat tepat waktu", "Spiritual", 7)
    roadmap.tambah_task("Olahraga 20 menit tiap hari", "Kesehatan", 7)
    roadmap.tambah_task("Membaca 10 halaman buku", "Ilmu & Pengembangan Diri", 7)
    roadmap.tambah_task("Belajar modul Odoo baru", "Karir", 7)
    roadmap.tambah_task("Silaturahmi dengan keluarga", "Sosial", 7)

    # Tandai salah satu selesai
    roadmap.tandai_selesai("Shalat tepat waktu")

    # Tampilkan progress
    roadmap.tampilkan_progress()
