# set base image
FROM python:3.13-alpine

# set working directory
WORKDIR /app

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy dependencies
COPY pyproject.toml .
COPY uv.lock .

# install dependencies
RUN uv sync --frozen --no-install-project --no-dev

# add project files
COPY app/ app/

# run app
CMD ["uv", "run", "app/main.py"]
