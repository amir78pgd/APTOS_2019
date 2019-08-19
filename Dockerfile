# reference: https://hub.docker.com/_/ubuntu/
FROM ubuntu:16.04

# Adds metadata to the image as a key value pair example LABEL version="1.0"
LABEL maintainer="Amir Ashraff <amir.ashraff@gmail.com>"

##Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Open Ports for Web App
EXPOSE 8000

#Setup File System

# Run a shell script
CMD  ["./python3 manage.py runserver"]
