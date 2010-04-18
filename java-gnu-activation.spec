%include	/usr/lib/rpm/macros.java
Summary:	GNU JavaBeans(TM) Activation Framework (JAF)
Summary(pl.UTF-8):	Środowisko aktywacyjne JavaBeans(TM) (JAF) w wersji GNU
Name:		java-gnu-activation
Version:	1.1.1
Release:	7
License:	LGPL
Group:		Libraries/Java
Source0:	http://ftp.gnu.org/gnu/classpathx/activation-%{version}.tar.gz
# Source0-md5:	de50d7728e8140eb404f2b4554321f8c
Patch0:		%{name}-MimeType-symbols-fix.patch
URL:		http://www.gnu.org/software/classpathx/jaf/jaf.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Provides:	java(jaf) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU JAF is a framework for declaring what beans operate on what MIME
type data. Content handler beans can be defined to handle particular
MIME content. The JAF unites Internet standards for declaring content
with JavaBeans(TM).

%description -l pl.UTF-8
GNU JAF to szkielet służący do deklarowania, na jakim typie danych
mają operować beans. Procedura obsługi beans może być zdefiniowana do
operowania na konkretnej zawartości MIME. JAF jednoczy standardy
internetowe do deklarowania zawartości przy użyciu JavaBeans(TM).

%package javadoc
Summary:	API documentation for GNU JAF
Summary(pl.UTF-8):	Dokumentacja API GNU JAF
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	java-gnu-activation-doc

%description javadoc
API documentation for GNU JavaBeans(TM) Activation Framework.

%description javadoc -l pl.UTF-8
Dokumentacja API GNU JavaBeans(TM) Activation Framework.

%prep
%setup -q -n activation-%{version}
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
unset CLASSPATH || :
export JAVAC=%{javac}
%configure

%{__make}

export SHELL=/bin/sh
%{__make} javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_javadir}/{activation.jar,gnu-activation-%{version}.jar}
ln -s gnu-activation-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/activation.jar
ln -s gnu-activation-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jaf-1.1.jar
ln -s gnu-activation-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jaf.jar

cp -a docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog source/javax/activation/*.html
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
