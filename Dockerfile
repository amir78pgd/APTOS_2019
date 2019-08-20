# reference: https://hub.docker.com/_/ubuntu/
FROM python:3.6

RUN apt-get update && apt-get install -y python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Adds metadata to the image as a key value pair example LABEL version="1.0"
LABEL maintainer="Amir Ashraff <amir.ashraff@gmail.com>"

##Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Open Ports for Web App
EXPOSE 8000

WORKDIR /manage.py

COPY . /manage.py

#Setup File System
ENTRYPOINT [ "python3" ]


# Run a shell script
CMD [ "python3", "manage.py runserver 0.0.0.0:8000" ]
