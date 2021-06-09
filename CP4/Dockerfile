#pull the base image
FROM python:3.6.9

#set the env dependency
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set the workring dir
WORKDIR /CP4

# copy the dependency
COPY Pipfile Pipfile.lock /CP4/
RUN pip install pipenv && pipenv install --system

#COPY the project
COPY . /CP4/
