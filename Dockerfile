FROM tiangolo/uvicorn-gunicorn:python3.9-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app
COPY .env /app/.env