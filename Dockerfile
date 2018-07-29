FROM ubuntu:latest

RUN mkdir -p /usr/src/application
WORKDIR /usr/src/application

COPY . /usr/src/application

RUN apt-get update -y
RUN apt install -y python3-pip python3-dev libxml2-dev libxslt-dev build-essential
RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application"]

# Expose the Flask port
EXPOSE 8000