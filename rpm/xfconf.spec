# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfconf
Version:        4.21.2
Release:        2%{?dist}
Summary:        Hierarchical configuration system for Xfce

License:        GPL-2.0-only
URL:            https://docs.xfce.org/xfce/xfconf/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfce_version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(dbus-1) >= 1.1.0
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  systemd-rpm-macros

Requires:       dbus

Obsoletes:      libxfce4mcs < 4.4.3-3
Obsoletes:      xfconf-perl < 4.13.8

%description
Xfconf is a hierarchical (tree-like) configuration system where the
immediate child nodes of the root are called "channels".  All settings
beneath the channel nodes are called "properties."

%package devel
Summary:        Development tools for xfconf
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       dbus-devel
Requires:       glib2-devel

%description devel
This package includes the libraries and header files you will need
to compile applications for xfconf.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=false \
    -Dintrospection=true \
    -Dvala=enabled \
    -Dgsettings-backend=true

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/lib*.so.*
%{_bindir}/xfconf-query
%{_libdir}/xfce4/xfconf/
%{_libdir}/girepository-1.0/Xfconf-0.typelib
%{_datadir}/vala/vapi/libxfconf-0.deps
%{_datadir}/vala/vapi/libxfconf-0.vapi
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%{_datadir}/gir-1.0/Xfconf-0.gir
%{_datadir}/bash-completion/completions/xfconf-query
%{_userunitdir}/xfconfd.service

%files devel
%doc %{_datadir}/gtk-doc
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/xfconf-0
%{_libdir}/gio/modules/libxfconfgsettingsbackend.so

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.2-1
- Initial Xfce 4.21 spec file
