Name:		automake
Version:	1.15
Release:	1%{?dist}
Summary:	A GNU tool for automatically creating Makefiles	

Group:		Development/Tools
License:	GPLv2+ and GFDL and Public Domain and MIT
URL:		http://www.gnu.org/software/automake/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz	

#BuildRequires:	
#Requires:	

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%files
/usr/bin/automake-1.15
/usr/bin/automake
/usr/bin/aclocal
/usr/bin/aclocal-1.15
/usr/share/automake-1.15/depcomp
/usr/share/automake-1.15/tap-driver.sh
/usr/share/automake-1.15/mdate-sh
/usr/share/automake-1.15/compile
/usr/share/automake-1.15/COPYING
/usr/share/automake-1.15/config.sub
/usr/share/automake-1.15/ylwrap
/usr/share/automake-1.15/texinfo.tex
/usr/share/automake-1.15/config.guess
/usr/share/automake-1.15/install-sh
/usr/share/automake-1.15/py-compile
/usr/share/automake-1.15/INSTALL
/usr/share/automake-1.15/missing
/usr/share/automake-1.15/mkinstalldirs
/usr/share/automake-1.15/ar-lib
/usr/share/automake-1.15/test-driver
/usr/share/automake-1.15/Automake/Version.pm
/usr/share/automake-1.15/Automake/ItemDef.pm
/usr/share/automake-1.15/Automake/FileUtils.pm
/usr/share/automake-1.15/Automake/XFile.pm
/usr/share/automake-1.15/Automake/Config.pm
/usr/share/automake-1.15/Automake/ChannelDefs.pm
/usr/share/automake-1.15/Automake/RuleDef.pm
/usr/share/automake-1.15/Automake/DisjConditions.pm
/usr/share/automake-1.15/Automake/Item.pm
/usr/share/automake-1.15/Automake/Condition.pm
/usr/share/automake-1.15/Automake/Options.pm
/usr/share/automake-1.15/Automake/Channels.pm
/usr/share/automake-1.15/Automake/Configure_ac.pm
/usr/share/automake-1.15/Automake/General.pm
/usr/share/automake-1.15/Automake/Wrap.pm
/usr/share/automake-1.15/Automake/Getopt.pm
/usr/share/automake-1.15/Automake/Language.pm
/usr/share/automake-1.15/Automake/VarDef.pm
/usr/share/automake-1.15/Automake/Variable.pm
/usr/share/automake-1.15/Automake/Rule.pm
/usr/share/automake-1.15/Automake/Location.pm
/usr/share/automake-1.15/am/progs.am
/usr/share/automake-1.15/am/remake-hdr.am
/usr/share/automake-1.15/am/check2.am
/usr/share/automake-1.15/am/texinfos.am
/usr/share/automake-1.15/am/vala.am
/usr/share/automake-1.15/am/depend.am
/usr/share/automake-1.15/am/yacc.am
/usr/share/automake-1.15/am/lex.am
/usr/share/automake-1.15/am/data.am
/usr/share/automake-1.15/am/compile.am
/usr/share/automake-1.15/am/distdir.am
/usr/share/automake-1.15/am/libtool.am
/usr/share/automake-1.15/am/dejagnu.am
/usr/share/automake-1.15/am/texi-vers.am
/usr/share/automake-1.15/am/configure.am
/usr/share/automake-1.15/am/header-vars.am
/usr/share/automake-1.15/am/install.am
/usr/share/automake-1.15/am/header.am
/usr/share/automake-1.15/am/library.am
/usr/share/automake-1.15/am/texibuild.am
/usr/share/automake-1.15/am/scripts.am
/usr/share/automake-1.15/am/ltlib.am
/usr/share/automake-1.15/am/java.am
/usr/share/automake-1.15/am/inst-vars.am
/usr/share/automake-1.15/am/mans-vars.am
/usr/share/automake-1.15/am/libs.am
/usr/share/automake-1.15/am/mans.am
/usr/share/automake-1.15/am/program.am
/usr/share/automake-1.15/am/lisp.am
/usr/share/automake-1.15/am/lang-compile.am
/usr/share/automake-1.15/am/ltlibrary.am
/usr/share/automake-1.15/am/clean-hdr.am
/usr/share/automake-1.15/am/depend2.am
/usr/share/automake-1.15/am/check.am
/usr/share/automake-1.15/am/clean.am
/usr/share/automake-1.15/am/subdirs.am
/usr/share/automake-1.15/am/tags.am
/usr/share/automake-1.15/am/footer.am
/usr/share/automake-1.15/am/python.am
/usr/share/aclocal/README
/usr/share/aclocal-1.15/depend.m4
/usr/share/aclocal-1.15/obsolete.m4
/usr/share/aclocal-1.15/ar-lib.m4
/usr/share/aclocal-1.15/depout.m4
/usr/share/aclocal-1.15/auxdir.m4
/usr/share/aclocal-1.15/prog-cc-c-o.m4
/usr/share/aclocal-1.15/as.m4
/usr/share/aclocal-1.15/maintainer.m4
/usr/share/aclocal-1.15/options.m4
/usr/share/aclocal-1.15/mkdirp.m4
/usr/share/aclocal-1.15/lead-dot.m4
/usr/share/aclocal-1.15/gcj.m4
/usr/share/aclocal-1.15/dmalloc.m4
/usr/share/aclocal-1.15/amversion.m4
/usr/share/aclocal-1.15/init.m4
/usr/share/aclocal-1.15/vala.m4
/usr/share/aclocal-1.15/sanity.m4
/usr/share/aclocal-1.15/python.m4
/usr/share/aclocal-1.15/silent.m4
/usr/share/aclocal-1.15/lex.m4
/usr/share/aclocal-1.15/strip.m4
/usr/share/aclocal-1.15/install-sh.m4
/usr/share/aclocal-1.15/extra-recurs.m4
/usr/share/aclocal-1.15/substnot.m4
/usr/share/aclocal-1.15/lispdir.m4
/usr/share/aclocal-1.15/make.m4
/usr/share/aclocal-1.15/cond.m4
/usr/share/aclocal-1.15/upc.m4
/usr/share/aclocal-1.15/cond-if.m4
/usr/share/aclocal-1.15/runlog.m4
/usr/share/aclocal-1.15/tar.m4
/usr/share/aclocal-1.15/missing.m4
/usr/share/aclocal-1.15/internal/ac-config-macro-dirs.m4

%changelog