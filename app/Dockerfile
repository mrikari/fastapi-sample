FROM python:3.12.2-slim-bookworm

COPY . /opt/app

WORKDIR /opt/app
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--reload", "--reload-dir", "/opt/app", "main:app"]
# CMD ["gunicorn", "main:app"]
