FROM python:3.12-slim

RUN apt update && apt install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.cargo/bin/uv /usr/local/bin/

WORKDIR /asteroids
COPY . .

CMD ["uv", "run", "main.py"]
