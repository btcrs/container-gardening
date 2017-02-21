# container-gardening

![banner](./img/container.png)

[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)]() [![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Star)]()

> A collection of scripts and provisioning tools that help maintain my garden

TODO: Fill out this long description.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Install

```
git pull https://github.com/btcrs/container-gardening.git
cd container-gardening
cd dockerfiles
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

## Contribute

**Remaining**

- humidity (docker & code)
- ph (docker)
- dockercompose

PRs accepted.

## License

MIT © Ben Carothers
