FROM python:3.11.13-alpine3.22

WORKDIR /app

COPY requirements*.txt ./

RUN pip3 install -r requirements.txt

RUN pip3 install -r requirements-dev.txt

COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]
