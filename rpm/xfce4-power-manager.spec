# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfce4-power-manager
Version:        4.21.1
Release:        2%{?dist}
Summary:        Power management for the Xfce desktop environment

License:        GPL-2.0-or-later
URL:            https://goodies.xfce.org/projects/applications/%{name}
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.72.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.8
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.102
BuildRequires:  pkgconfig(upower-glib) >= 0.99.10
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner) >= 1.20
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xrandr) >= 1.5.0

Requires:       xfce4-panel >= %{xfce_version}
Requires:       polkit
Requires:       upower >= 0.99

%description
Xfce Power Manager uses the information and facilities provided by UPower to
display icons and handle user callbacks in an interactive Xfce session.
Xfce Power Preferences allows authorised users to set policy and change
preferences.

%prep
%autosetup

%build
%meson \
    -Dx11=enabled \
    -Dwayland=enabled \
    -Dpanel-plugin=enabled \
    -Dpolkit=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/xfce4-power-manager
%{_bindir}/xfce4-power-manager-settings
%{_sbindir}/xfce4-pm-helper
%{_sbindir}/xfpm-power-backlight-helper
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%config(noreplace) %{_sysconfdir}/xdg/autostart/xfce4-power-manager.desktop
%{_datadir}/applications/xfce4-power-manager-settings.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.powermanager.*
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/man/man1/xfce4-power-manager.1*
%{_datadir}/man/man1/xfce4-power-manager-settings.1*
%{_datadir}/metainfo/org.xfce.PowerManager.appdata.xml
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop

%changelog
