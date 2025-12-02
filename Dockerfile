FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set a proper working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies using uv
RUN uv sync --frozen --no-cache

# Run your Python script
ENTRYPOINT ["uv", "run", "call_server.py"]
