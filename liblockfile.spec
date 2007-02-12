Summary:	NFS-safe locking library, includes dotlockfile program
Summary(pl.UTF-8):	Biblioteka blokowania plików uwzględniająca NFS wraz z programem dotlockfile
Name:		liblockfile
Version:	1.06.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/libl/liblockfile/%{name}_%{version}.tar.gz
# Source0-md5:	a6ab675558e50ea8d99648f707a121a0
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liblockfile is a shared library with NFS-safe locking functions. It
includes the command-line utility ``dotlockfile''.

%description -l pl.UTF-8
liblockfile to biblioteka współdzielona z funkcjami blokowania plików
bezpiecznymi także w przypadku używania NFS-a. Zawiera działający z
linii poleceń program dotlockfile.

%package devel
Summary:	Header files for liblockfile library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblockfle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is a development package for liblockfile. It includes headers and
documentation.

%description devel -l pl.UTF-8
To jest pakiet programistyczny dla liblockfile, zawiera pliki
nagłówkowe i dokumentację.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--enable-shared \
	--with-mailgroup

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir},%{_mandir}/man{1,3}}

%{__make} install \
	MAILGROUP=%(id -gn) \
	ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dotlockfile
%attr(755,root,root) %{_libdir}/liblockfile.so.*.*
%{_mandir}/man1/dotlockfile.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblockfile.so
%{_includedir}/lockfile.h
%{_includedir}/maillock.h
%{_mandir}/man3/lockfile_create.3*
%{_mandir}/man3/maillock.3*
