lint:
	uv run ruff check --fix

format:
	ruff format

run:
	uv run app/main.py

docker:
	docker build -t docker_demonstration_image .
	docker run -e BOT_TOKEN=$$BOT_TOKEN --name docker_demonstration_container -it \
           docker_demonstration_image
	docker stop docker_demonstration_container || true
	docker rm -f docker_demonstration_container || true
	docker rmi docker_demonstration_image || true

docker-compose-up:
	docker compose up --build -d

docker-compose-logs:
	docker compose logs

docker-compose-stop:
	docker compose down --rmi local
