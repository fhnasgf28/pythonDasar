import os
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Inisialisasi Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load model klasifikasi gambar (buat model sederhana atau gunakan model pretrained)
model = load_model('model.h5')  # Pastikan model Anda sudah dilatih dan disimpan

# Fungsi untuk memeriksa file yang diunggah
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Halaman utama untuk mengunggah gambar
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Cek apakah file diunggah
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Klasifikasi gambar
            result = classify_image(filepath)
            return render_template('upload.html', result=result, img_path=filepath)
    return render_template('upload.html')

# Fungsi untuk klasifikasi gambar
def classify_image(img_path):
    # Load gambar dan preprocess
    img = image.load_img(img_path, target_size=(224, 224))  # Sesuaikan ukuran dengan model
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediksi menggunakan model
    predictions = model.predict(img_array)
    class_names = ['Class A', 'Class B']  # Ganti dengan nama kelas Anda
    predicted_class = class_names[np.argmax(predictions)]
    return predicted_class

if __name__ == '__main__':
    # Pastikan folder uploads ada
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
