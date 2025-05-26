import pyautogui
import time
import random

# Jarak gerakan mouse ke kanan (dalam pixel)
offset = random.randint(1, 100)

try:
    while True:
        current_x, current_y = pyautogui.position()
        new_x = current_x + random.randint(1,1000)
        pyautogui.moveTo(new_x, current_y, duration=0.5)
        print(f"Mouse moved to: ({new_x}, {current_y})")
        time.sleep(70)  # tunggu 1 menit
except KeyboardInterrupt:
    print("Program dihentikan.")
