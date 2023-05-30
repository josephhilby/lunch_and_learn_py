# Dockerfile
# Chose python 3.11 as base image
FROM python:3.11.3-slim-buster

# Set working directory
# WORKDIR /app

# Copy requirements.txt to working directory
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    adduser --disabled-password --no-create-home app-runner

# Copy all files to working directory
COPY . .

USER app-runner

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]