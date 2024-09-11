from pydub import AudioSegment
from models.time_conversion import time_code_to_milliseconds
import ffmpeg



def ensure_stereo(audio):
    # Jeśli plik jest mono, konwertujemy go na stereo, kopiując lewy kanał do prawego
    if audio.channels == 1:
        audio = audio.set_channels(2)
        left_channel = audio.split_to_mono()[0]
        stereo_audio = AudioSegment.from_mono_audiosegments(left_channel, left_channel)
        return stereo_audio
    return audio


def merge_audio_files(audio_files, output_file):
    # Stwórz pusty plik audio o odpowiedniej długości
    combined = AudioSegment.silent(duration=0)
    current_end_time = 0

    for file in audio_files:
        # Załaduj plik audio
        audio = AudioSegment.from_file(file)
        # Upewnij się, że audio jest stereo
        audio = ensure_stereo(audio)
        # Oblicz czas rozpoczęcia w milisekundach
        requested_start_time = time_code_to_milliseconds(file)

        # Ustal rzeczywisty czas rozpoczęcia (max z czasów początkowych lub końca poprzedniego fragmentu)
        actual_start_time = max(requested_start_time, current_end_time)

        # Debugowanie: Wypisz szczegóły
        print(f"Processing file: {file}")
        print(f"Requested start time: {requested_start_time} ms")
        print(f"Actual start time: {actual_start_time} ms")
        print(f"Audio duration: {len(audio)} ms")

        # Ustaw nową długość pliku wynikowego
        if len(combined) < actual_start_time + len(audio):
            combined = combined + AudioSegment.silent(duration=(actual_start_time + len(audio) - len(combined)))

        # Dodaj audio do odpowiedniego miejsca w pliku wynikowym
        combined = combined.overlay(audio, position=actual_start_time)

        # Zaktualizuj czas zakończenia aktualnego fragmentu
        current_end_time = actual_start_time + len(audio)

    # Zapisz wynikowy plik audio
    combined.export(output_file, format="mp3")

def merge_video(video_path: str, subs_path: str | None, volume: float | None = 0.6):
    # if not volume: volume = 0.6
    video_out = "video_out/main.mp4"
    video_temp = "video_out/temp.mp4"

    # Najpierw wczytujemy oba strumienie
    video = ffmpeg.input(video_path)
    audio = ffmpeg.input("tts_out/merged/full.mp3")

    # Tworzymy filtr do zmiany głośności audio
    audio_with_volume = audio.filter('volume', volume)

    # Zmiksowanie ścieżek audio przy użyciu amix
    mixed_audio = ffmpeg.filter([video.audio, audio_with_volume], 'amix', inputs=2, duration='longest')

    if subs_path:
        video_with_subtitles = video.filter('ass', subs_path)

        (
            ffmpeg
            .output(video_with_subtitles, mixed_audio, video_out,vcodec="h264_amf" , acodec='aac')
            .overwrite_output()
            .run()
        )

    else:
        (
            ffmpeg
            .output(video.video, mixed_audio, video_out, vcodec='copy', acodec='aac')
            .overwrite_output()
            .run()
        )
