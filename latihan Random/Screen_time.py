# main.py
import pygetwindow as gw
import time
import json
from datetime import datetime

# --- Konfigurasi ---
DATA_FILE = "screen_time_data.json" # File untuk menyimpan data
POLL_INTERVAL = 1 # Detik. Seberapa sering memeriksa jendela aktif.

def load_data():
    """Memuat data dari file JSON. Jika file tidak ada, kembalikan dictionary kosong."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Menyimpan data ke file JSON."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def track_screen_time():
    """Fungsi utama untuk melacak screen time."""
    data = load_data()
    active_window_title = ""
    start_time = time.time()

    print("🚀 Pelacak Screen Time Dimulai...")
    print("Tekan Ctrl+C untuk berhenti dan menyimpan sesi terakhir.")

    try:
        while True:
            new_window = gw.getActiveWindow()
            
            # Jika tidak ada jendela aktif atau judulnya kosong, lewati
            if new_window is None or new_window.title == "":
                time.sleep(POLL_INTERVAL)
                continue

            new_window_title = new_window.title

            # Jika jendela berganti
            if new_window_title != active_window_title:
                end_time = time.time()
                
                # Simpan durasi untuk jendela sebelumnya (jika ada)
                if active_window_title:
                    duration = end_time - start_time
                    # Tambahkan durasi ke total waktu aplikasi
                    data[active_window_title] = data.get(active_window_title, 0) + duration
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Sesi untuk '{active_window_title}' berakhir. Durasi: {duration:.2f} detik.")
                
                # Reset untuk jendela baru
                active_window_title = new_window_title
                start_time = time.time()
                save_data(data) # Simpan setiap kali ada perubahan
            
            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        # Menangani saat pengguna menekan Ctrl+C
        print("\n Merekam sesi terakhir sebelum keluar...")
        
        # Simpan durasi untuk jendela terakhir yang aktif
        if active_window_title:
            final_duration = time.time() - start_time
            data[active_window_title] = data.get(active_window_title, 0) + final_duration
        
        save_data(data)
        print("✅ Data berhasil disimpan. Sampai jumpa!")

if __name__ == "__main__":
    track_screen_time()
  
