FROM python:3.8-slim-buster

# make app directory for all files in build
RUN mkdir -p /app
WORKDIR /app

# install python dependencies under requirements.txt
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# add source code to build
ADD ./src/ /app/