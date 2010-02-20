
Name:		gwibber
Version:	2.29.90.1
Release:	%mkrel 1
Summary:	An open source microblogging client for GNOME developed with Python and GTK
Group:		Networking/Other
License:	GPLv2+
URL:		https://launchpad.net/gwibber
Source0:	http://launchpad.net/gwibber/trunk/%{version}/+download/gwibber-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	python-mako
Requires:	dbus-python gnome-python-gconf python-pyxml
Requires:	python-webkitgtk python-feedparser pyxdg python-imaging
Requires:	python-egenix-mx-base
Requires:	python-sexy python-simplejson >= 1.9.1 gnome-python-desktop
Requires:	desktopcouch
BuildRequires:	python-devel desktop-file-utils intltool gettext python-distutils-extra
BuildArch:	noarch

%description
Gwibber is an open source microblogging client for GNOME developed with Python
and GTK. It supports Twitter, Jaiku, Identi.ca, Facebook, and Digg.


%prep
%setup -q
sed -i -e '/^#! \?\//, 1d' $(find %{name} | grep "\.py$")

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --prefix %{_prefix} --skip-build --root %{buildroot}

## Reinstall .desktop file
#rm -rf %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications build/share/applications/%{name}.desktop

## Install i18n data  (THIS MUST COME LAST)
cp -a build/mo %{buildroot}%{_datadir}/locale
%find_lang %{name}

 
%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS README
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/*
%{_datadir}/indicators/messages/applications/%{name}
