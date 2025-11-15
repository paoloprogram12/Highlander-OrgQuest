FROM ghcr.io/astral-sh/uv:debian
RUN mkdir /app
WORKDIR /app
COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --no-cache
COPY . .
#ENTRYPOINT ["/bin/bash", "-c"]
CMD ["uv", "run", "main.py"]
