FROM python:3.10-slim

WORKDIR /app

COPY app/ app/
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install allure-pytest

CMD ["pytest", "app", "-q", "--alluredir=/allure-results"]