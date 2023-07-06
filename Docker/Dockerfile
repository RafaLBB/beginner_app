FROM python:3.7.4-slim-stretch

EXPOSE 8000

RUN apt-get -y update

RUN apt-get install -y --fix-missing \
    build-essential \
    git \
    wget \
    curl \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "app:app" ]

