Summary:	GSM audio encoding/decoding library
Summary(pl):	Biblioteka koduj±ca/dekoduj±ca d¼wiêk GSM
Summary(pt_BR):	Biblioteca de codificação/decodificação de áudio GSM
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÁÕÄÉÏ ËÏÄÉÒÏ×ÁÎÉÑ/ÄÅËÏÄÉÒÏ×ÁÎÉÑ GSM
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ÁÕÄ¦Ï ËÏÄÕ×ÁÎÎÑ/ÄÅËÏÄÕ×ÁÎÎÑ GSM
Name:		libgsm
Version:	1.0.10
Release:	8
License:	Free (Copyright (C) Technische Universitaet Berlin)
Group:		Libraries
Source0:	ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/gsm-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://kbs.cs.tu-berlin.de/~jutta/toast.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a free and public implementation of GSM audio encoding and
decoding. The gsm library is used in many free software projects
including 'rplay', but has never been packaged as a stand-alone shared
library. GSM encoding has specific uses in transmission of packetized
audio over the Internet.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s). The quality
of the algorithm is good enough for reliable speaker recognition; even
music often survives transcoding in recognizable form (given the
bandwidth limitations of 8 kHz sampling rate).

%description -l pl
To jest darmowa implementacja kodowania i dekodowania d¼wiêku GSM.
Biblioteka jest u¿ywana w wielu projektach, m.in. rplay. Kodowanie GSM
ma specyficzne zastosowani przy transmisji pakietowanego d¼wiêku przez
Internet.

GSM 06.10 dokonuje kompresji ramek 160 13-bitowych sampli (o
o¶miokilohercowej czêstotliwo¶ci próbkowania, czyli czêstotliwo¶ci
ramki 50 Hz) do 260 bitów; aby zachowaæ kompatybilno¶æ z typowymi
aplikacjami uniksowymi, nasza implementacja zamienia ramki 160
16-bitowych linearnych sampli w 33-bajtowe ramki (1650 bajtów/s).
Algorytm jest na tyle dobry, ¿e mo¿na go wykorzystaæ do przekazywania
mowy. Nawet muzyka czêsto pomy¶lnie przechodzi proces kodowania
(wzi±wszy pod uwagê ograniczenia przepustowo¶ci osmiokilohercowej
czêstotliwo¶ci próbkowania).

%description -l pt_BR
Esta é uma implementação pública e livre da codificação GSM. A
biblioteca gsm é usada por muitos programas de livre distribuição,
entre eles o rplay.

%description -l ru
üÔÏ Ó×ÏÂÏÄÎÁÑ ÒÅÁÌÉÚÁÃÉÑ ÁÕÄÉÏ ËÏÄÉÒÏ×ÁÎÉÑ/ÄÅËÏÄÉÒÏ×ÁÎÉÑ GSM.
ëÏÄÉÒÏ×ÁÎÉÅ GSM ÉÓÐÏÌØÚÕÅÔÓÑ ÐÒÉ ÐÅÒÅÄÁÞÅ ÁÕÄÉÏ ÞÅÒÅÚ éÎÔÅÒÎÅÔ.

%description -l uk
ãÅ ×¦ÌØÎÁ ÒÅÁÌ¦ÚÁÃ¦Ñ ÁÕÄ¦Ï ËÏÄÕ×ÁÎÎÑ/ÄÅËÏÄÕ×ÁÎÎÑ GSM. ëÏÄÕ×ÁÎÎÑ GSM
×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÐÒÉ ÐÅÒÅÄÁÞ¦ ÁÕÄ¦Ï ÞÅÒÅÚ ¶ÎÔÅÒÎÅÔ.

%package devel
Summary:	Header files and development documentation for libgsm
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libgsm
Summary(pt_BR):	Biblioteca de codificação/decodificação de áudio GSM - arquivos para desenvolvimento
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ ÂÉÂÌÉÏÔÅËÉ libgsm
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ Â¦ÂÌ¦ÏÔÅËÉ libgsm
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libgsm.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libgsm.

%description devel -l pt_BR
Biblioteca de codificação/decodificação de áudio GSM - arquivos para
desenvolvimento

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ ÂÉÂÌÉÏÔÅËÉ libgsm.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú
×ÉËÏÒÉÓÔÁÎÎÑÍ Â¦ÂÌ¦ÏÔÅËÉ libgsm.

%package static
Summary:	GSM Audio Encoding/decoding static library
Summary(pl):	Statyczna biblioteka GSM Audio
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com a libgsm
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ libgsm
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ libgsm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GSM Audio Encoding/decoding static library.

%description static -l pl
Statyczna biblioteka GSM Audio.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libgsm

%description static -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦Â¦Ì¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ.

%prep
%setup -q -n gsm-1.0-pl10
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} -ansi -pedantic" \
	OPTFLAGS="%{rpmcflags}" WAV49="-DWAV49"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir},%{_libdir}}

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

echo .so toast.1 >$RPM_BUILD_ROOT%{_mandir}/man1/tcat.1
echo .so toast.1 >$RPM_BUILD_ROOT%{_mandir}/man1/untoast.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog MACHINES README
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
