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


%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 3.0.0.1-2mdv2011.0
+ Revision: 672397
- add sohu and sina plugin for ubuntu ppa

* Fri Apr 15 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.0.0.1-1
+ Revision: 653094
- update to 3.0.0.1 (which is not a gnome3 package, just the last stable release)

* Sun Nov 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.91.1-1mdv2011.0
+ Revision: 602462
- update to 2.91.1

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 2.32.2-1mdv2011.0
+ Revision: 598841
- new version 2.32.2

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

  + Sandro Cazzaniga <kharec@mandriva.org>
    - drop p0 (not applied since last release)

* Sun Sep 05 2010 Funda Wang <fwang@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 576042
- new version 2.31.91

* Mon Aug 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 572192
- new version 2.31.90
- don't use patch0 (seems be not applicable on this version, bbut keep it)

* Tue Aug 17 2010 Michael Scherer <misc@mandriva.org> 2.30.1-2mdv2011.0
+ Revision: 570935
- add a patch to gwibber to fix issues about KeyError: "_id"
- update to latest stable branch
- add missing Requires

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - python-curl is required

* Sun Apr 18 2010 Frederik Himpe <fhimpe@mandriva.org> 2.30.0.1-1mdv2010.1
+ Revision: 536443
- Update to new version 2.30.0.1

* Mon Apr 05 2010 Olivier Faurax <ofaurax@mandriva.org> 2.29.94-1mdv2010.1
+ Revision: 531482
- New version 2.29.94

* Sun Mar 28 2010 Olivier Faurax <ofaurax@mandriva.org> 2.29.92.1-2mdv2010.1
+ Revision: 528529
- Increment build number to bypass Build System dead submission in upload queue
- New version 2.29.92.1

* Sat Feb 20 2010 Frederik Himpe <fhimpe@mandriva.org> 2.29.90.1-1mdv2010.1
+ Revision: 508678
- Update to new version 2.29.90.1

* Sat Feb 13 2010 Frederik Himpe <fhimpe@mandriva.org> 2.29.1-2mdv2010.1
+ Revision: 505188
- Requires desktopcouch

* Wed Feb 10 2010 Michael Scherer <misc@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 503498
- new version of 2.29

* Sun Jul 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.0-0.r347mdv2010.0
+ Revision: 395327
- First Mandriva package based on Fedora's SPEC
- create gwibber

