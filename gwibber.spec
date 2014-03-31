%define __noautoreq 'typelib\\(Unity\\)|typelib\\(MessagingMenu\\)'

%define major 3
%define libname %mklibname %{name} %{major}
%define girmajor 0.3
%define girname %mklibname %{name}-gir %{girmajor}
%define develname %mklibname %{name} -d

Name:		gwibber
Version:	3.6.0
Release:	2
Summary:	An open source microblogging client for GNOME developed with Python and GTK
Group:		Networking/Other
License:	GPLv2+
URL:		https://launchpad.net/gwibber
Source0:	http://launchpad.net/gwibber/3.6/%{version}/+download/gwibber-%{version}.tar.gz
Source1:	https://launchpad.net/gwibber-service-sina/trunk/0.9.1/+download/gwibber-service-sina-0.9.1.tar.gz
Patch0:		gwibber-3.6.0-drop-gtk2.patch
Patch1:		gwibber-3.6.0-desktop-file.patch
BuildRequires:	pkgconfig(dee-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gdk-3.0) >= 3.2
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.26
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.26
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.2
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libaccounts-glib)
BuildRequires:	pkgconfig(libnotify) >= 0.7
BuildRequires:	pkgconfig(libsignon-glib)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.10
BuildRequires:	intltool >= 0.35.0
BuildRequires:	vala >= 0.15
BuildRequires:	python-devel >= 2.6
BuildRequires:	gettext-devel
BuildRequires:	python-distribute
BuildRequires:	python-distutils-extra
Requires: python-sqlite2
Requires: python-dbus
Requires: python-simplejson
Requires: python-oauth
Requires: python-imaging
Requires: python-httplib2
Requires: typelib(GnomeKeyring)
Requires: typelib(Accounts)
Requires: typelib(Signon)

%description
Gwibber is an open source microblogging client for GNOME developed with Python
and GTK. It supports Twitter, Jaiku, Identi.ca, Facebook, and Digg.

%package -n %{libname}
Summary: Gwibber - shared library
Group: Networking/Other

%description -n %{libname}
Gwibber - shared library.

%package -n %{girname}
Summary: GObject Introspection interface description for Gwibber
Group: Networking/Other
Requires: %{libname} = %{EVRD}

%description -n %{girname}
GObject Introspection interface description for Gwibber.

%package -n %{develname}
Summary: Development files for Gwibber
Group: Networking/Other
Requires: %{libname} = %{EVRD}

%description -n %{develname}
Development files for Gwibber.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

find libgwibber-gtk -name *.c -delete

%build
%configure2_5x --disable-spell --disable-unity --disable-schemas-compile
# No parallel make
make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.a

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/%{name}
%{_libexecdir}/entry-c
%{_libexecdir}/entry-vala
%{_datadir}/applications/*.desktop
%{_datadir}/accounts/applications/gwibber.application
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/indicators/messages/applications/gwibber.indicator
%{py_puresitedir}/*
%{_datadir}/GConf/gsettings/*.convert
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gwibber*-%{girmajor}.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps
