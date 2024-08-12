# Better-and-Simpler-Voiceover
Projekt umożliwiający proste i wygodne generowanie lektora wysokiej jakości na podstawie napisów.

## O projekcie
Celem projektu jest stworzenie łatwego w użyciu narzędzia, które pozwoli na automatyczne generowanie lektorów wysokiej jakości. Umożliwi to twórcy treści na szybkie i efektywnie tłumaczyć filmy, videozapisy i inne materiały multimedialne.

## Technologie
Projekt jest oparty o język Python i wykorzystuje TTS (Text-to-Speech) technologie do generowania mowy. Użyte biblioteki i narzędzia:
* [**XTTS model**](https://huggingface.co/coqui/XTTS-v2): Wykorzystywany do generowania mowy z napisów.
* [**Gradio**](https://www.gradio.app/): Wykorzystywane jako interfejs użytkownika, umożliwiający łatwe sterowanie projektem.
## Jak działa
Aby skorzystać z funkcjonalności Better-and-Simpler-Voiceover, wystarczy:

1. Wprowadzić tekst (napisy) do generowania lektora.
2. Uzyskać wysokiej jakości plik audio z nagranym lektorem.

## Instalacja
Aby zainstalować projekt, należy:

1. Pobrać najnowszą wersję projektu z platformy GitHub.
2. Stwożyć venv komendą `python3.10 -m venv venv` i załadować go w terminalu `source ./venv/bin/activate.fish`.
3. Zainstaluj *PyTorch* odpowiedniego dla twojej karty graficznej ze strony [PyTorch](https://pytorch.org/get-started/locally/).
4. Zainstaluj pozostałe zależności `pip install -r requirements.txt`.
4. Uruchomić skrypt `setup.py` za pomocą polecenia `python setup.py`.

## Plany na przyszłość
- [ ] Proste dodawanie własnych głosów (Obecnie należy dodać próbki do folderu `voices/Aktor/`)
- [ ] Export do pliku mp4
- [ ] Użycie ffmpg do łączenia plików audio
- [ ] Dodanie RVC do poprawy audio

## Kontakt
Jeśli masz pytania lub chcesz przekazać swoje uwagi dotyczące projektu, możesz skontaktować się z nami za pomocą adresu e-mail: S3ba9989@proton.me.