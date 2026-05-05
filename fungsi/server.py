#!/usr/bin/env python3
"""
Home Security Webcam Server
Logitech C270 - Flask Streaming Backend (Original High Quality)
"""

import cv2
import os
import subprocess
import time
import threading
from flask import Flask, Response, jsonify, send_from_directory, stream_with_context
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)

# ── Global State ──────────────────────────────────────────────
camera = None
camera_active = False
frame_lock = threading.Lock()
current_frame = None
camera_index = 2            # Default set to Index 2 (Extra)
audio_input = os.getenv('HOMESEC_AUDIO_INPUT', 'alsa')
audio_device = os.getenv('HOMESEC_AUDIO_DEVICE', 'plughw:CARD=WEBCAM,DEV=0')
audio_bitrate = os.getenv('HOMESEC_AUDIO_BITRATE', '128k')
audio_sample_rate = int(os.getenv('HOMESEC_AUDIO_SAMPLE_RATE', '44100'))
last_audio_error = None

# ── Camera Thread ─────────────────────────────────────────────
def capture_frames():
    global camera, current_frame, camera_active

    while camera_active:
        ret, frame = camera.read()
        if not ret:
            time.sleep(0.01)
            continue

        # ── Overlay: timestamp ─────────────────────────────────
        ts = time.strftime("%Y-%m-%d  %H:%M:%S")
        cv2.putText(frame, ts, (10, frame.shape[0] - 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

        with frame_lock:
            # Menggunakan kualitas JPEG 95% untuk hasil jernih tanpa filter
            ret2, jpeg = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
            if ret2:
                current_frame = jpeg.tobytes()

        time.sleep(0.01)


def generate_stream():
    while camera_active:
        with frame_lock:
            frame = current_frame
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.01)


def build_audio_command():
    input_format = (audio_input or 'pulse').strip().lower()
    device_name = (audio_device or 'default').strip() or 'default'

    return [
        'ffmpeg',
        '-nostdin',
        '-loglevel', 'error',
        '-f', input_format,
        '-i', device_name,
        '-ac', '1',
        '-ar', str(audio_sample_rate),
        '-vn',
        '-c:a', 'libmp3lame',
        '-b:a', audio_bitrate,
        '-f', 'mp3',
        'pipe:1'
    ]


def generate_audio_stream():
    global last_audio_error
    process = None
    try:
        last_audio_error = None
        process = subprocess.Popen(
            build_audio_command(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0
        )

        while camera_active:
            chunk = process.stdout.read(4096)
            if not chunk:
                if process.poll() is not None and process.stderr:
                    last_audio_error = process.stderr.read().decode('utf-8', errors='ignore').strip() or 'Audio stream stopped unexpectedly.'
                break
            yield chunk
    finally:
        if process:
            process.terminate()
            try:
                process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                process.kill()


def probe_audio_input():
    command = [
        'ffmpeg',
        '-nostdin',
        '-loglevel', 'error',
        '-f', (audio_input or 'alsa').strip().lower(),
        '-i', (audio_device or 'default').strip() or 'default',
        '-t', '1',
        '-ac', '1',
        '-ar', str(audio_sample_rate),
        '-vn',
        '-f', 'null',
        '-'
    ]
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=4
    )
    return {
        'ok': result.returncode == 0,
        'command': command,
        'stderr': result.stderr.strip()
    }


# ── Routes ────────────────────────────────────────────────────
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/start', methods=['POST'])
def start_camera():
    global camera, camera_active, camera_index, audio_input, audio_device
    if camera_active:
        return jsonify({
            'status': 'already_running',
            'index': camera_index,
            'audio_input': audio_input,
            'audio_device': audio_device
        })

    from flask import request
    data = request.get_json(silent=True) or {}
    req_index = data.get('index', camera_index)
    req_audio_input = data.get('audio_input', audio_input)
    req_audio_device = data.get('audio_device', audio_device)

    # Inisialisasi kamera
    cam = cv2.VideoCapture(req_index)
    
    # Gunakan MJPG untuk performa 720p maksimal
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cam.set(cv2.CAP_PROP_FPS, 30)
    
    # MENGHAPUS MANUAL BRIGHTNESS/CONTRAST 
    # Membiarkan Auto-Exposure & Auto-White Balance bekerja (Agar tidak gelap)
    cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cam.isOpened():
        return jsonify({'status': 'error', 'message': f'Cannot open camera index {req_index}.'}), 500

    camera_index = req_index
    audio_input = req_audio_input
    audio_device = req_audio_device
    camera = cam
    camera_active = True

    t = threading.Thread(target=capture_frames, daemon=True)
    t.start()

    return jsonify({
        'status': 'started',
        'index': camera_index,
        'audio_input': audio_input,
        'audio_device': audio_device
    })


@app.route('/api/stop', methods=['POST'])
def stop_camera():
    global camera, camera_active, current_frame
    camera_active = False
    time.sleep(0.2)
    if camera:
        camera.release()
        camera = None
    current_frame = None
    return jsonify({'status': 'stopped'})


@app.route('/api/stream')
def stream():
    if not camera_active:
        return jsonify({'error': 'Camera not active'}), 503
    return Response(generate_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/api/audio')
def audio_stream():
    if not camera_active:
        return jsonify({'error': 'Camera not active'}), 503
    return Response(
        stream_with_context(generate_audio_stream()),
        mimetype='audio/mpeg',
        headers={
            'Cache-Control': 'no-store',
            'X-Content-Type-Options': 'nosniff'
        }
    )


@app.route('/api/audio_probe')
def audio_probe():
    if not camera_active:
        return jsonify({'error': 'Camera not active'}), 503

    result = probe_audio_input()
    payload = {
        'ok': result['ok'],
        'audio_input': audio_input,
        'audio_device': audio_device,
        'last_audio_error': last_audio_error,
        'stderr': result['stderr']
    }
    return jsonify(payload), (200 if result['ok'] else 500)


@app.route('/api/status')
def status():
    return jsonify({
        'active': camera_active,
        'audio_input': audio_input,
        'audio_device': audio_device,
        'last_audio_error': last_audio_error,
        'time': time.time()
    })


if __name__ == '__main__':
    print("\n" + "="*50)
    print("  🏠  Home Security Server — High Quality Mode")
    print("="*50)
    print(f"  Open: http://localhost:5000")
    print(f"  Default Camera index: {camera_index}")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
