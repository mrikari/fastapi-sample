[FastAPI](https://fastapi.tiangolo.com/) Sample 動作確認のために作っています。

# ことはじめ

##　起動

まずは起動。

```bash
docker-compose build --no-cache
docker-compose up -d
```

うまく起動したら早速アクセス: [http://localhost:8000/](http://localhost:8000/)

## マイグレーションの適用

```bash
docker-compose exec app bash
```

ターミナルに入れたらマイグレーション実行

```bash
alembic upgrade head
exit
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
docker-compose exec app bash
```

ターミナルに入れたらマイグレーション実行

```bash
alembic revision --autogenerate -m "brabra"
exit
```
