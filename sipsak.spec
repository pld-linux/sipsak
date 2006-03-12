Summary:	small comand line tool for developers and administrators of SIP applications
Name:		sipsak
Version:	0.9.6
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://download.berlios.de/sipsak/%{name}-%{version}-1.tar.gz
# Source0-md5:	c4eb8e282902e75f4f040f09ea9d99d5
URL:		http://sipsak.org/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sipsak is a command line tool for performing various tests on Session Initiation Protocol (SIP) applications and devices. It can make several different tests, send the contents of a file, and interpret and react on the responses. It supports (de-) registration with given contact URIs and digest authentication.
%prep
%setup -q

%build
%configure \
	--disable-gnutls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sipsak
%{_mandir}/man1/*
%doc ChangeLog README TODO NEWS
