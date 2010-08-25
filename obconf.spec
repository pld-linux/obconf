# TODO:
# - update to 2.0.3 (temporary broken link)
Summary:	Tool for configuring the Openbox window manager
Summary(pl.UTF-8):	Narzędzie do konfiguracji zarządcy okien Openbox
Name:		obconf
Version:	2.0.3
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://icculus.org/openbox/obconf/%{name}-%{version}.tar.gz
# Source0-md5:	b22e273721851dedad72acbc77eefb68
Patch0:		%{name}-desktop.patch
URL:		http://openbox.org/obconf/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.15
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	openbox-devel >= 1:3.4.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%description -l pl.UTF-8
ObConf pozwala na konfigurację Openboksa w czasie rzeczywistym. Można
nim zmieniać opcje takie jak motyw, nazwy pulpitów i ustawienia
zachowania okien.

%prep
%setup -q
%patch0 -p1

%build
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

# no -> nb
mv $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/obconf
%{_datadir}/%{name}
%{_desktopdir}/obconf.desktop
%{_pixmapsdir}/obconf.png
%{_datadir}/mime/packages/obconf.xml

# FIXME: move these dirs to filesystem package (?)
# it's workaround to not require kdelibs
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/x-openbox-theme.desktop
