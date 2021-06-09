#pull the base image
FROM python:3.6.9

#set the env dependency
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#SET the workingdir
WORKDIR /CP5

#COPY THE FILE AND DEPENDENCY
COPY Pipfile Pipfile.lock /CP5/
RUN pip install pipenv && pipenv install --system

#COPY the project
COPY . /CP5/