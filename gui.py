import gradio as gr
from gradio.layouts.tabs import Tab
from pathlib import Path

from models.main import *

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
    with Tab(label="3. Połącz audio z wideo."):
        gr.Interface(
            fn=render_video,
            inputs=[gr.Video(label="Anime wideo"), gr.File(label="(Opsional) Subs:"), gr.Slider(label="Audio volium", maximum=2, value=0.75 )],
            outputs=gr.Video(),
            submit_btn="Render",
            allow_flagging="never",
        )


root.launch()
