.PHONY: help install test run down clean

help:
	@echo "Available commands:"
	@echo "  make           Show this help message"
	@echo "  make install   Install all requirements to run the service"
	@echo "  make test      Run tests"
	@echo "  make run       Run the service and all related services in Docker"
	@echo "  make down      Teardown all running services"
	@echo "  make clean     Teardown and remove all containers"

install:
	@echo "No need for installation, everything is Dockerized"

test:
	@echo "Running tests..."
	pytest

run:
	@echo "Starting application..."
	docker-compose up -d --build
	docker-compose exec app uvicorn src.main:app --host 0.0.0.0 --port 8080

down:
	@echo "Stopping all running services..."
	docker-compose down

clean:
	@echo "Stopping and removing all containers, volumes, and orphans..."
	docker-compose down --volumes --remove-orphans