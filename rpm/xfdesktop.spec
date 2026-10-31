# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfdesktop
Version:        4.21.1
Release:        2%{?dist}
Summary:        Desktop manager for the Xfce Desktop Environment

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfdesktop/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel >= 0.12.0
BuildRequires:  garcon-devel >= 0.1.2
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libgudev1-devel >= 145
BuildRequires:  libICE-devel
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  libSM-devel
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libxfce4ui-devel >= %{xfce_version}
BuildRequires:  libxfce4windowing-devel >= 4.20.6
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  Thunar-devel >= 1.8.0
BuildRequires:  xfconf-devel >= %{xfce_version}

Requires:       xfwm4 >= 4.20
Requires:       xfce4-panel >= %{xfce_version}

%description
This package includes a desktop manager for the Xfce Desktop Environment.

%prep
%autosetup

%build
%meson \
    -Dtests=false

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/xfdesktop
%{_bindir}/xfdesktop-settings
%{_datadir}/applications/xfdesktop-settings.desktop
%{_datadir}/backgrounds/xfce/*.jpg
%{_datadir}/backgrounds/xfce/*.svg
%{_datadir}/icons/hicolor/*/apps/org.xfce.xfdesktop.*
%{_datadir}/pixmaps/xfce4_xicon*.png
%{_datadir}/pixmaps/xfdesktop/xfdesktop-fallback-icon.png
%{_datadir}/xfce4/applications/xfdesktop.desktop
%{_mandir}/man1/xfdesktop.1*

%changelog
