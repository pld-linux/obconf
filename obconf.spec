# TODO:
# - .desktop
# - should be accessable from GNOME control center (maybe)
# - check BR
#
Summary:	Tool for configuring the Openbox window manager
Summary(pl):	Narzêdzie do konfiguracji zarz±dcy okien Openbox
Name:		obconf
Version:	1.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://openbox.org/obconf/%{name}-%{version}.tar.gz
# Source0-md5:	dd57f5362218de1dcad48014a74982e6
URL:		http://openbox.org/obconf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint >= 0.12.1
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	openbox-devel >= 3.0-0.beta5.1
BuildRequires:	XFree86-devel
BuildRequires:	xft-devel >= 2.0
Requires:	openbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%description -l pl
ObConf pozwala na konfiguracjê Openboxa w czasie rzeczywistym. Mo¿na
nim zmieniaæ opcje jak motyw, nazwy pulpitów i ustawienia zachowania
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
