import cv2
import mediapipe as mp
import numpy as np
from pynput.mouse import Button, Controller

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Inisialisasi Mouse Controller dari pynput
mouse = Controller()

# Inisialisasi Webcam
cap = cv2.VideoCapture(0)


# Fungsi untuk mendeteksi posisi ujung jari telunjuk dan jari tengah
def get_finger_tip_positions(image, hand_landmarks):
    image_height, image_width, _ = image.shape
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    x_index = int(index_finger_tip.x * image_width)
    y_index = int(index_finger_tip.y * image_height)
    x_middle = int(middle_finger_tip.x * image_width)
    y_middle = int(middle_finger_tip.y * image_height)
    return (x_index, y_index), (x_middle, y_middle)


# Fungsi untuk menentukan apakah 1 jari atau 2 jari yang terangkat
def count_fingers_up(hand_landmarks):
    fingertips_index = [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]

    fingertips_mcp = [
        mp_hands.HandLandmark.THUMB_IP,
        mp_hands.HandLandmark.INDEX_FINGER_MCP,
        mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
        mp_hands.HandLandmark.RING_FINGER_MCP,
        mp_hands.HandLandmark.PINKY_MCP
    ]

    fingers_up = 0
    for i in range(1, 5):
        tip = hand_landmarks.landmark[fingertips_index[i]]
        mcp = hand_landmarks.landmark[fingertips_mcp[i]]
        if tip.y < mcp.y:
            fingers_up += 1

    return fingers_up


# Ambang batas untuk gerakan scroll (sesuaikan dengan kenyamanan)
scroll_threshold = 50

# Untuk smoothing pergerakan scroll
previous_y_index = 0

# Variabel untuk teks notifikasi
scroll_text = ""
text_color = (0, 255, 0)  # Warna hijau

while True:
    # Baca frame dari webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame secara horizontal agar lebih natural
    frame = cv2.flip(frame, 1)

    # Konversi gambar ke RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Proses gambar dengan MediaPipe Hands
    results = hands.process(rgb_frame)

    # Jika terdeteksi tangan
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar landmark tangan
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Dapatkan posisi ujung jari telunjuk dan jari tengah
            (x_index, y_index), (x_middle, y_middle) = get_finger_tip_positions(frame, hand_landmarks)

            # Gambar lingkaran di ujung jari telunjuk dan jari tengah
            cv2.circle(frame, (x_index, y_index), 10, (0, 255, 0), -1)  # Telunjuk: Hijau
            cv2.circle(frame, (x_middle, y_middle), 10, (0, 0, 255), -1)  # Tengah: Biru

            # Hitung jumlah jari yang terangkat (selain jempol)
            num_fingers_up = count_fingers_up(hand_landmarks)

            # Kontrol scroll berdasarkan jumlah jari dan perubahan posisi y
            if previous_y_index != 0:
                # Scroll up dengan 1 jari (telunjuk)
                if num_fingers_up == 1:
                    delta_y = y_index - previous_y_index
                    if delta_y < -scroll_threshold:
                        mouse.scroll(0, 1)  # Scroll up
                        scroll_text = "Scrolling Up (1 Finger)"
                        text_color = (0, 255, 255)  # Warna kuning
                        print("Scrolling Up (1 Finger)")

                # Scroll down dengan 2 jari (telunjuk dan tengah)
                elif num_fingers_up == 2:
                    delta_y = y_index - previous_y_index
                    if delta_y > scroll_threshold:
                        mouse.scroll(0, -1)  # Scroll down
                        scroll_text = "Scrolling Down (2 Fingers)"
                        text_color = (0, 0, 255)  # Warna biru
                        print("Scrolling Down (2 Fingers)")

                else:
                    scroll_text = ""

            # Update previous_y_index untuk frame berikutnya
            previous_y_index = y_index

    # Tampilkan teks notifikasi di layar
    cv2.putText(frame, scroll_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    # Tampilkan frame
    cv2.imshow('Hand Tracking and Scroll Control', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()