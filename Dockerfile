# Dockerfile
# Chose python 3.11 as base image
FROM python:3.11-bullseye

# Set working directory
# WORKDIR /app

# Copy requirements.txt to working directory
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy all files to working directory
COPY . .
