# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfce4-session
Version:        4.21.2
Release:        1%{?dist}
Summary:        Xfce session manager

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfce4-session/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.72.0
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-devel >= 3.24.0
BuildRequires:  intltool
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libwnck3-devel >= 3.10.0
BuildRequires:  libxfce4ui-devel >= %{xfce_version}
BuildRequires:  libxfce4util-devel >= %{xfce_version}
BuildRequires:  libxfce4windowing-devel >= 4.19.2
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  xfconf-devel >= %{xfce_version}
BuildRequires:  xrdb

# xset and iceauth are only used by the shipped xinitrc/scripts and are not
# packaged in CentOS Stream 10. They are optional at runtime.
Requires:       exo
Requires:       polkit
Requires:       systemd >= 195
Requires:       xrdb

Suggests:       imsettings-xfce
Suggests:       xfce4-screensaver

Obsoletes:      xfce-utils < 4.8.3-7.fc18
Obsoletes:      xfce4-session-engines <= 4.13.1
Obsoletes:      xfce4-session-devel <= 4.13.3

%description
xfce4-session is the session manager for the Xfce desktop environment.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for xfce4-session.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=true \
    -Dintrospection=true \
    -Dvala=disabled \
    -Dx11=enabled \
    -Dwayland=enabled \
    -Dgtk-layer-shell=enabled \
    -Dpolkit=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/startxfce4
%{_bindir}/xfce4-session
%{_bindir}/xfce4-session-logout
%{_bindir}/xfce4-session-settings
%{_bindir}/xflock4
%{_libdir}/libxfce4session-client-1.so.0
%{_libdir}/libxfce4session-client-1.so.0.*
%{_libdir}/xfce4/session/xfsm-shutdown-helper
%config(noreplace) %{_sysconfdir}/xdg/xfce4/Xft.xrdb
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xinitrc
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%{_datadir}/applications/xfce4-session-logout.desktop
%{_datadir}/applications/xfce4-session-settings.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.session.*
%{_datadir}/icons/hicolor/*/actions/xfsm-*.png
%{_datadir}/man/man1/xfce4-session.1*
%{_datadir}/man/man1/xfce4-session-logout.1*
%{_datadir}/polkit-1/actions/org.xfce.session.policy
%{_datadir}/wayland-sessions/xfce-wayland.desktop
%{_datadir}/xdg-desktop-portal/xfce-portals.conf
%{_datadir}/xsessions/xfce.desktop
%{_datadir}/xfce4/labwc/labwc-environment
%{_datadir}/xfce4/labwc/labwc-rc.xml

%files devel
%{_includedir}/xfce4/libxfce4session-client-1/
%{_libdir}/libxfce4session-client-1.so
%{_libdir}/pkgconfig/libxfce4session-client-1.pc
%{_libdir}/girepository-1.0/Libxfce4sessionclient-*
%{_datadir}/gir-1.0/Libxfce4sessionclient-*
%doc %{_datadir}/gtk-doc/html/libxfce4session-client

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.2-1
- Initial Xfce 4.21 spec file
