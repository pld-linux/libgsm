Summary:	GSM audio encoding/decoding library
Name:		libgsm
Version:	1.0.10
Release:	1
Source0:	ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/gsm-%{version}.tar.gz
Patch0:		gsm-1.0.9-makefile.patch
Group:		Libraries
Copyright:	Free/Copyright Technische Universitaet Berlin
Vendor:		Tycho Softworks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a free and public implimentation of GSM audio encoding and
decoding. The gsm library is used in many free software projects
including 'rplay', but has never been packaged as a stand-alone shared
libary. GSM encoding has specific uses in transmission of packetized
audio over the Internet.

%prep
%setup -q -n gsm-1.0-pl10
%patch -p1

%build
%{__make} RPM_OPT_FLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_prefix}/{bin,man/man{1,3},include,lib}
%{__make} INSTALL_ROOT=${RPM_BUILD_ROOT}%{_prefix} install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog INSTALL MACHINES MANIFEST README
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/toast
%attr(755,root,root) %{_bindir}/untoast
%attr(755,root,root) %{_bindir}/tcat
%{_prefix}/man/man3/*
%{_includedir}/gsm.h
%{_libdir}/libgsm*

%clean
rm -rf ${RPM_BUILD_ROOT}
