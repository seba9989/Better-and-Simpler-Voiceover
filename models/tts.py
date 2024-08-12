from glob import glob

import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"


def tts_render(subs: list[dict[str, str]], voice: str):
    print(device)
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

    for sub in subs:
        text = sub["text"]

        start_time = sub["start"]

        out_path = f"tts_out/fragments/{start_time}.wav"
        
        print(out_path)

        tts.tts_to_file(
            text=text,
            speed=0.5,
            emotion="neutral",
            speaker_wav=glob(f"./voices/{voice}/*.mp3"), # type: ignore
            file_path=out_path,
            language="pl",
        )
