Summary:	GNU JavaBeans(TM) Activation Framework (JAF)
Summary(pl):	¦rodowisko aktywacyjne JavaBeans(TM) (JAF) w wersji GNU
Name:		java-gnu-activation
Version:	1.1.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/classpathx/activation-%{version}.tar.gz
# Source0-md5:	de50d7728e8140eb404f2b4554321f8c
URL:		http://www.gnu.org/software/classpathx/jaf/jaf.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
Provides:	jaf
Provides:	java-activation
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU JAF is a framework for declaring what beans operate on what MIME
type data. Content handler beans can be defined to handle particular
MIME content. The JAF unites Internet standards for declaring content
with JavaBeans(TM).

%description -l pl
GNU JAF to szkielet s³u¿±cy do deklarowania, na jakim typie danych
maj± operowaæ beans. Procedura obs³ugi beans mo¿e byæ zdefiniowana do
operowania na konkretnej zawarto¶ci MIME. JAF jednoczy standardy
internetowe do deklarowania zawarto¶ci przy u¿yciu JavaBeans(TM).

%package javadoc
Summary:	API documentation for GNU JAF
Summary(pl):	Dokumentacja API GNU JAF
Group:		Documentation
Obsoletes:	java-gnu-activation-doc

%description javadoc
API documentation for GNU JavaBeans(TM) Activation Framework.

%description javadoc -l pl
Dokumentacja API GNU JavaBeans(TM) Activation Framework.

%prep
%setup -q -n activation-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
unset CLASSPATH || :
export JAVAC=%{javac}
%configure

%{__make}
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

cp -R docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog source/javax/activation/*.html
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
