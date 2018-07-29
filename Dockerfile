FROM python:3-alpine

RUN mkdir -p /usr/src/application
WORKDIR /usr/src/application

COPY . /usr/src/application

# RUN apt-get update -y
#RUN apt install -y python3-pip python3-dev libxml2-dev libxslt-dev
RUN apk add postgresql-libs  && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
    apk add libxml2-dev libxslt-dev && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps



CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application"]

# Expose the Flask port
EXPOSE 8000