Summary:	GSM audio encoding/decoding library
Summary(pl.UTF-8):	Biblioteka kodująca/dekodująca dźwięk GSM
Summary(pt_BR.UTF-8):	Biblioteca de codificação/decodificação de áudio GSM
Summary(ru.UTF-8):	Библиотека аудио кодирования/декодирования GSM
Summary(uk.UTF-8):	Бібліотека аудіо кодування/декодування GSM
Name:		libgsm
%define	sver	22
Version:	1.0.%{sver}
Release:	1
License:	Free (Copyright (C) Technische Universitaet Berlin)
Group:		Libraries
Source0:	https://www.quut.com/gsm/gsm-%{version}.tar.gz
# Source0-md5:	fcca74c770a341d78ea4604418c1264b
Patch0:		%{name}-makefile.patch
URL:		https://www.quut.com/gsm/
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

%description -l pl.UTF-8
To jest darmowa implementacja kodowania i dekodowania dźwięku GSM.
Biblioteka jest używana w wielu projektach, m.in. rplay. Kodowanie GSM
ma specyficzne zastosowani przy transmisji pakietowanego dźwięku przez
Internet.

GSM 06.10 dokonuje kompresji ramek 160 13-bitowych sampli (o
ośmiokilohercowej częstotliwości próbkowania, czyli częstotliwości
ramki 50 Hz) do 260 bitów; aby zachować kompatybilność z typowymi
aplikacjami uniksowymi, nasza implementacja zamienia ramki 160
16-bitowych linearnych sampli w 33-bajtowe ramki (1650 bajtów/s).
Algorytm jest na tyle dobry, że można go wykorzystać do przekazywania
mowy. Nawet muzyka często pomyślnie przechodzi proces kodowania
(wziąwszy pod uwagę ograniczenia przepustowości osmiokilohercowej
częstotliwości próbkowania).

%description -l pt_BR.UTF-8
Esta é uma implementação pública e livre da codificação GSM. A
biblioteca gsm é usada por muitos programas de livre distribuição,
entre eles o rplay.

%description -l ru.UTF-8
Это свободная реализация аудио кодирования/декодирования GSM.
Кодирование GSM используется при передаче аудио через Интернет.

%description -l uk.UTF-8
Це вільна реалізація аудіо кодування/декодування GSM. Кодування GSM
використовується при передачі аудіо через Інтернет.

%package devel
Summary:	Header files and development documentation for libgsm
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libgsm
Summary(pt_BR.UTF-8):	Biblioteca de codificação/decodificação de áudio GSM - arquivos para desenvolvimento
Summary(ru.UTF-8):	Файлы для разработки с использованием библиотеки libgsm
Summary(uk.UTF-8):	Файли для розробки з використанням бібліотеки libgsm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libgsm.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libgsm.

%description devel -l pt_BR.UTF-8
Biblioteca de codificação/decodificação de áudio GSM - arquivos para
desenvolvimento

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ с
использованием библиотеки libgsm.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм з
використанням бібліотеки libgsm.

%package static
Summary:	GSM Audio Encoding/decoding static library
Summary(pl.UTF-8):	Statyczna biblioteka GSM Audio
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com a libgsm
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием libgsm
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням libgsm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GSM Audio Encoding/decoding static library.

%description static -l pl.UTF-8
Statyczna biblioteka GSM Audio.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libgsm

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ.

%description static -l uk.UTF-8
Цей пакет містить статичні бібіліотеки для розробки програм.

%prep
%setup -q -n gsm-1.0-pl%{sver}
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc} -ansi -pedantic" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}" \
	OPTFLAGS="%{rpmcflags} %{rpmcppflags}" \
	WAV49="-DWAV49"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir},%{_libdir}}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	GSM_INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}

echo .so toast.1 >$RPM_BUILD_ROOT%{_mandir}/man1/tcat.1
echo .so toast.1 >$RPM_BUILD_ROOT%{_mandir}/man1/untoast.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog MACHINES README
%attr(755,root,root) %{_bindir}/tcat
%attr(755,root,root) %{_bindir}/toast
%attr(755,root,root) %{_bindir}/untoast
%attr(755,root,root) %{_libdir}/libgsm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsm.so.1
%{_mandir}/man1/tcat.1*
%{_mandir}/man1/toast.1*
%{_mandir}/man1/untoast.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsm.so
%{_includedir}/gsm.h
%{_mandir}/man3/gsm*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsm.a
