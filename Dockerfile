# Python 3.9 のイメージを使用
FROM python:3.10u

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt ./
COPY script.py ./

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

