FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN uv run call_server.py

COPY call_server.py .

ENTRYPOINT ["python", "call_server.py"]