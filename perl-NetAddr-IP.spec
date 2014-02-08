%define upstream_name    NetAddr-IP
%define upstream_version 4.044

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 4.44.0-3mdv2012.0
+ Revision: 765510
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 4.44.0-2
+ Revision: 764028
- rebuilt for perl-5.14.x

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.44.0-1
+ Revision: 677374
- update to new version 4.044

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.43.0-1
+ Revision: 654158
- update to new version 4.043

* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.42.0-1
+ Revision: 648091
- update to new version 4.042

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.41.0-1
+ Revision: 643415
- update to new version 4.041

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.40.0-1
+ Revision: 638933
- update to new version 4.040
- update to new version 4.038

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.37.0-1mdv2011.0
+ Revision: 601983
- new version

* Fri Nov 19 2010 Oden Eriksson <oeriksson@mandriva.com> 4.36.0-1mdv2011.0
+ Revision: 599051
- 4.036

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 4.35.0-1mdv2011.0
+ Revision: 596631
- update to 4.035

* Mon Oct 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.33.0-1mdv2011.0
+ Revision: 589355
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 4.30.0-2mdv2011.0
+ Revision: 564570
- rebuild for perl 5.12.1

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 4.30.0-1mdv2011.0
+ Revision: 561946
- update to 4.030

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.28.0-2mdv2011.0
+ Revision: 555300
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 4.28.0-1mdv2011.0
+ Revision: 552479
- update to 4.028

* Wed Jun 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.027-1mdv2010.1
+ Revision: 384739
- update to new version 4.027

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.026-1mdv2009.1
+ Revision: 353616
- update to new version 4.026

* Thu Jan 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.024-1mdv2009.1
+ Revision: 335368
- update to new version 4.024

* Sat Jan 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.023-1mdv2009.1
+ Revision: 330409
- update to new version 4.023
- update to new version 4.023

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.022-1mdv2009.1
+ Revision: 320439
- update to new version 4.022

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.021-1mdv2009.1
+ Revision: 314255
- update to new version 4.021

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.019-1mdv2009.1
+ Revision: 309311
- update to new version 4.019

* Tue Nov 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.017-1mdv2009.1
+ Revision: 306764
- update to new version 4.017

* Tue Nov 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.015-1mdv2009.1
+ Revision: 299762
- update to new version 4.015

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.014-1mdv2009.1
+ Revision: 299402
- update to new version 4.014

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.012-1mdv2009.1
+ Revision: 295509
- update to new version 4.012

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.011-1mdv2009.1
+ Revision: 292291
- update to new version 4.011

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 4.007-3mdv2009.0
+ Revision: 223847
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 4.007-2mdv2008.1
+ Revision: 152173
- rebuild for new perl
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.007-1mdv2008.0
+ Revision: 56123
- new version


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.004-1mdv2007.0
- new release

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.33-1mdk
- New release 3.33

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 3.028-2mdk
- Fix SPEC according to Perl Policy
    - Source URL

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.028-1mdk
- New release 3.028
- %%mkrel

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.25-1mdk
- New release 3.25
- spec cleanup

* Fri Jun 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.24-1mdk
- 3.24
- trim description

* Wed Nov 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.21-1mdk
- 3.21

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.20-1mdk
- Initial mdk release

