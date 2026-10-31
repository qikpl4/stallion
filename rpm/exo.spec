# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           exo
Version:        4.21.0
Release:        2%{?dist}
Summary:        Application library for the Xfce desktop environment

License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/exo/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfce_version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gtk-doc
BuildRequires:  gettext
BuildRequires:  intltool >= 0.31
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfce_version}
BuildRequires:  libnotify-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel

%description
Extension library for Xfce, targeted at application development.

%package devel
Summary:        Development tools for exo library
Requires:       %{name} = %{version}-%{release}
Requires:       libxfce4util-devel
Requires:       pkgconfig

%description devel
Development tools and static libraries and header files for the exo library.

%prep
%autosetup

%build
%configure --enable-gtk-doc --disable-static
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang exo

%files -f exo.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS THANKS
%{_bindir}/exo-desktop-item-edit
%{_bindir}/exo-open
%{_libdir}/libexo-2.so.0
%{_libdir}/libexo-2.so.0.1.0
%{_datadir}/pixmaps/exo
%{_mandir}/man1/exo-open.1.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/exo*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
