FROM python:3.11-slim

RUN mkdir workspace
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git make curl && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Clean up
RUN apt-get clean
RUN pip install "poetry"
RUN poetry config virtualenvs.create false
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/workspace/src"
# RUN poetry install
RUN rm -R *

# CMD ["poetry", "run", "uvicorn", "src.application.debate_controller:router", "--host", "0.0.0.0", "--port", "8000"]
