FROM resin/rpi-raspbian:jessie

RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python3 \
    python3-dev \
    python3-pip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install schedule 
RUN pip3 install --process-dependency-links aosong
Run sed -ie 's/default_bus = 1 if revision() > 1 else 0/default_bus = 1/g' /usr/local/lib/python3.4/dist-packages/quick2wire/i2c.py   

RUN git clone https://github.com/btcrs/container-gardening.git /data/container-gardening
ENV PYTHONPATH="${PYTHONPATH}:/data/container-gardening/reporter/"

# Define working directory
WORKDIR /data
VOLUME /data

CMD ["python3", "/data/container-gardening/humidity/humidity.py"]
