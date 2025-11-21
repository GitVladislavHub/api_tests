FROM python:3.14-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install allure-pytest


COPY . .

CMD ["python", "-m", "pytest", "tests/", "-v", "--alluredir=/app/allure-results"]
