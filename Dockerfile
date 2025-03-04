FROM python:3.11-slim

ENV DB_URI=postgresql://app_user:app_password@localhost:5432/microservices
ENV DB_USER=app_user
ENV DB_PASSWORD=app_password
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_NAME=microservices

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--port", "8000", "--reload"]

EXPOSE 8000