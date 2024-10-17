%define modname	IO-CaptureOutput

Summary:	Capture STDOUT and STDERR from Perl code, subprocesses or XS
Name:		perl-%{modname}
Version:	1.1105
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel

%description
This module provides routines for capturing STDOUT and STDERR from perl
subroutines, forked system calls (e.g. 'system()', 'fork()') and from XS or
C modules.

%prep
%autosetup -p1 -n %{modname}-%{version}
%__perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes META.yml LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*


