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

The app requires `.env` file with the following content:

```dotenv
BOT_TOKEN=your_bot_token
```

## Running locally

First, **load the `.env` file**. Then to run the application you need to execute makefile target `run`:

```bash
make run
```

## Running in Docker

To run the application in Docker, you need to execute makefile target `docker`:

```bash
make docker
```

It automatically builds the image and runs the container.
After the container stops, the image and container are removed

## Running in Docker Compose

To run the application in Docker Compose, you need to execute makefile target `docker-compose`:

```bash
make docker-compose
```

It automatically builds the image and runs the container in
[detached mode](https://docs.docker.com/compose/reference/up/).

To get the logs generated by the application, you can execute:

```bash
make docker-compose-logs
```

To stop the application and remove images, you can execute:

```bash
make docker-compose-stop
```
