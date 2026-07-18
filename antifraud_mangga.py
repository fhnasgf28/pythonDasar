"""
Sistem Anti-Kecurangan Dagang Buah Mangga
Program untuk memastikan kualitas dan standar perdagangan buah mangga yang adil
"""

from datetime import datetime
from enum import Enum
import json


class KualitasMangga(Enum):
    """Standar kualitas buah mangga"""
    GRADE_A = "Grade A - Premium"
    GRADE_B = "Grade B - Standar"
    GRADE_C = "Grade C - Ekonomi"
    REJECTED = "Ditolak - Tidak Layak"


class ValidatorMangga:
    """Validator untuk memastikan kualitas dan keaslian buah mangga"""
    
    def __init__(self):
        self.standar_berat = {
            "min": 150,  # gram
            "max": 400   # gram
        }
        self.standar_ukuran = {
            "min_diameter": 7,    # cm
            "max_diameter": 10    # cm
        }
        self.standar_warna = ["kuning", "merah muda", "hijau kekuningan"]
        self.standar_kekerasan = {
            "grade_a": (2, 3),    # skala 1-5
            "grade_b": (3, 4),
            "grade_c": (4, 5)
        }
    
    def cek_berat(self, berat_gram):
        """Validasi berat buah mangga"""
        if self.standar_berat["min"] <= berat_gram <= self.standar_berat["max"]:
            return True, "Berat sesuai standar"
        return False, f"Berat tidak valid. Standar: {self.standar_berat['min']}-{self.standar_berat['max']}g"
    
    def cek_ukuran(self, diameter_cm):
        """Validasi diameter buah mangga"""
        if self.standar_ukuran["min_diameter"] <= diameter_cm <= self.standar_ukuran["max_diameter"]:
            return True, "Ukuran sesuai standar"
        return False, f"Ukuran tidak valid. Standar: {self.standar_ukuran['min_diameter']}-{self.standar_ukuran['max_diameter']}cm"
    
    def cek_warna(self, warna):
        """Validasi warna buah mangga"""
        if warna.lower() in self.standar_warna:
            return True, f"Warna '{warna}' sesuai standar"
        return False, f"Warna tidak standar. Warna valid: {', '.join(self.standar_warna)}"
    
    def cek_kekerasan(self, nilai_kekerasan):
        """Validasi tingkat kekerasan (1-5, dengan 1 paling empuk)"""
        if not 1 <= nilai_kekerasan <= 5:
            return False, "Nilai kekerasan harus antara 1-5"
        return True, f"Kekerasan valid: {nilai_kekerasan}"
    
    def cek_cacat(self, jumlah_cacat, tipe_cacat):
        """Validasi cacat fisik"""
        jenis_cacat_valid = ["bintik", "goresan", "memar", "busuk"]
        
        if tipe_cacat.lower() not in jenis_cacat_valid:
            return False, f"Jenis cacat tidak terdaftar. Valid: {', '.join(jenis_cacat_valid)}"
        
        if jumlah_cacat == 0:
            return True, "Tidak ada cacat"
        elif jumlah_cacat <= 2:
            return True, "Cacat dalam toleransi"
        else:
            return False, "Cacat terlalu banyak"


class PenilaiKualitas:
    """Sistem penilai kualitas buah mangga berdasarkan standar"""
    
    def __init__(self):
        self.validator = ValidatorMangga()
    
    def evaluasi_mangga(self, data_mangga):
        """
        Evaluasi lengkap buah mangga
        
        Args:
            data_mangga (dict): Data buah mangga dengan keys:
                - berat_gram
                - diameter_cm
                - warna
                - kekerasan (1-5)
                - cacat_jumlah
                - cacat_tipe
        """
        hasil_validasi = {
            "timestamp": datetime.now().isoformat(),
            "data_mangga": data_mangga,
            "hasil_pengecekan": {},
            "skor_total": 0,
            "kualitas": None,
            "status": "REJECTED",
            "catatan": []
        }
        
        # Cek berat
        valid, msg = self.validator.cek_berat(data_mangga["berat_gram"])
        hasil_validasi["hasil_pengecekan"]["berat"] = {"valid": valid, "pesan": msg}
        if valid:
            hasil_validasi["skor_total"] += 20
        else:
            hasil_validasi["catatan"].append(f"⚠️ {msg}")
        
        # Cek ukuran
        valid, msg = self.validator.cek_ukuran(data_mangga["diameter_cm"])
        hasil_validasi["hasil_pengecekan"]["ukuran"] = {"valid": valid, "pesan": msg}
        if valid:
            hasil_validasi["skor_total"] += 20
        else:
            hasil_validasi["catatan"].append(f"⚠️ {msg}")
        
        # Cek warna
        valid, msg = self.validator.cek_warna(data_mangga["warna"])
        hasil_validasi["hasil_pengecekan"]["warna"] = {"valid": valid, "pesan": msg}
        if valid:
            hasil_validasi["skor_total"] += 20
        else:
            hasil_validasi["catatan"].append(f"⚠️ {msg}")
        
        # Cek kekerasan
        valid, msg = self.validator.cek_kekerasan(data_mangga["kekerasan"])
        hasil_validasi["hasil_pengecekan"]["kekerasan"] = {"valid": valid, "pesan": msg}
        if valid:
            hasil_validasi["skor_total"] += 20
        else:
            hasil_validasi["catatan"].append(f"⚠️ {msg}")
        
        # Cek cacat
        valid, msg = self.validator.cek_cacat(
            data_mangga["cacat_jumlah"],
            data_mangga["cacat_tipe"]
        )
        hasil_validasi["hasil_pengecekan"]["cacat"] = {"valid": valid, "pesan": msg}
        if valid:
            hasil_validasi["skor_total"] += 20
        else:
            hasil_validasi["catatan"].append(f"⚠️ {msg}")
        
        # Tentukan grade berdasarkan skor
        if hasil_validasi["skor_total"] == 100:
            hasil_validasi["kualitas"] = KualitasMangga.GRADE_A
            hasil_validasi["status"] = "APPROVED - GRADE A"
        elif hasil_validasi["skor_total"] >= 80:
            hasil_validasi["kualitas"] = KualitasMangga.GRADE_B
            hasil_validasi["status"] = "APPROVED - GRADE B"
        elif hasil_validasi["skor_total"] >= 60:
            hasil_validasi["kualitas"] = KualitasMangga.GRADE_C
            hasil_validasi["status"] = "APPROVED - GRADE C"
        else:
            hasil_validasi["kualitas"] = KualitasMangga.REJECTED
            hasil_validasi["status"] = "REJECTED"
        
        return hasil_validasi


class SistemDagangMangga:
    """Sistem terintegrasi untuk mengelola perdagangan buah mangga yang jujur"""
    
    def __init__(self):
        self.penilai = PenilaiKualitas()
        self.riwayat_transaksi = []
        self.log_kecurangan = []
    
    def deteksi_kecurangan(self, data_mangga, harga_per_kg):
        """Deteksi potensi kecurangan dalam transaksi"""
        anomali = []
        
        # Cek harga yang mencurigakan
        harga_normal = 15000  # Rp per kg (estimasi)
        if harga_per_kg < harga_normal * 0.5:
            anomali.append(f"🚨 HARGA MENCURIGAKAN: Rp{harga_per_kg}/kg (jauh di bawah standar)")
        elif harga_per_kg > harga_normal * 3:
            anomali.append(f"🚨 HARGA MENCURIGAKAN: Rp{harga_per_kg}/kg (jauh di atas standar)")
        
        # Cek kombinasi data yang tidak logis
        if data_mangga["berat_gram"] < 200 and data_mangga["kekerasan"] <= 2:
            anomali.append("⚠️ KOMBINASI TIDAK LOGIS: Buah kecil tapi sangat empuk (tanda cacat)")
        
        if data_mangga["cacat_jumlah"] > 0 and harga_per_kg >= 20000:
            anomali.append("⚠️ KECURANGAN MUNGKIN: Buah cacat dijual dengan harga premium")
        
        return anomali
    
    def proses_transaksi(self, data_mangga, harga_per_kg, jumlah_kg, pembeli_id):
        """Proses transaksi perdagangan mangga"""
        evaluasi = self.penilai.evaluasi_mangga(data_mangga)
        anomali = self.deteksi_kecurangan(data_mangga, harga_per_kg)
        
        transaksi = {
            "timestamp": datetime.now().isoformat(),
            "pembeli_id": pembeli_id,
            "evaluasi_kualitas": evaluasi,
            "harga_per_kg": harga_per_kg,
            "jumlah_kg": jumlah_kg,
            "total_harga": harga_per_kg * jumlah_kg,
            "anomali_terdeteksi": anomali,
            "status_transaksi": "DITOLAK" if anomali or evaluasi["status"] == "REJECTED" else "DISETUJUI"
        }
        
        self.riwayat_transaksi.append(transaksi)
        
        if anomali:
            self.log_kecurangan.append({
                "timestamp": datetime.now().isoformat(),
                "pembeli_id": pembeli_id,
                "anomali": anomali
            })
        
        return transaksi
    
    def laporan_summary(self):
        """Generate laporan ringkasan"""
        total_transaksi = len(self.riwayat_transaksi)
        transaksi_disetujui = sum(1 for t in self.riwayat_transaksi if t["status_transaksi"] == "DISETUJUI")
        transaksi_ditolak = total_transaksi - transaksi_disetujui
        kecurangan_terdeteksi = len(self.log_kecurangan)
        
        return {
            "total_transaksi": total_transaksi,
            "transaksi_disetujui": transaksi_disetujui,
            "transaksi_ditolak": transaksi_ditolak,
            "kecurangan_terdeteksi": kecurangan_terdeteksi,
            "tingkat_keberhasilan": f"{(transaksi_disetujui/total_transaksi*100):.1f}%" if total_transaksi > 0 else "0%"
        }


# Contoh penggunaan
if __name__ == "__main__":
    print("=" * 60)
    print("SISTEM ANTI-KECURANGAN DAGANG BUAH MANGGA")
    print("=" * 60)
    
    sistem = SistemDagangMangga()
    
    # Contoh 1: Buah mangga berkualitas Grade A
    print("\n📋 TRANSAKSI 1: Buah Mangga Grade A")
    print("-" * 60)
    mangga_bagus = {
        "berat_gram": 280,
        "diameter_cm": 8.5,
        "warna": "kuning",
        "kekerasan": 2,
        "cacat_jumlah": 0,
        "cacat_tipe": "tidak ada"
    }
    transaksi1 = sistem.proses_transaksi(mangga_bagus, 20000, 5, "PEMBELI001")
    print(json.dumps(transaksi1, indent=2, ensure_ascii=False))
    
    # Contoh 2: Buah mangga berkualitas rendah
    print("\n📋 TRANSAKSI 2: Buah Mangga Grade C (Cacat)")
    print("-" * 60)
    mangga_jelek = {
        "berat_gram": 150,
        "diameter_cm": 7,
        "warna": "hijau kekuningan",
        "kekerasan": 4,
        "cacat_jumlah": 3,
        "cacat_tipe": "memar"
    }
    transaksi2 = sistem.proses_transaksi(mangga_jelek, 8000, 3, "PEMBELI002")
    print(json.dumps(transaksi2, indent=2, ensure_ascii=False))
    
    # Contoh 3: Potensi kecurangan (harga tidak wajar)
    print("\n📋 TRANSAKSI 3: DETEKSI KECURANGAN - Harga Mencurigakan")
    print("-" * 60)
    mangga_mencurigakan = {
        "berat_gram": 350,
        "diameter_cm": 9,
        "warna": "merah muda",
        "kekerasan": 2,
        "cacat_jumlah": 0,
        "cacat_tipe": "tidak ada"
    }
    transaksi3 = sistem.proses_transaksi(mangga_mencurigakan, 45000, 2, "PEMBELI003")
    print(json.dumps(transaksi3, indent=2, ensure_ascii=False))
    
    # Laporan ringkasan
    print("\n" + "=" * 60)
    print("LAPORAN RINGKASAN")
    print("=" * 60)
    laporan = sistem.laporan_summary()
    for key, value in laporan.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n✅ Sistem anti-kecurangan berfungsi dengan baik!")
