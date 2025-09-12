.PHONY: help install test run down clean

help:
	@echo "Available commands:"
	@echo "  make           Show this help message"
	@echo "  make install   Checks for required tools (Docker and Node.js)"
	@echo "  make test      Run tests"
	@echo "  make run       Start all services in Docker"
	@echo "  make down      Teardown all running services"
	@echo "  make clean     Teardown and remove all containers"

install:
	@echo "Checking for Docker Desktop..."
	@if ! docker --version >/dev/null 2>&1; then \
		echo "Docker is not installed. Please install Docker Desktop."; exit 1; \
	else \
		echo "Docker is installed."; \
	fi
	@echo "Checking for Node.js..."
	@if ! node --version >/dev/null 2>&1; then \
		echo "Node.js is not installed. Please install Node.js."; exit 1; \
	else \
		echo "Node.js is installed."; \
	fi
	@echo "All required tools are installed."

test:
	@echo "Running tests..."
	docker-compose exec app pytest -v

run:
	@echo "Starting containers..."
	docker-compose up -d
	npx supabase start
	npx supabase db reset --db-url "postgresql://postgres:postgres@localhost:54322/postgres" --yes --debug

down:
	@echo "Stopping all running services..."
	docker-compose down
	npx supabase stop

clean:
	@echo "Stopping and removing all containers, volumes, and orphans..."
	docker-compose down --volumes --remove-orphans
	npx supabase stop