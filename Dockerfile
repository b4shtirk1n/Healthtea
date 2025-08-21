FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN pip install uv
RUN uv sync --locked --all-extras
COPY . .
CMD ["uv", "run", "main.py"]