import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)

while True:
    ret, frame2 = cap.read()
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.GaussianBlur(frame2, (21, 21), 0)

    # hitung perbedaan antara frame saat ini dan frame sebelumnya
    diff = cv2.absdiff(frame1, frame2)

    # ambil threshold untuk mendeteksi perubahan
    thresh = cv2.threshold(diff, 30,255, cv2.THRESH_BINARY)[1]

    # lakukan dilasi untuk memperbesar area puth (gerakan)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # temukan kontur padagambar yang telah didilasi
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # GAMBAR KOTAK di sekitar objek yang bergerak
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # tampilkan hasil
    cv2.imshow("Frame", frame1)
    frame1 = frame2

    # tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()