# container-gardening

![banner](./img/container.png)

> A collection of scripts and provisioning tools that help maintain my garden

container-gardening is a framework for creating a network of IOT sensors hosted
on Raspberry Pis. Each sensor is runs in a Docker container and uses the reporter
class to send a standardized message to the Gardener. The Gardener is a small REST/RPC 
data aggregator that acts as the messenger to and from the garden. Data is passed in the
form {"Parameter": XXX,"Value": XXX}. Once recieved, the Gardener can either store the data
locally, or in my case, pass it on to a centralized RESTful API.

Each machine in the garden has its own docker-compose.yml file organized in the compose directory.
Starting up that machine, or any machine with the same configuration, is a simple as typing `docker-compose up`.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Install

Machines are hardware dependent, but installation is simple. Docker and its ecosystem must
be installed.

#### To run a full machine installation

```
git pull https://github.com/btcrs/container-gardening.git
cd container-gardening
cd compose/*Machine Directory*
docker-machine up
```
This builds every necessary container

#### To run a single container

```
git pull https://github.com/btcrs/container-gardening.git
cd container-gardening
cd dockerfile/*Component*
```
Follow usage to build and run appropriately.

## Usage

```
docker build -t <tag> .
docker run --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -ti <tag>
```

To add env variables

```
docker run --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem -e [variables] --privileged -ti <tag>
```

The address of the Gardener machine is expected to be in an ENV variable named `GARDENER` the port
if the compose file is not modified will always be `80`.

## Contribute

PRs accepted.

## License

MIT © Ben Carothers
