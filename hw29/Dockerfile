FROM python:3.10-slim

WORKDIR /app

COPY app/ app/
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "app"]