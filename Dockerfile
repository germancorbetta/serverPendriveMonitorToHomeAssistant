# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the script into the container
COPY script.py /app/script.py

# Update the system and install dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir flask \
    && rm -rf /var/lib/apt/lists/*

# Expose the port Flask is listening to
EXPOSE 5590

# Set the command to run the script
CMD ["python3", "/app/script.py"]