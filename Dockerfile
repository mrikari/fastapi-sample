FROM python:3.12.2-slim-bookworm

COPY requirements.txt /tmp/requirements.txt

WORKDIR /code/app
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--reload", "--reload-dir", "/code/app", "main:app"]
