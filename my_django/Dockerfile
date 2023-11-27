# 使用するPythonのイメージを指定
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションのコードをコピー
COPY . /app/

# ポートを公開
EXPOSE 8000

# Djangoサーバーを起動
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
