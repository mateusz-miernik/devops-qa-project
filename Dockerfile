FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . .
WORKDIR .
RUN uv sync --frozen --no-cache

ENTRYPOINT ["python", "call_server.py"]