import subprocess
import os

def convert_mp4_to_mp3(input_path, output_path=None):
    if output_path is None:
        base = os.path.splitext(input_path)[0]
        output_path = f"{base}.mp3"

    command = [
        "ffmpeg",
        "-i", input_path,
        "-vn",                 # no video
        "-acodec", "libmp3lame",
        "-ab", "192k",         # bitrate
        output_path,
        "-y"                   # overwrite
    ]

    subprocess.run(command, check=True)
    return output_path


# Example usage
convert_mp4_to_mp3("video.mp4")
