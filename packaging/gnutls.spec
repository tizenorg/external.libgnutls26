#sbs-git:slp/pkgs/l/libgnutls26 gnutls 2.12.0 334e00aa49812702098c8de319a48e4a1bac6f02
Summary: A TLS protocol implementation
Name: gnutls
Version: 2.12.0
Release: 1
License: LGPLv2+
Group: System/Libraries
BuildRequires: libgcrypt-devel >= 1.2.2, gettext-tools
BuildRequires: zlib-devel, readline-devel, libtasn1-devel
BuildRequires: lzo-devel, libtool, automake, autoconf
URL: http://www.gnutls.org/
Source0: %{name}-%{version}.tar.gz
Source1001: packaging/gnutls.manifest 

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libgcrypt >= 1.2.2

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libgcrypt-devel
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
cp %{SOURCE1001} .

rm -f doc/*.info* lib/po/libgnutls26.pot
if [ -e doc/gnutls.pdf.debbackup ] && [ ! -e doc/gnutls.pdf ] ; then
	mv doc/gnutls.pdf.debbackup doc/gnutls.pdf ;
fi

%configure  --enable-ld-version-script --disable-cxx --without-lzo \
            --cache-file=config.cache --with-libgcrypt \
            --with-included-libtasn1
make

%install
rm -fr $RPM_BUILD_ROOT
%make_install



%remove_docs

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest gnutls.manifest
%{_libdir}/libgnutls*.so.*
%{_prefix}/share/locale/*/LC_MESSAGES/libgnutls26.mo

%files devel
%manifest gnutls.manifest
%{_includedir}/*
%{_libdir}/libgnutls*.so
%{_libdir}/pkgconfig/*.pc
