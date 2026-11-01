# Stallion

Stallion is an experimental suite shipping Xfce 4.21 (for the most part) using CentOS Stream 10.

It consists of both a [Copr repo](https://copr.fedorainfracloud.org/coprs/charles2/stallion/) and a bootc image.

## Source

The build metadata in `rpm/` consists of only files that we developed or forks of Fedora spec files.

Missing packages are either from Fedora or EPEL dist-git or SRPMs from older versions of CentOS Stream.

## Building bootc image

```
podman build -t stallion bootc
```
