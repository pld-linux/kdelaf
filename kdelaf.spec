#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	KDE Look and Feel for Java
Name:		kdelaf
Version:	060417
Release:	1
License:	GPL
Group:		Applications
Source0:	http://kdelaf.freeasinspeech.org/dl.php?file=%{name}.tgz
# Source0-md5:	da70a1c4bf7b9889a397dc98694b1de5
Source1:	http://kdelaf.freeasinspeech.org/dl.php?file=%{name}worker.tgz
# Source1-md5:	2fc3e398891158bb136c6e26c3c70b62
URL:		http://kdelaf.freeasinspeech.org
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         javadir         %{_libdir}/java
%define         _noautoreqdep   libjava.so libjvm.so

%description
KDE Look and Feel for Java

%prep
%setup -q -c -T -a0 -a1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
cd kdelafworker
cp -f /usr/share/automake/config.sub .
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/jre/lib/ext

cd kdelafworker
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd -
cp *.jar $RPM_BUILD_ROOT%{_javadir}/jre/lib/ext

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/jre/lib/ext/*
%attr(755,root,root) %{_bindir}/*
