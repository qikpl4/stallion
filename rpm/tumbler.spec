# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           tumbler
Version:        4.21.1
Release:        3%{?dist}
Summary:        D-Bus service for applications to request thumbnails

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://docs.xfce.org/xfce/tumbler/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.72.0
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libgsf-devel
BuildRequires:  libopenraw-devel
BuildRequires:  libpng-devel
BuildRequires:  libxfce4util-devel >= %{xfce_version}
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-rpm-macros

%description
Tumbler is a D-Bus service for applications to request thumbnails for various
URI schemes and MIME types. It is an implementation of the thumbnail
management D-Bus specification described on
http://live.gnome.org/ThumbnailerSpec written in an object-oriented fashion.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications
that use %{name}.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=false \
    -Dcover-thumbnailer=enabled \
    -Ddesktop-thumbnailer=enabled \
    -Dffmpeg-thumbnailer=disabled \
    -Dfont-thumbnailer=enabled \
    -Dgepub-thumbnailer=disabled \
    -Dgst-thumbnailer=enabled \
    -Djpeg-thumbnailer=enabled \
    -Dodf-thumbnailer=enabled \
    -Dpixbuf-thumbnailer=enabled \
    -Dpoppler-thumbnailer=enabled \
    -Draw-thumbnailer=disabled \
    -Dxdg-cache=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%config(noreplace) %{_sysconfdir}/xdg/tumbler/tumbler.rc
%{_libdir}/libtumbler-1.so.0
%{_libdir}/libtumbler-1.so.0.*
%{_libdir}/tumbler-1/tumblerd
%{_libdir}/tumbler-1/plugins/*.so
%{_libdir}/tumbler-1/plugins/cache/*.so
%{_userunitdir}/tumblerd.service
%{_datadir}/dbus-1/services/org.xfce.Tumbler.*
%{_datadir}/icons/hicolor/*/apps/org.xfce.tumbler.png

%files devel
%{_includedir}/tumbler-1/
%{_libdir}/libtumbler-1.so
%{_libdir}/pkgconfig/tumbler-1.pc
%doc %{_datadir}/gtk-doc/html/tumbler

%changelog
