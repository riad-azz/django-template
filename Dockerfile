# Pull base image
FROM python:latest

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get install -y netcat
RUN pip install --upgrade pip

# Set work directory
WORKDIR /code

# Copy dependencies
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy project
COPY . .