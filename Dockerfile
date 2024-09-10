FROM python:3.12.6-alpine3.20

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "server.py"]