Summary: The GNU versions of find utilities (find and xargs)
Name: findutils
Version: 4.4.2
Release: 1%{?dist}
License: GPLv3+
Group: Applications/File
URL: http://www.gnu.org/software/findutils/
Source0: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

Patch1: fix-gnulib-freadahead.patch

Requires(post): texinfo
Requires(preun): texinfo
Provides: /bin/find

BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: texinfo

%description
The findutils package contains programs which will help you locate
files on your system.  The find utility searches through a hierarchy
of directories looking for files which match a certain set of criteria
(such as a file name pattern).  The xargs utility builds and executes
command lines from standard input arguments (usually lists of file
names generated by the find command).

You should install findutils because it includes tools that are very
useful for finding things on your system.

%prep
%setup -q
%patch1 -p1

%build
%configure

# uncomment to turn off optimizations
#find -name Makefile | xargs sed -i 's/-O2/-O0/'

make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%post
if [ -f %{_infodir}/find.info.gz ]; then
  /usr/bin/install-info %{_infodir}/find.info.gz %{_infodir}/dir || :
fi

%preun
if [ $1 = 0 ]; then
  if [ -f %{_infodir}/find.info.gz ]; then
    /usr/bin/install-info --delete %{_infodir}/find.info.gz %{_infodir}/dir || :
  fi
fi

%files 
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/find
%{_bindir}/oldfind
%{_bindir}/xargs
#%{_mandir}/man1/find.1*
#%{_mandir}/man1/oldfind.1*
#%{_mandir}/man1/xargs.1*
#%{_infodir}/find.info*
#%{_infodir}/find-maint.info.gz

%changelog