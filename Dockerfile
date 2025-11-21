FROM python:3.12-slim 

WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install allure-pytest


COPY . .

CMD ["python", "-m", "pytest", "tests/", "-v", "--alluredir=/app/allure-results"]
