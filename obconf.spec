Summary:	Tool for configuring the Openbox window manager
Summary(pl):	Narzêdzie do konfiguracji zarz±dcy okien Openbox
Name:		obconf
Version:	1.5
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://openbox.org/obconf/%{name}-%{version}.tar.gz
# Source0-md5:	a0f0e14db3d889bd67f98f1c00b4a9f7
Patch0:		%{name}-desktop.patch
URL:		http://openbox.org/obconf/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-autopoint >= 0.12.1
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	openbox-devel >= 1:3.0-0.rc1.1
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
Requires:	openbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%description -l pl
ObConf pozwala na konfiguracjê Openboksa w czasie rzeczywistym. Mo¿na
nim zmieniaæ opcje jak motyw, nazwy pulpitów i ustawienia zachowania
okien.

%prep
%setup -q
%patch0 -p1

%build
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
%{_desktopdir}/obconf.desktop
