#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Fractal-DLA
Summary:	Math::Fractal::DLA - Diffusion Limited Aggregation (DLA) Generator
Summary(pl):	Math::Fractal::DLA - generator fraktali DLA
Name:		perl-Math-Fractal-DLA
Version:	0.20
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3d645fb1dc29245aaec49a657607aa8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-GD >= 1.27
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fractal::DLA is a Diffusion Limited Aggregation (DLA) fractal
generator.

%description -l pl
Modu³ Math::Fractal::DLA jest generatorem fraktali DLA (Diffusion
Limited Aggregation).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
%dir %{perl_vendorlib}/Math/Fractal
%{perl_vendorlib}/Math/Fractal/DLA.pm
%{perl_vendorlib}/Math/Fractal/DLA
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.mc
