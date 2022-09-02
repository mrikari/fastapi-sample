[FastAPI](https://fastapi.tiangolo.com/) Sample 動作確認のために作っています。

# ことはじめ

[uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) を参考にまずは起動。

```bash
docker-compose build --no-cache
docker-compose up -d
```

うまく起動したら早速アクセス: [http://localhost:8000/](http://localhost:8000/)

## 開発環境の整備

HotReloadを設定して、開発中はコードを変更した場合に自動的にサーバーが再起動するようにする。

```bash
docker-compose -f docker-compose.dev.yml  build
docker-compose -f docker-compose.dev.yml up
```

...うまく動かなかったのでPythonをインストールして動かす。

```bash
python -m venv .venv

# for Windows
source .venv/Scripts/activate

pip install -r requirements.dev.txt
uvicorn main:app --reload --app-dir ./app
```