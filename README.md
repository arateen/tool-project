# ミニ便利ツール & ゲーム集

## 概要
コマンドライン上で動作する便利な計算機能やミニゲーム（じゃんけん等）をまとめた対話型ツールです。

## 利用したオープンソースソフトウェア（OSS）
- rich: ターミナル画面の文字装飾、パネル枠線の描画に使用（https://github.com/Textualize/rich）

## 動作環境と事前準備
- Python 3.x
- 必要ライブラリのインストール：
  pip install rich

## 使い方
コマンドプロンプトで以下を実行します：
python tool.py

## Git/GitHub運用の工夫点
- 機能ごとにブランチ（feature-janken, feature-rich-ui等）を切り替えて開発しました。
- ペア間でプルリクエストとコードレビューを実施してから master にマージしました。