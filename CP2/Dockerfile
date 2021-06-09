#PULL the BASE IMAGE
FROM python:3.6.9

#env dependency
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#workdir
WORKDIR /CP2

#SET THE DEPENDANCY
COPY Pipfile Pipfile.lock /CP2/
RUN pip3 install pipenv && pipenv install --system

#copy the project
COPY . /CP2/