#pull the imagesENV
FROM python:3.6.9

#det the env dependency
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#WORKING ENV
WORKDIR /CP3

# INSTALL THE DEPENDENCY
COPY Pipfile Pipfile.lock /CP3/
RUN pip install pipenv && pipenv install --system

#COPY THE PROJECT
COPY . /CP3/
