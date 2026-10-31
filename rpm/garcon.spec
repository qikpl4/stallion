# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           garcon
Version:        4.21.0
Release:        2%{?dist}
Summary:        Implementation of the freedesktop.org menu specification

License:        LGPL-2.1-or-later AND GFDL-1.1-or-later
URL:            https://docs.xfce.org/xfce/garcon/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfce_version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfce_version}
BuildRequires:  pkgconfig(gio-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc

Obsoletes:      libxfce4menu < 4.6.3
Conflicts:      xfdesktop <= 4.6.2

%description
Garcon is an implementation of the freedesktop.org menu specification replacing
the former Xfce menu library libxfce4menu. It is based on GLib/GIO only and
aims at covering the entire specification except for legacy menus.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(gtk+-3.0) >= 3.24.0
Requires:       pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=true \
    -Dintrospection=true \
    -Dtests=false

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%config(noreplace) %{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Garcon*
%{_datadir}/icons/hicolor/*/apps/org.xfce.garcon.png
%{_datadir}/gir-1.0/Garcon*
%{_datadir}/desktop-directories/*.directory

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/

%changelog
