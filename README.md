# container-gardening

Dockerized IOT components used to collect data on my hydroponic garden.

## Usage

```
docker build -t <tag> .
docker run --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -ti btcrs/temperature
```
