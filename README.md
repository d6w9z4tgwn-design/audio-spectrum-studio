# Audio Spectrum Studio

WAVファイルを高速フーリエ変換（FFT）で解析し、周波数成分を見やすいスペクトル画像として出力するツールです。音声のピーク周波数確認や、収録素材のノイズチェックに利用できます。

## 主な機能

- モノラル・ステレオWAVを自動的に扱えるFFT解析
- 相対dBスケールの高解像度PNGを生成
- 最大表示周波数を指定して、人の声など注目帯域を拡大

## セットアップ
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## 使い方

`python app.py input.wav spectrum.png --max-frequency 8000` を実行します。`--max-frequency` を省略すると、ナイキスト周波数まで表示します。出力先のフォルダがなければ自動作成します。

Python 3.10+ 推奨。
