PYTHON = python3
PIP = pip
DOCKER_COMPOSE = docker-compose
PROJECT_NAME = batch_insert_project
DOCKER_IMAGE = batch_insert_with_python_image

install:
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

run:
	@echo "Running the project..."
	$(PYTHON) main.py

clean-cache:
	@echo "Cleaning up __pycache__ directories..."
	find . -type d -name '__pycache__' -exec rm -r {} +

compose-up:
	@echo "Starting services with Docker Compose..."
	$(DOCKER_COMPOSE) up --build

compose-down:
	@echo "Stopping Docker Compose services..."
	$(DOCKER_COMPOSE) down

compose-rebuild:
	@echo "Rebuilding and restarting Docker Compose services..."
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) up --build

# Help menu
help:
	@echo "Available commands:"
	@echo "  make install            - Install dependencies"
	@echo "  make run                - Run the project locally"
	@echo "  make clean-cache              - Remove __pycache__ directories"
	@echo "  make compose-up         - Start services with Docker Compose"
	@echo "  make compose-down       - Stop Docker Compose services"
	@echo "  make compose-rebuild    - Rebuild and restart Docker Compose services"
