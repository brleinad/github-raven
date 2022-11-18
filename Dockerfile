FROM python:3.9.7-slim-buster
ENV LANG C.UTF-8

# Python settings
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


RUN apt-get -y update && apt-get -y autoremove

RUN mkdir /app
WORKDIR /app

RUN apt-get install -y python python-pip python-dev && apt-get clean

COPY . .

RUN pip install -r requirements.txt

ENV ENV prod
ENV ALLOWED_HOSTS $ALLOWED_HOSTS

EXPOSE 8080
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8080"]