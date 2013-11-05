
%global commit 40809aed657502e9de158e2cfe2c659a316f2f90
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           bitcoin
Version:        0.8.3
Release:        1%{?dist}
Summary:        Bitcoin is an experimental new digital currency

License:        MIT
URL:            http://bitcoin.org/
Source0:        https://github.com/bitcoin/bitcoin/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  qt-devel gcc-c++ boost-devel openssl-freeworld-devel libdb-cxx-devel desktop-file-utils
#Requires:       

%description
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network. Bitcoin
is also the name of the open source software which enables the use of
this currency.

%prep
%setup -qn %{name}-%{commit}

%build
/usr/lib64/qt4/bin/qmake "USE_UPNP=-"
make %{?_smp_mflags} SUBLIBS="-L/usr/lib64/openssl-freeworld"

%install
install -D bitcoin-qt %{buildroot}%{_bindir}/bitcoin-qt
install -D share/pixmaps/bitcoin128.png %{buildroot}%{_datadir}/pixmaps/bitcoin128.png
desktop-file-install                        \
--dir=%{buildroot}%{_datadir}/applications  \
contrib/debian/bitcoin-qt.desktop

%files
%doc COPYING README.md doc/assets-attribution.txt doc/files.txt doc/release-notes.md doc/Tor.txt 
%{_bindir}/bitcoin-qt
%{_datadir}/pixmaps/bitcoin128.png
%{_datadir}/applications/bitcoin-qt.desktop

%changelog
* Mon Jul 15 2013 Jeff Mendoza <jeffmendoza@live.com> - 0.8.3-1
- Initial revision
