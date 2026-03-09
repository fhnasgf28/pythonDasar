import pyautogui
import time
import random

# Jarak gerakan mouse maksimum (dalam pixel)
max_offset = 100

try:
    while True:
        current_x, current_y = pyautogui.position()
        offset_x = random.randint(-max_offset, max_offset)
        offset_y = random.randint(-max_offset, max_offset)
        new_x = current_x + offset_x
        new_y = current_y + offset_y
        pyautogui.moveTo(new_x, new_y, duration=0.5)
        print(f"Mouse moved to: ({new_x}, {new_y})")
        time.sleep(60)  # tunggu 1 menit
except KeyboardInterrupt:
    print("Program dihentikan.")