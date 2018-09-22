%define	snap	20170713
%define	rel	1
Summary:	Small comand line tool for developers and administrators of SIP applications
Summary(pl.UTF-8):	Małe narzędzie linii poleceń dla programistów i administratorów aplikacji SIP
Name:		sipsak
Version:	0.9.6
Release:	4.%{snap}.%{rel}
License:	GPL
Group:		Networking/Utilities
# https://github.com/nils-ohlmeier/sipsak
Source0:	http://ftp.debian.org:/debian/pool/main/s/sipsak/%{name}_%{version}+git%{snap}.orig.tar.gz
# Source0-md5:	a7f0f8ca2076939cd9ceba2ce1a80889
URL:		http://sipsak.org/
BuildRequires:	c-ares-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sipsak is a command line tool for performing various tests on Session
Initiation Protocol (SIP) applications and devices. It can make
several different tests, send the contents of a file, and interpret
and react on the responses. It supports (de-) registration with given
contact URIs and digest authentication.

%description -l pl.UTF-8
sipsak to działające z linii poleceń narzędzie do wykonywania różnych
testów na aplikacjach i urządzeniach korzystających z protokołu SIP
(Session Initiation Protocol - protokołu nawiązywania sesji). Potrafi
wykonywać kilka różnych testów, wysyłać zawartość plików,
interpretować i reagować na odpowiedzi. Obsługuje (de-)rejestrowanie z
podanym URI kontaktowym i uwierzytelnianie digest.

%prep
%setup -q -n %{name}
sed -i -e 's#gnutls#no-gnutls#g' configure.ac

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
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
%doc ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/sipsak
%{_mandir}/man1/*
