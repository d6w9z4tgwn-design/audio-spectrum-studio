# audio-spectrum-studio

WAV音声のFFTとスペクトル画像を生成。

Analyze WAV audio with FFT.

## Setup / 起動
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## Usage / 使用例
`python app.py input.wav spectrum.png --max-frequency 8000` — generates a high-resolution chart with a readable dB scale.

Python 3.10+ recommended. AI-generated development assistance was used.
