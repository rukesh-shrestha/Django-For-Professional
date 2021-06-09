#pull the base image
FROM python:3.6.9

#ENV DEPENDENCY
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#WORKING DIR
WORKDIR /CP6

#COPY THE PROJECT FILES
COPY Pipfile Pipfile.lock /CP6/
RUN pip install pipenv && pipenv install --system

#copy the project
COPY . /CP6/