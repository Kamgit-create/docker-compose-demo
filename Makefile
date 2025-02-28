lint:
	uv run ruff check --fix

format:
	ruff format

run:
	uv run app/main.py
