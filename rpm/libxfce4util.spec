# Xfce 4.21 spec file - Maintainable for 4.22
# Version variables at the top for easy updates

%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           libxfce4util
Version:        4.21.0
Release:        1%{?dist}
Summary:        Utility library for the Xfce desktop environment

License:        LGPL-2.1-or-later
URL:            https://docs.xfce.org/xfce/libxfce4util/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfce_version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  vala

%description
This package includes basic utility non-GUI functions for Xfce.

%package devel
Summary:        Development files for libxfce4util
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel
Requires:       gtk3-devel
Requires:       pkgconfig

%description devel
This package includes static libraries and header files for the
libxfce4util library.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=true \
    -Dintrospection=true \
    -Dvala=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/lib*.so.*
%{_sbindir}/xfce4-kiosk-query
%{_libdir}/girepository-1.0/Libxfce4util-1.0.typelib
%{_datadir}/gir-1.0/Libxfce4util-1.0.gir
%{_datadir}/vala/vapi/libxfce4util-1.0.vapi
%{_datadir}/vala/vapi/libxfce4util-1.0.deps

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4
%doc %{_datadir}/gtk-doc/

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.0-1
- Initial Xfce 4.21 spec file
