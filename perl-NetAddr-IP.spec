# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname NetAddr-IP
%define modver 4.079

Summary:	Manage IPv4 and IPv6 addresses and subnets in Perl

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/NetAddr::IP
Source0:	http://www.cpan.org/modules/by-module/NetAddr/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module provides an object-oriented abstraction on top of IP
addresses or IP subnets, that allows for easy manipulations.

%prep
%setup -qn %{modname}-%{modver}
rm -f t/00-Sign.t # debug files make it fails

%build
perl Makefile.PL  INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%{perl_vendorarch}/NetAddr
%{perl_vendorarch}/auto/NetAddr
%doc %{_mandir}/man3/*
