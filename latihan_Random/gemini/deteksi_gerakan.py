import cv2
import time
import os
import numpy as np

# load model deteksi wajah dan mata
xml_folder_path = os.path.join(os.getcwd(), 'xml_opencv')
face_cascade = cv2.CascadeClassifier(os.path.join(xml_folder_path, 'haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(xml_folder_path, 'haarcascade_eye.xml'))
# Check if the cascades are loaded successfully
if face_cascade.empty():
    print("Error loading haarcascade_frontalface_default.xml")
if eye_cascade.empty():
    print("Error loading haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)
# variable untuk mencatat waktu kedipan
last_blink_time = time.time()
blink_count = 0
pupil_center = 0


# fungsi untuk mendeteksi kedipan
def detect_blink(gray, frame):
    global last_blink_time, blink_count, pupil_center
    # deteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Deteksi mata
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # ROI mata untuk pelacakan pupil
            roi_gray_eye = roi_gray[ey:ey + eh, ex:ex + ew]
            roi_color_eye = roi_color[ey:ey + eh, ex:ex + ew]
            # Assuming 'pupil_ratio' is defined somewhere or here
            pupil_ratio = 0.0  # Placeholder value; you need to calculate it based on your context
            if pupil_ratio < 0.3:
                if time.time() - last_blink_time >= 0.2:
                    blink_count += 1
                    last_blink_time = time.time()
    if eye_cascade:
        if time.time() - last_blink_time >= 0.2:
            blink_count += 1
            last_blink_time = time.time()


def transalate_blink(blink_count):
    if blink_count == 3:
        return "Minta tolong"
    elif blink_count == 4:
        return "Ingin Pipis"


while True:
    ret, frame2 = cap.read()
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.GaussianBlur(gray, (21, 21), 0)
    detect_blink(gray, frame2)

    # tampilkan pesan jika jumlah kedipan sudah sesuai dengan kode
    if blink_count >= 5:
        message = transalate_blink(blink_count)
        print(message)
        blink_count = 0
    # hitung perbedaan antara frame saat ini dan frame sebelumnya
    diff = cv2.absdiff(frame1, gray)
    # ambil threshold untuk mendeteksi perubahan
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    # lakukan dilasi untuk memperbesar area putih (gerakan)
    dilated = cv2.dilate(thresh, None, iterations=3)
    # temukan kontur pada gambar yang telah didilasi
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # GAMBAR KOTAK di sekitar objek yang bergerak
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # tampilkan hasil
    cv2.imshow("Frame", frame1)
    frame1 = gray

    # tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()