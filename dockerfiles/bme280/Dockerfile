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

RUN pip install schedule
RUN git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
RUN cd Adafruit_Python_GPIO
RUN sudo python setup.py install

RUN git clone https://github.com/btcrs/container-gardening.git /data/container-gardening
ENV PYTHONPATH="${PYTHONPATH}:/data/container-gardening/reporter/"

WORKDIR /data
VOLUME /data

CMD ["python", "/data/container-gardening/multi/multi.py"]
