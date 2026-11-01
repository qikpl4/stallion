# Stallion

Stallion is an experimental suite shipping Xfce 4.21 (for the most part) using CentOS Stream 10 and Wayland.

It consists of both a [Copr repo](https://copr.fedorainfracloud.org/coprs/charles2/stallion/) and a bootc image.

## Source

The build metadata in `rpm/` consists of only files that we developed or forks of Fedora spec files.

Missing packages are either from dist-git or SRPMs from Fedora/EPEL/CentOS.

## Building bootc image

```
podman build -t stallion bootc
```

## Usage of the bootc image

It is rather important to note that the bootc image does not automatically start Xfce upon login or a display manager. You have to manually run `xfwl4`.

Furthermore, the installation process will fail if the installer does not have a network connection.
