import cv2
import time
import os

# Load model deteksi wajah dan mata
xml_folder_path = os.path.join(os.getcwd(), 'xml_opencv')
face_cascade = cv2.CascadeClassifier(os.path.join(xml_folder_path, 'haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(xml_folder_path, 'haarcascade_eye.xml'))

# Check if the cascades are loaded successfully
if face_cascade.empty():
    print("Error loading haarcascade_frontalface_default.xml")
if eye_cascade.empty():
    print("Error loading haarcascade_eye.xml")

# Inisialisasi webcam
cap = cv2.VideoCapture(0)
blink_count = 0
last_blink_time = time.time()
message_to_display = None  # Variabel untuk menyimpan pesan


def detect_blink(gray, frame):
    global last_blink_time, blink_count
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # Deteksi mata
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
        if len(eyes) < 2:  # Jika mata kurang dari 2 (berkedip)
            if time.time() - last_blink_time > 0.2:  # Kedipan harus terjadi minimal 0.2 detik
                blink_count += 1
                last_blink_time = time.time()
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)


def translate_blink(blink_count):
    if blink_count <= 3:
        return "Minta tolong"
    elif blink_count == 4:
        return "Ingin Pipis"
    return None


while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_blink(gray, frame)

    # Tampilkan pesan jika jumlah kedipan sesuai dengan kode
    message = translate_blink(blink_count)
    if message:
        message_to_display = message
        blink_count = 0

    # Jika ada pesan, tampilkan di layar
    if message_to_display:
        cv2.putText(
            frame,  # Frame tempat teks ditampilkan
            message_to_display,  # Pesan yang ditampilkan
            (50, 50),  # Koordinat (x, y) teks
            cv2.FONT_HERSHEY_SIMPLEX,  # Jenis font
            1,  # Ukuran font
            (0, 0, 255),  # Warna (BGR)
            2,  # Ketebalan garis teks
            cv2.LINE_AA  # Jenis garis
        )

    # Tampilkan frame
    cv2.imshow("Farhan", frame)

    # Tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
