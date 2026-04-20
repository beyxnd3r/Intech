FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install grpcio

CMD ["python", "server.py"]