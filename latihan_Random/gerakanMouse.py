import pyautogui
import time

# Jarak gerakan mouse ke kanan (dalam pixel)
offset = 100

try:
    while True:
        current_x, current_y = pyautogui.position()
        new_x = current_x + offset
        pyautogui.moveTo(new_x, current_y, duration=0.5)
        print(f"Mouse moved to: ({new_x}, {current_y})")
        time.sleep(60)  # tunggu 1 menit
except KeyboardInterrupt:
    print("Program dihentikan.")
