Name:		gwibber
Version:	3.0.0.1
Release:	%mkrel 2
Summary:	An open source microblogging client for GNOME developed with Python and GTK
Group:		Networking/Other
License:	GPLv2+
URL:		https://launchpad.net/gwibber
Source0:	http://launchpad.net/gwibber/trunk/%{version}/+download//gwibber-%{version}.tar.gz
Source1:	http://ppa.launchpad.net/gwibber-team/ppa/ubuntu/pool/main/g/gwibber-service-sina/gwibber-service-sina_0.0.1+r12-2.tar.gz
Source2:	http://ppa.launchpad.net/gwibber-team/ppa/ubuntu/pool/main/g/gwibber-service-sohu/gwibber-service-sohu_0.0.1+r13-1.tar.gz
Requires:	python-mako
Requires:	dbus-python gnome-python-gconf python-pyxml python-curl
Requires:	python-webkitgtk python-feedparser pyxdg python-imaging
Requires:	python-egenix-mx-base
Requires:	python-sexy python-simplejson >= 1.9.1 gnome-python-desktop
Requires:	desktopcouch python-curl
BuildRequires:	python-devel desktop-file-utils intltool gettext python-distutils-extra
BuildArch:	noarch

%description
Gwibber is an open source microblogging client for GNOME developed with Python
and GTK. It supports Twitter, Jaiku, Identi.ca, Facebook, and Digg.


%prep
%setup -q -a1 -a2
sed -i -e '/^#! \?\//, 1d' $(find %{name} | grep "\.py$")

%build
%{__python} setup.py build

for i in gwibber-service-*
do
	pushd $i
	%{__python} setup.py build
	popd
done

%install
%{__python} setup.py install --prefix %{_prefix} --skip-build --root %{buildroot}

for i in gwibber-service-*
do
	pushd $i
	%{__python} setup.py install --prefix %{_prefix} --skip-build --root %{buildroot}
	popd
done

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
%{python_sitelib}/*.egg-info
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/*
%{_datadir}/indicators/messages/applications/%{name}
