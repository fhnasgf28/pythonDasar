import pyautogui
import time

import datetime

def switch_tab_every_3_minutes():
    print("Program dimulai. Pindah tab setiap 3 menit.")
    
    # Cek apakah sekarang jam 15:40
    now = datetime.datetime.now()
    target_time = now.replace(hour=15, minute=40, second=0, microsecond=0)
    
    # Jika sekarang jam 15:40, set waktu berhenti 1.2 jam dari sekarang
    if now.hour == 15 and now.minute == 40:
        stop_time = now + datetime.timedelta(hours=1.2)
        print(f"Ditemukan waktu 15:40. Program akan berhenti pada {stop_time.strftime('%H:%M')}")
    else:
        stop_time = None
        print("Bukan jam 15:40. Program akan berjalan tanpa batas waktu.")
    
    try:
        while True:
            # Cek apakah sudah waktunya berhenti (jika stop_time ada)
            if stop_time and datetime.datetime.now() >= stop_time:
                print("Waktu 1.2 jam telah berlalu. Program dihentikan.")
                break
                
            time.sleep(180)  # Tunggu 3 menit
            pyautogui.hotkey('command', 'option', 'right')  # Shortcut untuk berpindah tab kanan (Safari/Chrome)
            print(f"Berpindah ke tab berikutnya... {datetime.datetime.now().strftime('%H:%M:%S')}")
            
    except KeyboardInterrupt:
        print("Program dihentikan secara manual.")

if __name__ == "__main__":
    switch_tab_every_3_minutes()
