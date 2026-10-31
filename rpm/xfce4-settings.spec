# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfce4-settings
Version:        4.21.3
Release:        1%{?dist}
Summary:        Settings Manager for Xfce

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfce4-settings/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  colord-devel
BuildRequires:  desktop-file-utils >= 0.7
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  garcon-devel >= %{xfce_version}
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  intltool
BuildRequires:  libXrandr-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libnotify-devel
BuildRequires:  libxfce4ui-devel >= %{xfce_version}
BuildRequires:  libxfce4util-devel >= %{xfce_version}
BuildRequires:  libxklavier-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  xfconf-devel >= %{xfce_version}

Requires:       xfconf

%description
This package includes the settings manager applications for the Xfce desktop.

%prep
%autosetup

%build
%meson \
    -Dx11=enabled \
    -Dwayland=enabled \
    -Dlibnotify=enabled \
    -Dlibxklavier=enabled \
    -Dxcursor=enabled \
    -Dxorg-libinput=disabled \
    -Dxrandr=enabled \
    -Dgtk-layer-shell=enabled \
    -Dupower=enabled \
    -Dcolord=enabled \
    -Dsound-settings=true

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/xfce4-accessibility-settings
%{_bindir}/xfce4-appearance-settings
%{_bindir}/xfce4-color-settings
%{_bindir}/xfce4-display-settings
%{_bindir}/xfce4-find-cursor
%{_bindir}/xfce4-keyboard-settings
%{_bindir}/xfce4-mime-helper
%{_bindir}/xfce4-mime-settings
%{_bindir}/xfce4-mouse-settings
%{_bindir}/xfce4-settings-editor
%{_bindir}/xfce4-settings-manager
%{_bindir}/xfsettingsd
%{_libdir}/gtk-3.0/modules/libxfsettingsd-gtk-settings-sync.so
%{_libdir}/xfce4/settings/appearance-install-theme
%{_libdir}/xfce4/xfce4-compose-mail
%config(noreplace) %{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%config(noreplace) %{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%config(noreplace) %{_sysconfdir}/xdg/xfce4/helpers.rc
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%{_datadir}/applications/xfce4-*-settings.desktop
%{_datadir}/applications/xfce4-settings-*.desktop
%{_datadir}/applications/xfce4-audio-player.desktop
%{_datadir}/applications/xfce4-file-manager.desktop
%{_datadir}/applications/xfce4-image-viewer.desktop
%{_datadir}/applications/xfce4-mail-reader.desktop
%{_datadir}/applications/xfce4-terminal-emulator.desktop
%{_datadir}/applications/xfce4-text-editor.desktop
%{_datadir}/applications/xfce4-video-player.desktop
%{_datadir}/applications/xfce4-web-browser.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.*
%{_datadir}/icons/hicolor/*/devices/xfce-display-*.png
%{_datadir}/icons/hicolor/scalable/devices/xfce-display-*.svg
%{_datadir}/xfce4/helpers/*.desktop

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.3-1
- Initial Xfce 4.21 spec file
