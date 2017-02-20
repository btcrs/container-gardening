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
    libffi-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install smbus-cffi

RUN git clone https://github.com/btcrs/container-gardening.git /data/container-gardening

WORKDIR /data
VOLUME /data

CMD ["python", "/data/container-gardening/pressure/5803/pressure.py"]
