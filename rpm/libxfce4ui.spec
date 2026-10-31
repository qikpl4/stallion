# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           libxfce4ui
Version:        4.21.9
Release:        1%{?dist}
Summary:        Commonly used Xfce widgets

License:        LGPL-2.1-or-later
URL:            https://docs.xfce.org/xfce/libxfce4ui/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfce_version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  libSM-devel
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfce_version}
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.24.0
BuildRequires:  pkgconfig(epoxy) >= 1.2
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  xfce4-dev-tools

Obsoletes:      libxfcegui4 < 4.10.0-9

%description
Libxfce4ui is used to share commonly used Xfce widgets among the Xfce
applications.

%package -n     xfce4-about
Summary:        Xfce 4 'About' dialog

%description -n xfce4-about
This package contains the 'About Xfce' dialog with info on the desktop
environment, its contributors, and its licensing.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk3-devel
Requires:       libxfce4util-devel
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
    -Dvala=enabled \
    -Dx11=enabled \
    -Dwayland=enabled \
    -Dsession-management=enabled \
    -Dstartup-notification=enabled \
    -Dlibgtop=enabled \
    -Depoxy=enabled \
    -Dgudev=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS THANKS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_bindir}/xfce-open
%{_bindir}/xfce-desktop-item-edit
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Libxfce4ui-2.0.typelib
%{_datadir}/gir-1.0/Libxfce4ui-2.0.gir
%{_datadir}/vala/vapi/libxfce4ui-2.deps
%{_datadir}/vala/vapi/libxfce4ui-2.vapi
%{_libdir}/girepository-1.0/Libxfce4kbdprivate-3.0.typelib
%{_datadir}/gir-1.0/Libxfce4kbdprivate-3.0.gir
%{_datadir}/pixmaps/libxfce4ui/

%files -n xfce4-about
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_datadir}/icons/hicolor/*/apps/*xfce*

%files devel
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.9-1
- Initial Xfce 4.21 spec file
