# reference: https://hub.docker.com/_/ubuntu/
FROM ubuntu:18.04

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

# Adds metadata to the image as a key value pair example LABEL version="1.0"
LABEL maintainer="Amir Ashraff <amir.ashraff@gmail.com>"

##Set environment variables
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Open Ports for Web App
EXPOSE 8000

WORKDIR /manage.py

COPY . /manage.py
ENTRYPOINT [ "python3" ]
CMD [ "python3", "manage.py runserver 0.0.0.0:8000" ]
