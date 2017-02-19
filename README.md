# container-gardening

![banner](./img/container.png)

TODO: Put more badges here.

> A collection of scripts and provisioning tools that help maintain my garden

TODO: Fill out this long description.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Install

```
```

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

PRs accepted.

## License

MIT © Ben Carothers
