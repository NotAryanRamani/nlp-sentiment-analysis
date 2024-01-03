FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD gunicorn --bind 0.0.0.0:$PORT application:application