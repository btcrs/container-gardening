FROM resin/rpi-raspbian:jessie

RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install adafruit-mcp3008
RUN pip install schedule 

RUN git clone https://github.com/btcrs/container-gardening.git /data/container-gardening

# Define working directory
WORKDIR /data
VOLUME /data

CMD ["python", "/data/container-gardening/depth/depth.py"]
