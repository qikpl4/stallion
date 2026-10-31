# Xfce 4.21 spec file for xfwl4 - Maintainable for 4.22
# NOTE: Requires additional dependencies not in CentOS Stream 10 repos:
#   - libdisplay-info >= 0.3.0 (currently 0.2.0 in repos)
#   - pixman >= 0.44.0 (currently 0.43.4 in repos)  
#   - libseat >= 0.9.0 (not in repos)
# Build these first before attempting xfwl4.

%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfwl4
Version:        4.21.1
Release:        2%{?dist}
Summary:        Xfce Wayland compositor

License:        GPL-3.0-or-later
URL:            https://docs.xfce.org/xfce/xfwl4/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

# Rust toolchain
BuildRequires:  cargo >= 1.92.0
BuildRequires:  rustc >= 1.92.0

# Core build tools
BuildRequires:  meson >= 0.57.0
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig

# System libraries
BuildRequires:  libdrm-devel >= 2.4.0
BuildRequires:  mesa-libgbm-devel >= 25.0.0
BuildRequires:  libinput-devel >= 1.28.0
BuildRequires:  libxkbcommon-devel >= 0.8.0
BuildRequires:  pixman-devel >= 0.44.0
BuildRequires:  libseat-devel >= 0.9.0
BuildRequires:  systemd-devel >= 257

# Display detection
BuildRequires:  libdisplay-info-devel >= 0.3.0

# Xfce dependencies
BuildRequires:  libxfce4ui-devel >= 4.21.4
BuildRequires:  pkgconfig(libxfconf-0) >= 4.21.2

# XWayland (optional but recommended)
Requires:       xorg-x11-server-Xwayland

# Runtime deps
Requires:       dbus-x11
Requires:       xfwm4 >= 4.20
Requires:       libxfce4windowing >= 4.20.7
Requires:       xfce4-settings >= 4.21.3
Requires:       xfdesktop >= 4.21.0

%description
xfwl4 is the Wayland compositor for Xfce. It is written in Rust using the
smithay framework and aims to provide feature parity with xfwm4 on Wayland.

Note: This is an experimental compositor under active development.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for xfwl4.

%prep
%autosetup

%build
%meson \
    -Doptimization=2 \
    -Ddebug=true

%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/xfwl4
%{_datadir}/wayland-sessions/xfwl4.desktop
%{_datadir}/locale/*/LC_MESSAGES/xfwl4.mo
%{_datadir}/xfce4/xfwl4/defaults

%changelog
