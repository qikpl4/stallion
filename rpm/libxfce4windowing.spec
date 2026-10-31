# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           libxfce4windowing
Version:        4.20.7
Release:        1%{?dist}
Summary:        Windowing concept abstraction library for X11 and Wayland

License:        LGPL-2.1-or-later
URL:            https://docs.xfce.org/xfce/libxfce4windowing/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.20/%{name}-%{version}.tar.bz2

BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig(gdk-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.40.8
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.68.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.68.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.68.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gtk-doc) >= 1.30
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner) >= 1.20
BuildRequires:  tar
BuildRequires:  xfce4-dev-tools >= 4.19.4
BuildRequires:  pkgconfig(libdisplay-info) >= 0.1.1
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(xrandr) >= 1.5.0

Recommends:     gdk-pixbuf2-modules-extra

%description
Libxfce4windowing is an abstraction library that attempts to present
windowing concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for libxfce4windowing.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=true \
    -Dintrospection=true \
    -Dvala=enabled \
    -Dtests=false

%meson_build

%install
%meson_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc NEWS ChangeLog
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Libxfce4windowing*
%{_datadir}/gir-1.0/Libxfce4windowing*
%{_datadir}/vala/vapi/libxfce4windowing-0.vapi
%{_datadir}/vala/vapi/libxfce4windowing-0.deps
%{_datadir}/vala/vapi/libxfce4windowingui-0.vapi
%{_datadir}/vala/vapi/libxfce4windowingui-0.deps

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.20.7-1
- Initial Xfce 4.20 spec file
