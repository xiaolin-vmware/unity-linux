Name:       libxrender
Version:    0.9.9
Release:    1%{?dist}
Summary:    X.Org Rendering Extension client library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.bz2

BuildRequires: xproto libx11-devel libsm-devel
BuildRequires: libice-devel e2fsprogs-devel

%description
%{name} is a library for the Render Extension to the X11 protocol.

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for libXrender. If you like to develop programs using libXrender, you will need
to install libXrender-devel. 

%prep
%setup -q -n libXrender-%{version}

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libXrender.so.*
%{_libdir}/libXrender.so.*.*.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXrender.so
%{_libdir}/libXrender.a

%changelog
