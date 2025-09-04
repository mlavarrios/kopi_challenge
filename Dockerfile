# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Copy requirements if present
COPY requirements.txt ./

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy application code
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/workspace/src"

# Default command (change as needed)
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]