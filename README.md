# Docker Compose demonstration

## Introduction

It's a simple demonstration of Docker and Docker Compose. It was created so I can show how to use these tools
on an example

## Requirements

You need to have [uv](https://docs.astral.sh/uv/) installed on your machine

Installing the environment:

```bash
uv venv
uv sync
```

The app requires an environment variable:

```dotenv
BOT_TOKEN=your_bot_token
```

## How to run

To run the application you need to execute the following command:

```bash
uv run app/main.py
```
