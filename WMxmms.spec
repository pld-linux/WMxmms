Summary:	An XMMS interface for WindowMaker
Summary(pl.UTF-8):   Interfejs XMMS dla WindowMakera
Name:		WMxmms
Version:	0.1.4
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dockapps.org/download.php/id/252/%{name}-%{version}.tar.gz
# Source0-md5:	b7fc2b01340f267b7f29b608d3f63a98
URL:		http://dockapps.org/file.php/id/172/
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An XMMS interface for WindowMaker.

%description -l pl.UTF-8
Interfejs XMMS dla WindowMakera.

%prep
%setup -q

%build
%configure
%{__make} \
	LDFLAGS="%{rpmldflags} `xmms-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
