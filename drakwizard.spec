Summary:	Wizard Launcher and its collection of wizards
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/drakwizard/trunk/
Name:		drakwizard
Version:	3.7.4
Release:	6
Source0:	%{name}-%{version}.tar.lzma
Source1:	%name.png
License:	GPL
Group:		System/Configuration/Other
Requires:	perl-base
Requires:	usermode
Requires:	perl-Locale-gettext
Requires:	drakxtools >= 9.1-0.4mdk
Requires:	perl-Libconf >= 0.39.19
Requires:	drakwizard-base = %{version}-%{release}
BuildRequires:	gettext-base
BuildRequires:	perl-base
BuildArch:		noarch
Obsoletes:	wizards_lib-dhcp < %{version}-%{release}
Obsoletes:	wizards_lib-ftp < %{version}-%{release}
Obsoletes:	wizards_lib-web < %{version}-%{release}
Obsoletes:	wizards_lib < %{version}-%{release}
Obsoletes:	wizard < %{version}-%{release}
Obsoletes:	wizards_lib-time < %{version}-%{release}
Obsoletes:	wizards_lib-global < %{version}-%{release}
Obsoletes:	wizards_lib-dns < %{version}-%{release}
Obsoletes:	wizards_lib-server < %{version}-%{release}
Obsoletes:	wizards_lib-proxy < %{version}-%{release}
Obsoletes:	wizards_lib-db < %{version}-%{release}
Obsoletes:	wizards_lib-news < %{version}-%{release}
Obsoletes:	wizards_lib-firewall < %{version}-%{release}
Obsoletes:	wizards_lib-client < %{version}-%{release}
Obsoletes:	wizards_lib-common < %{version}-%{release}
Obsoletes:	wizards_lib-postfix < %{version}-%{release}
Provides:	wizards_lib-dhcp
Provides:	wizards_lib-ftp
Provides:	wizards_lib-web
Provides:	wizards_lib wizard
Provides:	wizards_lib-time
Provides:	wizards_lib-global
Provides:	wizards_lib-dns
Provides:	wizards_lib-server
Provides:	wizards_lib-proxy
Provides:	wizards_lib-db
Provides:	wizards_lib-news
Provides:	wizards_lib-firewall
Provides:	wizards_lib-client
Provides:	wizards_lib-common
Provides:	wizards_lib-postfix


%description
drakwizard allows you to launch :
- server wizard: configures basic services.
- global wizard: wizard that launch each other.
- dhcpd, dns, ftp, apache, time wizards, ssh.

%package base
Summary:	Base of Wizard Launcher
Group:		System/Configuration/Other
Conflicts:	drakwizard < 3.0-1mdk

%description base
Base package for drakwizard.

%prep
%setup -q

%build

%install
%makeinstall
%find_lang %{name}

%files base -f %{name}.lang
%doc TODO README.adding_wizard
%config(noreplace) %_sysconfdir/gnome-vfs-2.0/vfolders/*
%_sbindir/drakwizard
%{perl_vendorlib}/MDK/Wizard/Apache.pm
%{perl_vendorlib}/MDK/Wizard/Varspaceval.pm
%{perl_vendorlib}/MDK/Wizard/Wizcommon.pm
%{perl_vendorlib}/MDK/Wizard/Wizcommon_gtk2.pm
%{perl_vendorlib}/MDK/Wizard/IFCFG.pm
%_datadir/wizards/desktop/*

%files
%{perl_vendorlib}/MDK/Wizard/Bind.pm
%{perl_vendorlib}/MDK/Wizard/Dhcp.pm
%{perl_vendorlib}/MDK/Wizard/Ntp.pm
%{perl_vendorlib}/MDK/Wizard/Proftpd.pm
%{perl_vendorlib}/MDK/Wizard/Squid.pm
%{perl_vendorlib}/MDK/Wizard/Sshd.pm
%_datadir/wizards/sshd_wizard
%_datadir/wizards/dhcp_wizard
%_datadir/wizards/dns_wizard
%_datadir/wizards/ftp_wizard
%_datadir/wizards/proxy_wizard




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.7.4-3mdv2011.0
+ Revision: 663863
- mass rebuild

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 3.7.4-2mdv2011.0
+ Revision: 556987
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 3.7.4-1mdv2010.1
+ Revision: 546241
- 3.7.4
- translation updates

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.7.3-3mdv2010.1
+ Revision: 522534
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.7.3-2mdv2010.0
+ Revision: 413399
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 3.7.3-1mdv2009.1
+ Revision: 367439
- translation updates

* Mon Mar 23 2009 Thierry Vignaud <tv@mandriva.org> 3.7.2-1mdv2009.1
+ Revision: 360627
- DNS wizard:
  o fix crashing when adding new host (#37251, #47018)
  o fix crashing when finishing adding an host (#37452)
  o fix 5 other #37452-like crashes
- fix 14 other #37452-like crashes in Apache, DHCP, DNS client, NTP,
  proftpd, PXE, squid, SSH wizards

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.7.1-2mdv2009.1
+ Revision: 350881
- rebuild

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 3.7.1-1mdv2009.0
+ Revision: 289959
- updated translations

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 3.7-1mdv2009.0
+ Revision: 286968
- updated translations

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.6-2mdv2009.0
+ Revision: 220703
- rebuild

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 3.6-1mdv2008.1
+ Revision: 192104
- updated translations

* Mon Mar 31 2008 Nicolas Vigier <nvigier@mandriva.com> 3.5-2mdv2008.1
+ Revision: 191214
- updated translations
- update descriptions

* Fri Mar 28 2008 Nicolas Vigier <nvigier@mandriva.com> 3.5-1mdv2008.1
+ Revision: 190940
- also start dhcpd and named servers
- start httpd and squid services on boot (#39254)
- updated translations

* Tue Mar 18 2008 Nicolas Vigier <nvigier@mandriva.com> 3.3-1mdv2008.1
+ Revision: 188720
- fix crash from bug #38937
- fix garbaging UTF-8 when localized messages are read (#37314) (tvignaud)
- disable FQDN test for ssh-server (aginies)
- Update Czech translation (mbukovjan)

* Wed Mar 05 2008 Nicolas Vigier <nvigier@mandriva.com> 3.2-3mdv2008.1
+ Revision: 180144
- remove disabled wizards so that mcc does not offer to run them

* Wed Mar 05 2008 Nicolas Vigier <nvigier@mandriva.com> 3.2-2mdv2008.1
+ Revision: 179653
- fix broken drakwizard

* Mon Mar 03 2008 Nicolas Vigier <nvigier@mandriva.com> 3.2-1mdv2008.1
+ Revision: 178112
- fix bug #38359 in squid wizard : 5s instead of 30s for shutdown_lifetime
  so the initscript is faster (andreas)
- disable broken wizards (aginies)
- fix bug #36616 to avoid opening drakbug when hostname is set to
  localhost (nvigier)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 3.1-5mdv2008.1
+ Revision: 149385
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Antoine Ginies <aginies@mandriva.com> 3.1-4mdv2008.0
+ Revision: 90870
- update po files

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 3.1-3mdv2008.0
+ Revision: 29225
- fix Bind wizard bug (#30936)


* Fri Mar 02 2007 Antoine Ginies <aginies@mandriva.com> 3.1-2mdv2007.0
+ Revision: 131312
- Import drakwizard

* Fri Mar 02 2007 Antoine Ginies <aginies@mandriva.com> 3.1-2mdv2007.1
- fix #12581, #15214 and #21698 , thanks to neoclust for the patch

* Sun Sep 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 3.1-1mdv2007.0
- updated translations

* Thu Sep 14 2006 Antoine Ginies <aginies@mandriva.com> 3.0-29mdv2007.0
- fix bug #25508 : DNS configuration crashes after putting an ip address into the External DNS
  field.
- update all PO files (thx all translators)

* Thu Jun 22 2006 Antoine Ginies <aginies@mandriva.com> 3.0-28mdv2007.0
- add a third NTP server server
- fix layout of various wizards
- remove sambaprint wizard (user should now use draksambashare)
- fix ftp default port to 21
- disable kolab and inn wizards (don't know how to use/fix them, help welcome)
- fix default image
- fix ask_warn in NIS wizard

* Wed Jun 21 2006 Antoine Ginies <aginies@mandriva.com> 3.0-27mdv2007.0
- fix problem of fixed list and value in summary

* Wed Jun 21 2006 Antoine Ginies <aginies@mandriva.com> 3.0-26mdv2007.0
- fix ask_warn bug (#21550)
- Samba wizard ask for netbios server name (#18480)
- fix postfix message size limit (#22145)

* Thu Mar 16 2006 Antoine Ginies <aginies@mandriva.com> 3.0-25mdk
- remove default password in kolab server

* Wed Feb 15 2006 Antoine Ginies <aginies@mandriva.com> 3.0-24mdk
- fix bug #20162
- do not install packages in testing mode (tvignaud)
- blino: 
   * bug #20360
   * use the new wizards API
   * use wizards::check_rpm
   * simplify and perl_checker style
   * rename wizards hash to avoid confusion
   * bless directly the wizard object instead of wrapping it in a hash
   * drop old wizard stuff, use the wizards module
   * fix additionnal wizard detection

* Tue Nov 29 2005 Antoine Ginies <aginies@n3.mandriva.com> 3.0-23mdk
- misc fix bug #19999

* Sat Sep 10 2005 <guibo@guibpiv.guibland.com> 3.0-22mdk
- Bind: fix serial pb. (#17886)
- Fix Samba wizard.
- Kolab: answer yes to erase old conf if needed

* Fri Sep 09 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-21mdk
- fix gtk_log box output
- fix kolab wizard

* Wed Sep 07 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-20mdk
- NTP: fix bug #18193 (pb with progressbar), banner
- Apache: banner, bug #18131
- Dhcp: fix next/back pb, banner
- Proxy, Ldap, Bind, FTP, NFS, Postfix: fix missing banner
- Nis: test nisdomainame value, fix missing banner

* Tue Sep 06 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-19mdk
- major update of PO files (thx all translators)
- Web: fix user directory problem

* Thu Sep 01 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-18mdk
- Fix icon pb in banner
- fix Ldap Wizard

* Tue Aug 30 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-17mdk
- Postfix: fix masquerade domains misconfiguration
- Sambashare: various fix (public, write list)
- update all PO files (thx all translators)
- use new icons (thx ln)

* Tue Aug 23 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-16mdk
- various improvement in sambashare wizard

* Thu Aug 11 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-15mdk
- fix install server wizard
- cosmetic fix in drakwizard
- various fix to be able to re run drakwizard in console mode (#16839)

* Wed Aug 10 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-14mdk
- split into drakwizard, and drakwizard-base
- update all PO files (thx all translators)
- remove entry in menu

* Tue Aug 09 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-13mdk
- FTP: fix bug #16899
- Squid: fix bug #17112 
- Postfix: fix bug #17207
- Ntp: use timezone #15630

* Thu Jul 14 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-12mdk
- various fix in sambashare
- add sambaprinters wizard
- various fix in samab wizard (thx kikim test)
- fix apache DocumentRoot pb

* Wed Jul 06 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-11mdk
- fix Missing file (Postfix Wizard Bug 16664)
- add a progress bar fonction
- Install server: use progress bar to see copy status
- Ntp: use progress bar to see NTP query status
- various typo fix
- Apache: fix user_mod (Bug 16688)

* Fri Jul 01 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-10mdk
- fix apache wizard require
- fix postfix default configuration file
- Install server wizard: add help ans some information

* Thu Jun 30 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-9mdk
- Ssh: fix ergo, glueconf support tabulation
- Samba: 
         - use samba.conf.default instead of smb.conf.clean
         - fix resolv name order option (samba wizard)
- Sambashare:
         - re-enable valid|write list
         - test if samba use exist
         - support more than one user (fix sambapasswd)
- add Sambaprint wizard (need various improvement/test/debug)
- Apache: fix wizard since rpm numbering change (thx Raphaël Gertz)

* Wed Jun 08 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-8mdk
- add ssh wizard
- various fix in Samba and Sambashare wizard:
	- create sambauser
	- remove unwanted option (read list, admin users)
	- test directory
	- fix some typo in tips
- fix IFCFG.pm (blino)

* Wed Jun 08 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-7mdk
- fix Postfix wizard (thx again anne /test/report/debug)
- FTP: can choose ServerName or port number, add some tips

* Tue Jun 07 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-6mdk
- Samba: use smb.conf.clean if no /etc/samba/smb.conf exist
- Postfix: new release

* Thu Jun 02 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-5mdk
- fix some rpmlint error
- various fix in Samba and Sambashare wizard

* Thu Jun 02 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-4mdk
- add Wizard to Manage Samba share
- various fix and improvement in Samba wizard
- add Wizard menu

* Wed Jun 01 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-3mdk
- add share management
- various fix in pdc and bdc mode
- add more options (pdc, bdc, standalone mode)
- require libconf 0.39.16 (in fact nightly build release)

* Tue May 31 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 3.0-2mdk
- Samba wizard:
      * detect previous Samba type
      *	add more tips
      * add more information
      * add more help
      * add LDAP configuration
      * add more test

* Fri May 27 2005 Antoine Ginies <aginies@n1.mandriva.com> 3.0-1mdk
- use libconf in Samba Wizard
- Clean Proftpd and Nisautofs

* Tue Apr 12 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.15-6mdk
- fix password pb in ldap wizard (Bug 15214)

* Fri Apr 08 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.15-5mdk
- remove mandrakelinux strings
- fix Linux install server

* Sat Apr 02 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.15-4mdk
- remove kolab wizard

* Wed Mar 30 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.15-3mdk
- fix ldap wizard

* Fri Mar 18 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.15-2mdk
- fix ldap root passwd (padbol)
- update po

* Thu Jan 27 2005 Antoine Ginies <aginies@mandrakesoft.com> 2.15-1mdk
- remove nis configuration client (included in drakauth)
- fix autofs map (hardcoded nis path :/) thx Fabrice Facora
- improve Hostname and domainename test

* Tue Oct 05 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.14-10mdk
- fix kolab wizard (needed_rpm, call correct kolab_boostrap script)

* Fri Oct 01 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.14-9mdk
- fix smb smb.conf s/;/#/ to workaround a bug... (thx misc Buchan)
- Check hostname and domainname Add service ldap stop when delete conf

* Thu Sep 09 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.14-8mdk
- fix drakwizard in console mode
- update po

* Wed Sep 08 2004 guibo <aginies@mandrakesoft.com> 2.14-7mdk
- fix pb of Dhcpd.conf and dhcpd_interface
- NIS wizard: fix pb of nsswitch.conf file
- fix samba share directory pb

* Wed Sep 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.14-6mdk
- working LDAP wizard

* Wed Aug 11 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.14-5mdk
- fix Samba printer pb
- fix permit root login under Proftpd

* Tue Aug 10 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.14-4mdk
- reload nfs in Mandrakelinux install server 
- typo fix in Samba wizard 
- DNS: now can remove host in dns, add increment serial
- remove drakwizard pxe (now use drakpxelinux please)

* Fri Jul 30 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.14-3mdk
- fix kolab needed_rpm
- Samba: fix pb of "enable share"
- fix squid config (missing visible_hostname) 
- thx nico-labs for all test

* Fri Jul 30 2004 mdkc <mdkc@dhcp114.mandrakesoft.com> 2.14-2mdk
- force apache2 (remove apache1.3 wizard)

* Fri Jul 30 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 2.14-1mdk
- DNS: fix dnsdoimaine test
- DHCP: fix interface choice

* Wed Jul 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.13-1mdk
- DHCP and NFS wizards: popup error messages
- DHCP wizard:
  o run more checks
  o display more meaningful error messages
- translation snapshot

* Thu Mar 25 2004 Antoine Ginies <aginies@mandrakesoft.com> 2.12-4mdk
- new fix kolab installtion pb.

* Thu Mar 25 2004 Antoine Ginies <aginies@mandrakesoft.com> 2.12-3mdk
- fix kolab installation problem (misc)

* Tue Mar 23 2004 guibo Antoine Ginies <aginies@mandrakesoft.com> 2.12-2mdk
- set default RAMsize to 48000
- updated po

* Thu Mar 18 2004 Antoine Ginies <aginies@no.mandrakesoft.com> 2.12-1mdk
- NFS, Bind: add information
- Kolab.pm: security: hide password (tv)
- updated po

* Fri Mar 12 2004 Antoine Ginies <aginies@no.mandrakesoft.com> 2.11-6mdk
- Kolab: fix typo error in bn_pwd
- Postfix: fix pb of relayhost
- Samba: fix printer sharing appear when not selected

* Thu Mar 11 2004 Antoine Ginies <aginies@mandrakesoft.com> 2.11-5mdk
- kolab: fix password PB

* Thu Mar 11 2004 Antoine Ginies <aginies@mandrakesoft.com> 2.11-4mdk
- updated po
- add kolab Wizard
- Postfix: fix cannonical pb 
- PXE: fix Menu problem
- DNS: cant access add/remove hosts if host is a DNS slave

