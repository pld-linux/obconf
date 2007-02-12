Summary:	Tool for configuring the Openbox window manager
Summary(pl.UTF-8):   Narzędzie do konfiguracji zarządcy okien Openbox
Name:		obconf
Version:	1.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://tr.openmonkey.com/files/obconf/%{name}-%{version}.tar.gz
# Source0-md5:	aaf62498b11d52dfce7a0b6060867a19
Patch0:		%{name}-desktop.patch
URL:		http://openbox.org/obconf/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-autopoint >= 0.12.1
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	openbox-devel >= 1:3.0-0.rc1.1
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%description -l pl.UTF-8
ObConf pozwala na konfigurację Openboksa w czasie rzeczywistym. Można
nim zmieniać opcje jak motyw, nazwy pulpitów i ustawienia zachowania
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
