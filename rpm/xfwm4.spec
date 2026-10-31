# Xfce 4.20 spec file - xfwm4 is X11-only (no 4.21 series)
%global xfce_major 4
%global xfce_minor 20
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfwm4
Version:        4.20.0
Release:        2%{?dist}
Summary:        Next generation window manager for Xfce

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfwm4/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.20/%{name}-%{version}.tar.bz2

# Add missing -lxfce4util to settings dialogs (fixed upstream in git master).
# Needed when building against libxfce4ui >= 4.21, whose .pc keeps
# libxfce4util in Requires.private (so it is no longer linked transitively).
Patch0:         xfwm4-4.20.0-libxfce4util-link.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfce_version}
BuildRequires:  libXext-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  startup-notification-devel >= 0.5
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  xfconf-devel >= %{xfce_version}
BuildRequires:  desktop-file-utils

Provides:       firstboot(windowmanager) = xfwm4

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc example.gtkrc-2.0 TODO AUTHORS COMPOSITOR
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%{_libdir}/xfce4/xfwm4/helper-dialog
%{_datadir}/applications/xfce-wm-settings.desktop
%{_datadir}/applications/xfce-wmtweaks-settings.desktop
%{_datadir}/applications/xfce-workspaces-settings.desktop
%{_datadir}/xfwm4/defaults
%{_datadir}/themes/*/xfwm4
%{_datadir}/icons/hicolor/*/apps/org.xfce.xfwm4*.png
%{_datadir}/icons/hicolor/*/apps/org.xfce.workspaces.png
%{_datadir}/icons/hicolor/scalable/apps/org.xfce.xfwm4*.svg
%{_datadir}/icons/hicolor/scalable/apps/org.xfce.workspaces.svg
%{_datadir}/icons/hicolor/*/apps/xfwm4-default.*
%{_datadir}/icons/hicolor/scalable/actions/xfce-wm-*.svg
%{_datadir}/icons/hicolor/*/actions/xfce-wm-*.png

%changelog
