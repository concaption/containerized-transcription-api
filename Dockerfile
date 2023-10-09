# Author: concaption
# Date Created: 2023-10-09

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Update and install dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg

# Copy src directory to /app
COPY src /app/src

# Expose port 8000
EXPOSE 8000

# Run app using uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
