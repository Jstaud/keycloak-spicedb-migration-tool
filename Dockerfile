# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install --no-cache-dir --upgrade poetry

# Install dependencies using Poetry
RUN poetry install --no-root

# Run tests
RUN poetry run pytest

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run k2spicedb when the container launches
CMD ["poetry", "run", "k2spicedb"]