.PHONY: help install test up down run clean

help:
	@echo "Available commands:"
	@echo "  make           Show this help message"
	@echo "  make install   Install all requirements to run the service"
	@echo "  make test      Run tests"
	@echo "  make up        Start all services in Docker"
	@echo "  make down      Teardown all running services"
	@echo "  make run       Run the API"
	@echo "  make clean     Teardown and remove all containers"

install:
	@echo "No need for installation, everything is Dockerized"

test:
	@echo "Running tests..."
	docker-compose exec app pytest -v

up:
	@echo "Starting containers..."
	docker-compose up -d --build

down:
	@echo "Stopping all running services..."
	docker-compose down

run:
	docker-compose exec app uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

clean:
	@echo "Stopping and removing all containers, volumes, and orphans..."
	docker-compose down --volumes --remove-orphans