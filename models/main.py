import re
from glob import glob

from pathlib import Path

from models import combine, subs_parser, tts

import os

subs: list[dict[str, str]] | None = None

import gradio as gr

def load_voices():
    voice_re = re.compile(r"./voices/(.*)")
    voices = []
    for voice in glob("./voices/*"):
        voice = voice_re.search(voice)
        if voice:
            voice = voice.group(1)
        else:
            return []
        voices.append(voice)
    return voices


def load_subs_fn(file_path: str):
    global subs
    subs = subs_parser.path_to_subs_list(file_path)
    subs_str = ""

    for x in subs:
        subs_str += f"""
            Time: {x['start']},    Character: {x['name']}:
            >    Text: {x['text']}
        """

    return subs_str


def render_TTS(voice: str):
    for x in glob("./tts_out/fragments/*"):
        os.remove(x)

    global subs
    if subs == None:
        return gr.Error("Krok po kroku. (Wróć do kroku pierwszego.)")
    tts.tts_render(subs, voice)

    combine.merge_audio_files(glob("./tts_out/fragments/*"), "./tts_out/merged/full.mp3")
    return Path("./tts_out/merged/full.mp3")

def render_video(video: str, subs: str | None, volume: float | None):
    print(subs)
    combine.merge_video(video, subs, volume)
    return Path("video_out/main.mp4")
