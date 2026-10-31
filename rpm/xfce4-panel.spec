# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfce4-panel
Version:        4.21.3
Release:        5%{?dist}
Summary:        Next generation panel for Xfce

License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfce4-panel/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel >= 0.12.0
BuildRequires:  garcon-devel >= %{xfce_version}
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-layer-shell-devel >= 0.7.0
BuildRequires:  gtk3-devel
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libxfce4ui-devel >= %{xfce_version}
BuildRequires:  libxfce4windowing-devel >= 4.20.6
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  meson
BuildRequires:  startup-notification-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  xfce4-session
BuildRequires:  xfconf-devel >= %{xfce_version}

%description
Next generation panel for Xfce.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for xfce4-panel.

%prep
%autosetup

%build
%meson \
    -Dgtk-doc=false \
    -Dintrospection=true \
    -Dvala=disabled \
    -Dx11=enabled \
    -Dwayland=enabled \
    -Dgtk-layer-shell=enabled \
    -Ddbusmenu=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/xfce4-panel
%{_bindir}/xfce4-popup-applicationsmenu
%{_bindir}/xfce4-popup-directorymenu
%{_bindir}/xfce4-popup-windowmenu
%{_libdir}/libxfce4panel-2.0.so.4
%{_libdir}/libxfce4panel-2.0.so.4.*
%{_libdir}/xfce4/panel/migrate
%{_libdir}/xfce4/panel/wrapper-2.0
%{_libdir}/xfce4/panel/plugins/*.so
%config(noreplace) %{_sysconfdir}/xdg/xfce4/panel/default.xml
%{_datadir}/applications/panel-desktop-handler.desktop
%{_datadir}/applications/panel-preferences.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel*.png
%{_datadir}/icons/hicolor/scalable/apps/org.xfce.panel*.svg
%{_datadir}/xfce4/applications/xfce4-panel.desktop
%{_datadir}/xfce4/panel/plugins/*.desktop

%files devel
%{_includedir}/xfce4/libxfce4panel-2.0/
%{_libdir}/libxfce4panel-2.0.so
%{_libdir}/pkgconfig/libxfce4panel-2.0.pc
%{_libdir}/girepository-1.0/Libxfce4panel-*
%{_datadir}/gir-1.0/Libxfce4panel-*

%changelog
