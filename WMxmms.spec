Summary:	An xmms interface for WM
Summary(pl):	Interfejs xmms dla WM
Name:		WMxmms
Version:	0.1.4
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dockapps.org/download.php/id/252/%{name}-%{version}.tar.gz
# Source0-md5:	b7fc2b01340f267b7f29b608d3f63a98
URL:		http://dockapps.org/file.php/id/172/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
An xmms interface for WM

%description -l pl
Interfejs xmms dla WM

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -pipe -Wall -pedantic `pkg-config --cflags gdk-pixbuf-xlib-2.0`" \
	USE_GDKPIXBUF2="1" \
	USE_GDKPIXBUF="0"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/%{name} $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
