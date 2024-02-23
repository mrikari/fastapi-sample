[FastAPI](https://fastapi.tiangolo.com/) Sample 動作確認のために作っています。

# ことはじめ

##　起動

まずは環境変数ファイルの用意
`.env.sample` を `.env` としてコピー

編集。

```bash
# sample
DEBUG=1
APP_NAME="FastAPI Sample"
APP_VERSION="1.0.0"
DATABASE_DSN="postgresql+asyncpg://postgres:postgres@db:5432/sample"
```

起動。

```bash
docker-compose build --no-cache
docker-compose up -d
```

うまく起動したら早速アクセス

```url
http://localhost:8000/
```

## マイグレーションの適用

```bash
docker-compose exec api alembic upgrade head
```

# 開発環境の整備

## Python仮想環境

```bash
python -m venv .venv

# for Windows
source .venv/Scripts/activate
# for Mac/Linux
source .venv/bin/activate
```

## マイグレーションのリビジョン作成

```bash
docker-compose exec api alembic revision --autogenerate -m "brabra"
```
