FROM resin/rpi-raspbian:jessie

RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install flask
RUN pip install flask_restful
RUN pip install tinydb

RUN git clone https://github.com/btcrs/container-gardening.git /data/container-gardening

WORKDIR /data
VOLUME /data

CMD ["python", "/data/container-gardening/gardener/gardener.py"]
