import re
from glob import glob

import gradio as gr
from gradio.layouts.tabs import Tab
from gradio.server_messages import List
from pathlib import Path

from models import combine, subs_parser, tts

subs: List[dict[str, str]] | None = None


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
    return subs


def render_TTS(voice: str):
    global subs
    if subs == None:
        return gr.Error("Krok po kroku. (Wróć do kroku pierwszego.)")
    tts.tts_render(subs, voice)
    
    combine.merge_audio_files(glob("./tts_out/fragments/*"), "./tts_out/merged/full.mp3")
    return Path("./tts_out/merged/full.mp3")


with gr.Blocks() as root:
    with Tab(label="1. Załaduj napisy."):
        gr.Interface(
            fn=load_subs_fn,
            inputs=gr.File(label="Plik z napisami"),
            outputs=gr.TextArea(label="Załadowane Napisy"),
            submit_btn="Przeanalizuj napisy",
            allow_flagging="never",
        )
    with Tab(label="2. Przygotuj wstępnie audio."):
        gr.Interface(
            fn=render_TTS,
            inputs=gr.Radio(load_voices(), label="Wybierz głos:"),
            outputs=gr.Audio(),
            submit_btn="Render",
            allow_flagging="never",
        )


root.launch()
