Summary:	GSM audio encoding/decoding library
Summary(pl):	Biblioteka koduj±ca/dekoduj±ca d¼wiêk GSM
Name:		libgsm
Version:	1.0.10
Release:	5
License:	Free/Copyright Technische Universitaet Berlin
Vendor:		Tycho Softworks
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/gsm-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a free and public implementation of GSM audio encoding and
decoding. The gsm library is used in many free software projects
including 'rplay', but has never been packaged as a stand-alone shared
library. GSM encoding has specific uses in transmission of packetized
audio over the Internet.

%description -l pl
To jest darmowa implementacja kodowania i dekodowania d¼wiêku GSM.
Biblioteka jest u¿ywana w wielu projektach, m.in. rplay. Kodowanie GSM
ma specyficzne zastosowani przy transmisji pakietowanego d¼wiêku przez
Internet.

%package devel
Summary:	Header files and development documentation for libgsm
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libgsm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libgsm.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libgsm.

%package static
Summary:	GSM Audio Encoding/decoding static library
Summary(pl):	Statyczna biblioteka GSM Audio
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
GSM Audio Encoding/decoding static library.

%description static -l pl
Statyczna biblioteka GSM Audio.

%prep
%setup -q -n gsm-1.0-pl10
%patch0 -p1

%build
%{__make} OPTFLAGS="%{rpmcflags}" WAV49="-DWAV49"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir},%{_libdir}}

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

echo .so toast.1 >$RPM_BUILD_ROOT%{_mandir}/man1/tcat.1
echo .so toast.1 >$RPM_BUILD_ROOT%{_mandir}/man1/untoast.1

gzip -9nf COPYRIGHT ChangeLog MACHINES MANIFEST README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgsm.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsm.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsm.a
