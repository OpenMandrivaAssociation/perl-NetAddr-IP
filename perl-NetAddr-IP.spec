%define upstream_name    NetAddr-IP
%define upstream_version 4.044

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:        Manage IPv4 and IPv6 addresses and subnets in Perl
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/modules/by-module/NetAddr/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides an object-oriented abstraction on top of IP
addresses or IP subnets, that allows for easy manipulations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/00-Sign.t # debug files make it fails

%build
%{__perl} Makefile.PL  INSTALLDIRS=vendor
%make

%check
%make test

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
