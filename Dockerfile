FROM python:3.12-slim

RUN apt update && \
    useradd -m appuser

USER appuser

WORKDIR /asteroids

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]