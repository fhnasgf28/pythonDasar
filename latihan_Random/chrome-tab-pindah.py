import pyautogui
import time

def switch_chrome_tab(interval_minutes=4):
    """ 
    Berpindah tab di Google Chrome setiap interval waktu tertentu.

    Args:
        interval_minutes (int): Interval waktu dalam menit untuk berpindah tab.
    """
    print(f"Memulai otomatisasi perpindahan tab Chrome setiap {interval_minutes} menit.")
    print("Pastikan Google Chrome adalah aplikasi yang aktif saat menjalankan skrip ini.")
    print("Tekan     Ctr    l+C di terminal untuk menghentikan skrip.")

    try:
        while True:
            # Tekan Ctrl + Tab untuk berpindah ke tab berikutnya
            # Gunakan ['command', 'tab'] untuk macOS
            pyautogui.hotkey('ctrl', 'tab')
            print(f"Tab telah berpindah. Menunggu {interval_minutes} menit...")
            time.sleep(interval_minutes * 60) # Konversi menit ke detik
    except KeyboardInterrupt:
        print("\nSkrip dihentikan oleh pengguna.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Panggil fungsi untuk memulai otomatisasi
if __name__ == "__main__":
    # Anda bisa mengubah angka 4 di bawah untuk interval waktu yang berbeda
    switch_chrome_tab(interval_minutes=4)