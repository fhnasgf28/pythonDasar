import cv2
from fer import FER
import matplotlib.pyplot as plt


def detect_expression():
    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)

    # Inisialisasi deteksi ekspresi
    detector = FER(mtcnn=True)  # Menggunakan MTCNN untuk deteksi wajah yang lebih baik

    print("Tekan 'q' untuk keluar.")
    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()
        if not ret:
            print("Tidak dapat membaca frame dari kamera.")
            break

        # Konversi frame ke RGB (FER membutuhkan RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Deteksi ekspresi
        results = detector.detect_emotions(rgb_frame)

        # Tampilkan deteksi wajah dan label ekspresi
        for result in results:
            (x, y, w, h) = result['box']
            emotion, score = detector.top_emotion(rgb_frame)

            # Gambar kotak di sekitar wajah
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Tampilkan label ekspresi di atas kotak
            label = f"{emotion} ({score:.2f})"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Tampilkan frame dengan deteksi ekspresi
        cv2.imshow("Deteksi Wajah dan Ekspresi", frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Tutup kamera dan jendela
    cap.release()
    cv2.destroyAllWindows()


# Jalankan fungsi
detect_expression()
