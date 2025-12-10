FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set a proper working directory
WORKDIR /app

# Copy only dependency files first for caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen

# Copy project files
COPY . /app

# Run your Python script
ENTRYPOINT ["uv", "run", "call_server.py"]
