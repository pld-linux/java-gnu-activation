#
Summary:	GNU JavaBeans(TM) Activation Framework (JAF)
Name:		java-gnu-activation
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/classpathx/activation-%{version}.tar.gz
# Source0-md5:	de50d7728e8140eb404f2b4554321f8c
URL:		http://www.gnu.org/software/classpathx/jaf/jaf.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	jdk
Requires:	jre
Provides:	jaf
Provides:	java-activation
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU JAF is a framework for declaring what beans operate on what MIME
type data. Content handler beans can be defined to handle particular
MIME content. The JAF unites internet standards for declaring content
with JavaBeans(TM).

%prep
%setup -q -n activation-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
# Sun java requires . in CLASSPATH for configure test
export CLASSPATH=.
export JAVAC=%{_bindir}/javac
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog source/javax/activation/*.html
%{_javadir}/*.jar
