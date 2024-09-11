from __future__ import print_function, unicode_literals
from models import main
import argparse
from pprint import pprint
import shutil
import os


import inquirer

voice_questions = [
    inquirer.List(
        "voice",
        message="Jaki głos wybierasz?",
        choices=main.load_voices()
    )
]


parser = argparse.ArgumentParser()
parser.add_argument("subs", type=str, help="Plik na podstawie którego generujesz głos.")
parser.add_argument("video", type=str, help="Plik aniem zgodny z napisami.")
parser.add_argument("--voice", type=str, help="Plik aniem zgodny z napisami.")
parser.add_argument("-s", "--bonus_subs", type=str, help="Plik który zostanie naiesiony na obraz.")
parser.add_argument("-o", "--output_file", type=str, help="Jak zapisać wynikowy plik wideo.")
parser.add_argument("-v", "--volume", type=float, help="Głośność generowanego głosu.")
args = parser.parse_args()

subs = os.path.expanduser(args.subs)
video = os.path.expanduser(args.video)
voice = args.voice if args.voice else inquirer.prompt(voice_questions)["voice"] # type: ignore[attr-defined]
bonus_subs = os.path.expanduser(args.bonus_subs) if args.bonus_subs else None
output_file =  os.path.expanduser(args.output_file) if args.output_file else None
volume = float(args.volume) if args.volume else None

print(subs)
print(video)
print(voice)
print(bonus_subs)
print(output_file)

print(main.load_subs_fn(subs))
main.render_TTS(voice)
main.render_video(video, subs=bonus_subs, volume=volume)
if output_file: shutil.copy('video_out/main.mp4', output_file)
