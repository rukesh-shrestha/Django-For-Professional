# Pull base image
From python:3.6.9

# Set env variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /code

# Install dependencies
COPY /env/Pipfile /env/Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy Project
COPY . /code/

