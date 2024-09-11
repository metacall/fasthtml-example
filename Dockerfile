FROM python:3.12.6-alpine3.20

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY main.py /app/

EXPOSE 5000

CMD [ "python3", "main.py"]
