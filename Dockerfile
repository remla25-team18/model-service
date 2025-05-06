FROM python:3.12-slim

RUN apt-get install -y git

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
