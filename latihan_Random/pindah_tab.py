import pyautogui
import time

def switch_tab_every_3_minutes():
    print("Program dimulai. Pindah tab setiap 3 menit.")
    try:
        while True:
            time.sleep(180)  # Tunggu 3 menit
            pyautogui.hotkey('command', 'option', 'right')  # Shortcut untuk berpindah tab kanan (Safari/Chrome)
            print("Berpindah ke tab berikutnya...")
    except KeyboardInterrupt:
        print("Program dihentikan secara manual.")

if __name__ == "__main__":
    switch_tab_every_3_minutes()
