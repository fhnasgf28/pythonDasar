import cv2
import face_recognition
import smtplib
from face_recognition import face_locations

def send_email_alert():
    # kirim email alert
    print("kirim email alert")
    sender_email = "assegaffarhan4@gmail.com"
    receiver_email = "assegaffarhan5@gmail.com"
    password = "ALKHAMDULILLAH234"

    message = """
    Subject: Face Recognition Alert

    Warning: An unknown person was detected in the video feed.
    """
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# buka kamera
video_capture = cv2.VideoCapture(0)
known_image= face_recognition.load_image_file(
    "farhan1.jpg")
known_face_encodings = face_recognition.face_encodings(known_image)[0]

# menyimpan lokasi wajah
known_face_encodings = [known_face_encodings]
known_face_name= ["farhan"]

while True:
    # membaca frame
    ret, frame = video_capture.read()
    if not ret:
        print("tidak dapat membaca frame")
        break

    #ubah frame ke RGB
    rgba_frame = frame[:, :, ::-1]

    # deteksi lokasi wajah
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # cek apakah wajah terdeteksi
        mathces = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in mathces:
            first_match_index = mathces.index(True)
            name = known_face_name[first_match_index]
        if name == "Unknown":
            send_email_alert()
        # tampilkan wajah terdeteksi
        num_face = len(face_locations)

        # tampilkan wajah terdeteksi
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f"{num_face} wajah terdeteksi", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # tampilkan frame
    cv2.imshow('Video', frame)

    # keluar jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()