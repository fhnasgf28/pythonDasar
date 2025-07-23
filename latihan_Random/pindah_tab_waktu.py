import pyautogui
import time
import datetime

def switch_tab_every_5_minutes():
    print("Program dimulai. Pindah tab setiap 5 menit.")
    # cek apakah sekarang jam 16.00
    now = datetime.datetime.now()
    target_time = now.replace(hour=16, minute=0, second=0, microsecond=0)

    # jik sekarang jam 16.00, set waktu berhenti 1.2 jam dari sekarang
    if now.hour == 16 and now.minute == 0:
        stop_time = now + datetime.timedelta(hours=1.2)
        print(f"Ditemukan waktu 16.00. Program akan berhenti pada {stop_time.strftime('%H:%M')}")
    else:
        stop_time = None
        print("Ditemukan waktu bukan jam 16.00. Program akan berjalan tanpa batas waktu.")

    try:
        while True:
            # cek apakah sudah waktunya berhenti (jika stop_time ada)
            if stop_time and datetime.datetime.now() >= stop_time:
                print("Waktu 1.2 jam telah berlalu. Program dihentikan.")
                break

            time.sleep(300)  # tunggu 5 menit
            pyautogui.hotkey('command', 'option', 'right')  # shortcut untuk berpindah tab kanan (Safari/Chrome)
            print(f"Berpindah ke tab berikutnya... {datetime.datetime.now().strftime('%H:%M:%S')}")

    except KeyboardInterrupt:
        print("Program dihentikan secara manual.")

if __name__ == "__main__":
    switch_tab_every_5_minutes()