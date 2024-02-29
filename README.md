[FastAPI](https://fastapi.tiangolo.com/) Sample 動作確認のために作っています。

# ことはじめ

## 起動

まずは環境変数ファイルの用意
`.env.sample` を `.env` としてコピー

.envファイル編集。

```bash
# Site settings
DEBUG=true
APP_NAME="FastAPI Sample"
APP_VERSION="1.0.0"

# Database settings
DB_SCHEME=postgresql+asyncpg
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DB_PATH=sample
# DATABASE_DSN=
```

Docker起動。

```bash
docker-compose build --no-cache
docker-compose up -d
```

うまく起動したら早速アクセス。

```url
http://localhost:8000/
```

## マイグレーションの適用

```bash
docker-compose exec api alembic upgrade head
```

# 開発環境の整備

## Python仮想環境

作成

```bash
python -m venv .venv
```

起動

```
# for Windows
source .venv/Scripts/activate
# for Mac/Linux
source .venv/bin/activate
```

開発環境用のモジュールインストール

```
pip install -r app/requirements.dev.txt
```

## マイグレーションのリビジョン作成

```bash
docker-compose exec api alembic revision --autogenerate -m "brabra"
```
