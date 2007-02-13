Summary:	KDE Look and Feel for Java
Summary(pl.UTF-8):	Wygląd i zachowanie KDE dla Javy
Name:		kdelaf
Version:	060417
Release:	1
License:	GPL
Group:		Applications
Source0:	http://kdelaf.freeasinspeech.org/dl.php?file=%{name}.tgz
# Source0-md5:	da70a1c4bf7b9889a397dc98694b1de5
Source1:	http://kdelaf.freeasinspeech.org/dl.php?file=%{name}worker.tgz
# Source1-md5:	2fc3e398891158bb136c6e26c3c70b62
URL:		http://kdelaf.freeasinspeech.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         javadir         %{_libdir}/java
%define         _noautoreqdep   libjava.so libjvm.so

%description
KDE Look and Feel for Java.

%description -l pl.UTF-8
Wygląd i zachowanie KDE dla Javy.


%prep
%setup -q -c -T -a0 -a1

%build
cd kdelafworker
cp -f /usr/share/automake/config.sub .
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/jre/lib/ext

%{__make} -C kdelafworker install \
	DESTDIR=$RPM_BUILD_ROOT
cp *.jar $RPM_BUILD_ROOT%{_javadir}/jre/lib/ext

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_javadir}/jre/lib/ext/*
