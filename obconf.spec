# TODO:
# - .desktop
# - should be accessable from GNOME control center (maybe)
# - check BR
Summary:	Tool for configuring the Openbox window manager
Summary(pl):	Narz�dzie do konfiguracji zarz�dcy okien Openbox
Name:		obconf
Version:	1.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://icculus.org/openbox/releases/%{name}-%{version}.tar.gz
# Source0-md5:	6ac86be513ae9c12b536b9a0de853c43
URL:		http://icculus.org/openbox/obconf.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint >= 0.12.1
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	openbox-devel >= 3.0-0.beta3.1
BuildRequires:	XFree86-devel
BuildRequires:	xft-devel >= 2.0
Requires:	openbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%description -l pl
ObConf pozwala na konfiguracj� Openboxa w czasie rzeczywistym. Mo�na
nim zmienia� opcje jak motyw, nazwy pulpit�w i ustawienia zachowania
okien.

%prep
%setup -q

%build
rm -f missing
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/obconf.glade