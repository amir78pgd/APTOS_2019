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

#Setup File System
RUN mkdir ds
ENV HOME=/ds
ENV SHELL=/bin/bash
VOLUME /ds
WORKDIR /ds
ADD manage.py /ds/manage.py
RUN chmod +x /ds/manage.py
#RUN . /opt/venv/bin/activate
#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT python3 manage.py runserver
# Run a shell script
CMD  python3 /ds/manage.py runserver 0.0.0.0:8000
