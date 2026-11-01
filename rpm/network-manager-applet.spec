# For some unfathomably stupid reason, Red Hat decided to remove all of the functionality in c10s.
# As such, the package from c9s is taken (and modified) here.

%global gtk3_version    %(pkg-config --modversion gtk+-3.0 2>/dev/null || echo bad)
%global gtk4_version    %(pkg-config --modversion gtk4 2>/dev/null || echo bad)
%global glib2_version   %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global nm_version      1:1.16.0
%global libnma_version  1.8.27
%global obsoletes_ver   1:0.9.7

%global rpm_version 1.26.0
%global real_version 1.26.0
%global release_version 3
%global epoch 1

%global real_version_major 1.26

%if 0%{?fedora} > 31 || 0%{?rhel} > 8
%bcond_with libnma_gtk4
%else
%bcond_without libnma_gtk4
%endif

%if 0%{?fedora} || 0%{?rhel} < 9
%bcond_without appindicator
%else
%bcond_with appindicator
%endif

Name: network-manager-applet
Summary: A network control and status applet for NetworkManager
Version: %{rpm_version}
Release: %{release_version}%{?dist}
Epoch:   %{epoch}
License: GPLv2+
URL: http://www.gnome.org/projects/NetworkManager/
Obsoletes: NetworkManager-gnome < %{obsoletes_ver}

Source: https://download.gnome.org/sources/network-manager-applet/%{real_version_major}/%{name}-%{real_version}.tar.xz
# Patch1: 0001-sample-name.patch
# Patch1: 0001-po-ja-update-Japanese-translation.patch

Requires: NetworkManager >= %{nm_version}
Requires: libnotify >= 0.4.3
Requires: nm-connection-editor%{?_isa} = %{epoch}:%{version}-%{release}
Requires: libnma%{?_isa} >= %{libnma_version}

BuildRequires: NetworkManager-libnm-devel >= %{nm_version}
BuildRequires: libnma-devel >= %{libnma_version}
BuildRequires: ModemManager-glib-devel >= 1.0
BuildRequires: glib2-devel >= 2.32
BuildRequires: gtk3-devel >= 3.10
%if %{with libnma_gtk4}
BuildRequires: gtk4-devel >= 3.96
%endif
BuildRequires: gobject-introspection-devel >= 0.10.3
BuildRequires: gettext-devel
BuildRequires: /usr/bin/autopoint
BuildRequires: pkgconfig
BuildRequires: libnotify-devel >= 0.4
BuildRequires: meson
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: desktop-file-utils
BuildRequires: iso-codes-devel
BuildRequires: libgudev1-devel >= 147
BuildRequires: libsecret-devel >= 0.12
BuildRequires: jansson-devel
BuildRequires: gcr-devel
BuildRequires: libselinux-devel
BuildRequires: mobile-broadband-provider-info-devel
%if %{with appindicator}
BuildRequires: libappindicator-gtk3-devel
%endif
%if 0%{?fedora} || 0%{?rhel} < 9
BuildRequires: libdbusmenu-gtk3-devel
%endif

%description
This package contains a network control and status notification area applet
for use with NetworkManager.

%package -n nm-connection-editor
Summary: A network connection configuration editor for NetworkManager
Requires: libnma%{?_isa} >= %{libnma_version}
Epoch: %{epoch}

%description -n nm-connection-editor
This package contains a network configuration editor and Bluetooth modem
utility for use with NetworkManager.


%package -n nm-connection-editor-desktop
Summary: The desktop file for nm-connection-editor
Requires: nm-connection-editor%{?_isa} = %{epoch}:%{version}-%{release}
Epoch: %{epoch}

%description -n nm-connection-editor-desktop
This package contains the desktop file and appdata for nm-connection-editor.
Without it, the nm-connection-editor cannot be started from the desktop
environment.


%prep
%autosetup -p1 -n "%{name}-%{real_version}"

%build
%meson \
    -Dselinux=true \
%if %{with appindicator}
    -Dappindicator=yes
%else
    -Dappindicator=no
%endif
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-vpn-properties

%find_lang nm-applet
cat nm-applet.lang >> %{name}.lang

# validate .desktop and autostart files
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/nm-applet.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/nm-connection-editor.desktop

%check
%meson_test


%files
%{_bindir}/nm-applet
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/icons/hicolor/22x22/apps/nm-adhoc.png
%{_datadir}/icons/hicolor/22x22/apps/nm-mb-roam.png
%{_datadir}/icons/hicolor/22x22/apps/nm-secure-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-signal-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-stage*-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-tech-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-active-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-wwan-tower.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/22x22/apps/nm-insecure-warn.png
%{_datadir}/GConf/gsettings/nm-applet.convert
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%{_mandir}/man1/nm-applet*
%doc NEWS CONTRIBUTING
%license COPYING

# Yes, lang files for the applet go in nm-connection-editor RPM since it
# is the RPM that everything else depends on
%files -n nm-connection-editor -f %{name}.lang
%{_bindir}/nm-connection-editor
%{_datadir}/icons/hicolor/*/apps/nm-device-*.*
%{_datadir}/icons/hicolor/*/apps/nm-no-connection.*
%{_datadir}/icons/hicolor/16x16/apps/nm-vpn-standalone-lock.png
%{_mandir}/man1/nm-connection-editor*
%dir %{_datadir}/gnome-vpn-properties


%files -n nm-connection-editor-desktop
%{_datadir}/applications/nm-connection-editor.desktop
%{_datadir}/metainfo/nm-connection-editor.appdata.xml


%changelog
