import time
from datetime import datetime
import os

def time_screen():
    """
    Menampilkan layar waktu dengan format yang menarik
    """
    try:
        while True:
            # Bersihkan layar
            os.system('clear' if os.name == 'posix' else 'cls')
            
            # Dapatkan waktu saat ini
            now = datetime.now()
            
            # Format waktu
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%A, %d %B %Y")
            
            # Tampilkan dengan format yang menarik
            print("\n" + "="*50)
            print(" " * 15 + "⏰ TIME SCREEN ⏰")
            print("="*50)
            print("\n")
            print(" " * 12 + "╔════════════════════╗")
            print(" " * 12 + "║                    ║")
            print(" " * 12 + f"║   {time_str}   ║")
            print(" " * 12 + "║                    ║")
            print(" " * 12 + "╚════════════════════╝")
            print("\n")
            print(" " * 8 + f"📅 {date_str}")
            print("\n" + "="*50 + "\n")
            
            # Update setiap 1 detik
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan. Terima kasih!")

if __name__ == "__main__":
    time_screen()
