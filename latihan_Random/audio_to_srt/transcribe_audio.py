import os
import math
import ffmpeg
from faster_whisper import WhisperModel

def extract_audio(video_path, audio_output_path):
    """
    Ekstrak audio dari video ke format WAV (16kHz, mono) agar optimal untuk Whisper.
    """
    try:
        print(f"--- Mengekstrak audio dari {video_path} ---")
        (
            ffmpeg
            .input(video_path)
            .output(audio_output_path, ac=1, ar='16000') # 16kHz mono is best for AI
            .run(quiet=True, overwrite_output=True)
        )
        print("Audio berhasil diekstrak.")
        return True
    except ffmpeg.Error as e:
        print("Error FFmpeg:", e.stderr.decode('utf8'))
        return False

def format_timestamp(seconds):
    """
    Ubah detik (float) ke format SRT (HH:MM:SS,mmm)
    """
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def generate_srt(transcription_segments, output_srt_path, max_chars=40):
    """
    Membuat file SRT dengan logika 'Smart Splitting' agar teks tidak kepanjangan.
    """
    with open(output_srt_path, "w", encoding="utf-8") as f:
        idx = 1

        for segment in transcription_segments:
            # Kita menggunakan word_timestamps, jadi kita bisa akses detail per kata
            words = segment.words

            # Grouping kata-kata menjadi baris yang pas di layar
            current_line = []
            current_length = 0
            line_start = words[0].start

            for i, word in enumerate(words):
                # Tambahkan kata ke buffer
                current_line.append(word)
                current_length += len(word.word) + 1 # +1 untuk spasi

                # Cek apakah sudah mencapai batas max karakter atau ini kata terakhir
                is_last_word = (i == len(words) - 1)

                # LOGIKA PEMUTUSAN BARIS (Agar presisi visual)
                if current_length >= max_chars or is_last_word or word.word.endswith(('.', '?', '!')):

                    line_end = word.end
                    text_content = "".join([w.word for w in current_line]).strip()

                    # Tulis ke SRT
                    f.write(f"{idx}\n")
                    f.write(f"{format_timestamp(line_start)} --> {format_timestamp(line_end)}\n")
                    f.write(f"{text_content}\n\n")

                    # Reset untuk baris berikutnya
                    idx += 1
                    current_line = []
                    current_length = 0
                    if not is_last_word:
                        line_start = words[i+1].start # Mulai baris baru dari kata berikutnya

    print(f"Subtitle berhasil disimpan di: {output_srt_path}")

def main(video_file, model_size="medium"):
    audio_file = "temp_audio.wav"
    srt_file = os.path.splitext(video_file)[0] + ".srt"

    # 1. Ekstrak Audio
    if not extract_audio(video_file, audio_file):
        return

    # 2. Load Model Whisper
    # Gunakan "cuda" jika ada GPU NVIDIA, jika tidak "cpu"
    # compute_type="float16" (GPU) atau "int8" (CPU)
    device = "cuda" if os.environ.get('CUDA_VISIBLE_DEVICES') else "cpu"
    compute_type = "float16" if device == "cuda" else "int8"

    print(f"--- Memulai Transkripsi (Model: {model_size} on {device}) ---")

    try:
        model = WhisperModel(model_size, device=device, compute_type=compute_type)

        # 3. Transkripsi dengan VAD dan Word Timestamps (KUNCI PRESISI)
        # vad_filter=True -> Membuang bagian hening agar timestamp tidak ngaret
        segments, info = model.transcribe(
            audio_file,
            beam_size=5,
            word_timestamps=True,  # WAJIB TRUE agar kita bisa potong per kalimat pendek
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500)
        )

        # Konversi generator segments ke list (agar bisa diproses di fungsi generate_srt)
        # Note: Ini akan memakan waktu proses transkripsi
        segments_list = list(segments)

        # 4. Buat SRT
        generate_srt(segments_list, srt_file, max_chars=40)

    except Exception as e:
        print(f"Terjadi kesalahan transkripsi: {e}")

    finally:
        # Hapus file audio temporary
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    # Ganti nama file video Anda di sini
    input_video = "farhan.mp4"
    main(input_video, model_size="small")