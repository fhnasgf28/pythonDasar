import cv2
import mediapipe as mp
import pyautogui

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Konfigurasi untuk deteksi tangan
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Buka kamera
cap = cv2.VideoCapture(0)

# Variabel untuk posisi Y sebelumnya
prev_y = None

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip gambar untuk efek seperti cermin
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Proses frame untuk deteksi tangan
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Gambarkan landmark tangan
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Ambil koordinat landmark tengah tangan (Landmark 9 = "Middle MCP")
                y_position = hand_landmarks.landmark[9].y  # Posisi Y normalisasi (0.0 - 1.0)

                # Deteksi gerakan tangan naik atau turun
                if prev_y is not None:
                    if y_position < prev_y - 0.02:  # Gerakan naik
                        pyautogui.scroll(10)  # Scroll ke atas
                    elif y_position > prev_y + 0.02:  # Gerakan turun
                        pyautogui.scroll(-10)  # Scroll ke bawah

                # Perbarui posisi Y sebelumnya
                prev_y = y_position

        # Tampilkan frame dengan deteksi tangan
        cv2.imshow("Hand Gesture Scroll", frame)

        # Keluar dengan menekan 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
