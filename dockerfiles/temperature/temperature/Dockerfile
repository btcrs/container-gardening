FROM resin/rpi-raspbian:jessie

RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    python-smbus \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install schedule 
RUN pip install envirophat
RUN git clone https://github.com/btcrs/container-gardening.git /data/container-gardening
ENV PYTHONPATH="${PYTHONPATH}:/data/container-gardening/reporter/"

WORKDIR /data
VOLUME /data

CMD ["python", "/data/container-gardening/temperature/temperature.py"]
