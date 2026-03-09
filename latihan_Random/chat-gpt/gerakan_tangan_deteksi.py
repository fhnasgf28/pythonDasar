import cv2
import numpy as np

# Tetapkan jangkauan warna (contoh: warna biru untuk jari telunjuk)
lower_bound = np.array([100, 150, 0])  # Rentang bawah HSV untuk biru
upper_bound = np.array([140, 255, 255])  # Rentang atas HSV untuk biru

# Variabel untuk menyimpan posisi
points = []
predicted_letter = ""


# Fungsi sederhana untuk mengenali huruf
def recognize_letter(points):
    if len(points) < 10:
        return ""
    # Contoh sederhana untuk mengenali huruf "L"
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    if max(x_coords) - min(x_coords) > 100 and max(y_coords) - min(y_coords) < 50:
        return "L"
    return "?"


# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Balik frame untuk membuat lebih intuitif
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Deteksi warna
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Ambil kontur terbesar
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 500:
            # Dapatkan koordinat pusat
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))
            points.append(center)

            # Gambar titik pada frame
            cv2.circle(frame, center, 5, (255, 0, 0), -1)

    # Jika terlalu banyak titik, reset
    if len(points) > 100:
        points = []

    # Prediksi huruf
    predicted_letter = recognize_letter(points)

    # Tampilkan prediksi
    cv2.putText(frame, f"Predicted Letter: {predicted_letter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow("Handwriting Recognition", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan resource
cap.release()
cv2.destroyAllWindows()
