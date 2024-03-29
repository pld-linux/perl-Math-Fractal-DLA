#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Fractal-DLA
Summary:	Math::Fractal::DLA - Diffusion Limited Aggregation (DLA) generator
Summary(pl.UTF-8):	Math::Fractal::DLA - generator fraktali DLA
Name:		perl-Math-Fractal-DLA
Version:	0.21
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ed161b97d7ad3834525b1ade02425cd
URL:		http://search.cpan.org/dist/Math-Fractal-DLA/
BuildRequires:	perl-GD >= 1.27
%if %{with tests}
BuildRequires:	perl-Log-LogLite >= 0.8
BuildRequires:	perl-Test-Simple >= 0.54
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fractal::DLA is a Diffusion Limited Aggregation (DLA) fractal
generator.

%description -l pl.UTF-8
Moduł Math::Fractal::DLA jest generatorem fraktali DLA (Diffusion
Limited Aggregation).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Fractal/DLA.pm
%{perl_vendorlib}/Math/Fractal/DLA
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.mc
