%define modname	NetAddr-IP
%define modver 4.075

Summary:	Manage IPv4 and IPv6 addresses and subnets in Perl

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/NetAddr/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
This module provides an object-oriented abstraction on top of IP
addresses or IP subnets, that allows for easy manipulations.

%prep
%setup -qn %{modname}-%{modver}
rm -f t/00-Sign.t # debug files make it fails

%build
%__perl Makefile.PL  INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorarch}/NetAddr
%{perl_vendorarch}/auto/NetAddr
%{_mandir}/man3/*
