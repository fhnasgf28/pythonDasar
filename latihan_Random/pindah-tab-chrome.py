import pyautogui
import time
import sys

# === KONFIGURASI ===
INTERVAL_PINDANG_TAB_MENIT = 4
# Ubah sesuai sistem operasi Anda
# Untuk Windows/Linux: ['ctrl', 'tab']
# Untuk macOS: ['command', 'tab']
TOMBOL_PINTAS_PINDAH_TAB = ['ctrl', 'tab']
# ===================

print(f"Script akan mulai memindahkan tab Chrome setiap {INTERVAL_PINDANG_TAB_MENIT} menit.")
print("Pindahkan mouse ke pojok kiri atas (0,0) untuk menghentikan script secara paksa.")

try:
    while True:
        # Pindahkan tab menggunakan kombinasi tombol pintas
        pyautogui.hotkey(*TOMBOL_PINTAS_PINDAH_TAB)
        print(f"Tab Chrome berh asil dipindahkan pada {time.ctime()}")
    
        # Tunggu selama interval yang ditentukan (dalam detik)
        time.sleep(INTERVAL_PINDANG_TAB_MENIT * 60)

except pyautogui.FailSafeException:
    print("\nScript dihentikan   secara paksa oleh pengguna (fail-safe diaktifkan).")
except KeyboardInterrupt:
    print("\nScript dihentikan oleh pengguna (Ctrl+C).")
except Exception as e:
    print(f"\nTerjadi error: {e}")
    sys.exit(1)

print("Script selesai.")