Summary:	GSM audio encoding/decoding library
Summary(pl):	Biblioteka koduj�ca/dekoduj�ca d�wi�k GSM
Summary(pt_BR):	Biblioteca de codifica��o/decodifica��o de �udio GSM
Summary(ru):	���������� ����� �����������/������������� GSM
Summary(uk):	��̦����� ��Ħ� ���������/����������� GSM
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
To jest darmowa implementacja kodowania i dekodowania d�wi�ku GSM.
Biblioteka jest u�ywana w wielu projektach, m.in. rplay. Kodowanie GSM
ma specyficzne zastosowani przy transmisji pakietowanego d�wi�ku przez
Internet.

GSM 06.10 dokonuje kompresji ramek 160 13-bitowych sampli (o
o�miokilohercowej cz�stotliwo�ci pr�bkowania, czyli cz�stotliwo�ci
ramki 50 Hz) do 260 bit�w; aby zachowa� kompatybilno�� z typowymi
aplikacjami uniksowymi, nasza implementacja zamienia ramki 160
16-bitowych linearnych sampli w 33-bajtowe ramki (1650 bajt�w/s).
Algorytm jest na tyle dobry, �e mo�na go wykorzysta� do przekazywania
mowy. Nawet muzyka cz�sto pomy�lnie przechodzi proces kodowania
(wzi�wszy pod uwag� ograniczenia przepustowo�ci osmiokilohercowej
cz�stotliwo�ci pr�bkowania).

%description -l pt_BR
Esta � uma implementa��o p�blica e livre da codifica��o GSM. A
biblioteca gsm � usada por muitos programas de livre distribui��o,
entre eles o rplay.

%description -l ru
��� ��������� ���������� ����� �����������/������������� GSM.
����������� GSM ������������ ��� �������� ����� ����� ��������.

%description -l uk
�� צ���� ���̦��æ� ��Ħ� ���������/����������� GSM. ��������� GSM
����������դ���� ��� ������ަ ��Ħ� ����� ��������.

%package devel
Summary:	Header files and development documentation for libgsm
Summary(pl):	Pliki nag��wkowe i dokumentacja do libgsm
Summary(pt_BR):	Biblioteca de codifica��o/decodifica��o de �udio GSM - arquivos para desenvolvimento
Summary(ru):	����� ��� ���������� � �������������� ���������� libgsm
Summary(uk):	����� ��� �������� � ������������� ¦�̦����� libgsm
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libgsm.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libgsm.

%description devel -l pt_BR
Biblioteca de codifica��o/decodifica��o de �udio GSM - arquivos para
desenvolvimento

%description devel -l ru
���� ����� �������� �����, ����������� ��� ���������� �������� �
�������������� ���������� libgsm.

%description devel -l uk
��� ����� ͦ����� �����, ����Ȧ�Φ ��� �������� ������� �
������������� ¦�̦����� libgsm.

%package static
Summary:	GSM Audio Encoding/decoding static library
Summary(pl):	Statyczna biblioteka GSM Audio
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a libgsm
Summary(ru):	����������� ���������� ��� ���������� � �������������� libgsm
Summary(uk):	������Φ ¦�̦����� ��� �������� � ������������� libgsm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GSM Audio Encoding/decoding static library.

%description static -l pl
Statyczna biblioteka GSM Audio.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libgsm

%description static -l ru
���� ����� �������� ����������� ���������� ��� ���������� ��������.

%description static -l uk
��� ����� ͦ����� ������Φ ¦¦̦����� ��� �������� �������.

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
