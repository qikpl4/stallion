# Xfce 4.21 spec file - Maintainable for 4.22
%global xfce_major 4
%global xfce_minor 21
%global xfce_version %{xfce_major}.%{xfce_minor}

Name:           xfce4-appfinder
Version:        4.21.1
Release:        1%{?dist}
Summary:        Application finder for Xfce

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfce4-appfinder/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  garcon-devel >= %{xfce_version}
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libxfce4ui-devel >= %{xfce_version}
BuildRequires:  libxfce4util-devel >= %{xfce_version}
BuildRequires:  make
BuildRequires:  meson

Requires:       exo

%description
xfce4-appfinder is an application finder for the Xfce desktop environment.

%prep
%autosetup

%build
%meson

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/xfce4-appfinder
%{_bindir}/xfrun4
%{_datadir}/applications/xfce4-appfinder.desktop
%{_datadir}/applications/xfce4-run.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.appfinder.*
%{_datadir}/metainfo/org.xfce.xfce4-appfinder.appdata.xml

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.1-1
- Initial Xfce 4.21 spec file
