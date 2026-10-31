# Xfce 4.21 spec file for xfce4-dev-tools
Name:           xfce4-dev-tools
Version:        4.21.2
Release:        2%{?dist}
Summary:        Development tools for Xfce

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfce4-dev-tools/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.21/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  gcc

%description
Xfce development tools, including scripts and utilities for building Xfce packages.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xdt-*
%{_bindir}/xfce-build
%{_bindir}/xfce-get-*
%{_bindir}/xfce-update-*
%{_bindir}/xfce-do-*
%{_datadir}/aclocal/*.m4
%{_mandir}/man1/xdt-*
%{_libdir}/cppcheck/cfg/xfce.cfg

%changelog
* Fri Oct 30 2026 qikp <qikp@example.com> - 4.21.2-1
- Initial Xfce 4.21 spec file
