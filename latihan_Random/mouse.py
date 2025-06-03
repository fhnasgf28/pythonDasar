import pyautogui
import time
import random

<<<<<<< HEAD
# Jarak gerakan mouse maksimum (dalam pixel)
max_offset = 100
=======
# Jarak gerakan mouse ke kanan (dalam pixel)
offset = random.randint(1, 100)
>>>>>>> 30cf9c3e754530092c33ed5ad0e6b36bc65d6b44

try:
    while True:
        current_x, current_y = pyautogui.position()
<<<<<<< HEAD
        offset_x = random.randint(-max_offset, max_offset)
        offset_y = random.randint(-max_offset, max_offset)
        new_x = current_x + offset_x
        new_y = current_y + offset_y
        pyautogui.moveTo(new_x, new_y, duration=0.5)
        print(f"Mouse moved to: ({new_x}, {new_y})")
        time.sleep(60)  # tunggu 1 menit
=======
        new_x = current_x + random.randint(1,1000)
        pyautogui.moveTo(new_x, current_y, duration=0.5)
        print(f"Mouse moved to: ({new_x}, {current_y})")
        time.sleep(70)  # tunggu 1 menit
>>>>>>> 30cf9c3e754530092c33ed5ad0e6b36bc65d6b44
except KeyboardInterrupt:
    print("Program dihentikan.")