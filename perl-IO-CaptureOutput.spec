%define upstream_name    IO-CaptureOutput
%define upstream_version 1.1102

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Epoch:		1

Summary:	Capture STDOUT and STDERR from Perl code, subprocesses or XS
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

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

BuildArch:	noarch

%description
This module provides routines for capturing STDOUT and STDERR from perl
subroutines, forked system calls (e.g. 'system()', 'fork()') and from XS or
C modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.110.200-3mdv2012.0
+ Revision: 765368
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.1102

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1:1.110.200-2
+ Revision: 654216
- rebuild for updated spec-helper

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.110.200-1mdv2010.1
+ Revision: 506248
- bump epoch
- update to 1.1102

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1101-1mdv2010.0
+ Revision: 370133
- update to new version 1.1101

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0801-2mdv2009.0
+ Revision: 268528
- rebuild early 2009.0 package (before pixel changes)
- fix spacing at top of description

* Thu May 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0801-1mdv2009.0
+ Revision: 210006
- import perl-IO-CaptureOutput


