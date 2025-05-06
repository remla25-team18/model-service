FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y git gcc build-essential

RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
