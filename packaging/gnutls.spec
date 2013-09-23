Summary: A TLS protocol implementation
Name: gnutls
Version: 2.12.20_1
Release: 1
License: LGPLv2.1
Group: System/Libraries
BuildRequires: gettext-tools
BuildRequires: zlib-devel, readline-devel, libtasn1-devel
BuildRequires: lzo-devel, libtool, automake, autoconf
BuildRequires: nettle-devel, gmp-devel
URL: http://www.gnutls.org/
Source0: %{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: nettle, gmp

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: nettle-devel, gmp-devel
Requires: pkgconfig
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
GnuTLS is a project that aims to develop a library which provides a secure 
layer, over a reliable transport layer. Currently the GnuTLS library implements
the proposed standards by the IETF's TLS working group.

%description devel
GnuTLS is a project that aims to develop a library which provides a secure
layer, over a reliable transport layer. Currently the GnuTLS library implements
the proposed standards by the IETF's TLS working group.
This package contains files needed for developing applications with
the GnuTLS library.

%prep
%setup -q

%build

rm -f doc/*.info* lib/po/libgnutls26.pot

%configure  --enable-ld-version-script --disable-cxx --without-lzo --with-included-libtasn1 --without-p11-kit
make

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}

%make_install

%remove_docs

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/share/license/%{name}
%manifest libgnutls26.manifest
%{_libdir}/libgnutls*.so.*
%{_prefix}/share/locale/*/LC_MESSAGES/libgnutls.mo

%files devel
%{_includedir}/*
%{_libdir}/libgnutls*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Sep 23 2013 Keunsoon Lee <keunsoon.lee@samsung.com>
- [Release] Update changelog for gnutls-2.12.20_1
