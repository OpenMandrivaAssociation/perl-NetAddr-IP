%define module  NetAddr-IP
%define name    perl-%{module}
%define version 4.019
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Manage IPv4 and IPv6 addresses and subnets in Perl
Group:          Development/Perl
License:        Artistic
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/NetAddr/%{module}-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides an object-oriented abstraction on top of IP
addresses or IP subnets, that allows for easy manipulations.

%prep
%setup -q -n %{module}-%{version}
rm -f t/00-Sign.t # debug files make it fails

%build
%{__perl} Makefile.PL  INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/NetAddr
%{perl_vendorarch}/auto/NetAddr
%{_mandir}/*/*

