Summary: GSM audio encoding/decoding library
Name: libgsm
Version: 1.0.10
Release: 1
Source: ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/gsm-%{version}.tar.gz
Patch: gsm-1.0.9-makefile.patch
Group: Librarites
Copyright: Free/Copyright Technische Universitaet Berlin
Vendor: Tycho Softworks
Packager: David Sugar <dyfet@tycho.com>
BuildRoot: /tmp/%{name}-root

%description
This is a free and public implimentation of GSM audio encoding
and decoding.  The gsm library is used in many free software projects
including 'rplay', but has never been packaged as a stand-alone
shared libary.  GSM encoding has specific uses in transmission of
packetized audio over the Internet.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n gsm-1.0-pl10

%patch -p1

%build
make RPM_OPT_FLAGS="${RPM_OPT_FLAGS}"

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/{bin,man/man{1,3},include,lib}
make INSTALL_ROOT=${RPM_BUILD_ROOT}/usr install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc COPYRIGHT ChangeLog INSTALL MACHINES MANIFEST README
%defattr(-,root,root)
/usr/bin/toast
/usr/bin/untoast
/usr/bin/tcat
/usr/man/man3/*
/usr/include/gsm.h
/usr/lib/libgsm*

%clean
rm -rf ${RPM_BUILD_ROOT}
