%define name drakwizard
%define version 3.7.4
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.lzma
Source1: %name.png
License: GPL
Group: System/Configuration/Other
Requires: perl-base, usermode, perl-Locale-gettext, drakxtools >= 9.1-0.4mdk, perl-Libconf >= 0.39.19, drakwizard-base = %{version}-%{release}
BuildRequires: gettext-base, perl-base
Buildroot: %{_tmppath}/%{name}
BuildArch: noarch
Prefix: %{_prefix}
Obsoletes: wizards_lib-dhcp wizards_lib-ftp wizards_lib-web wizards_lib wizard wizards_lib-time wizards_lib-global wizards_lib-dns wizards_lib-server wizards_lib-proxy wizards_lib-db wizards_lib-news wizards_lib-firewall wizards_lib-client wizards_lib-common wizards_lib-postfix
Provides: wizards_lib-dhcp wizards_lib-ftp wizards_lib-web wizards_lib wizard wizards_lib-time wizards_lib-global wizards_lib-dns wizards_lib-server wizards_lib-proxy wizards_lib-db wizards_lib-news wizards_lib-firewall wizards_lib-client wizards_lib-common wizards_lib-postfix
Summary: Wizard Launcher and its collection of wizards
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/drakwizard/trunk/

%description
drakwizard allows you to launch :
- server wizard: configures basic services.
- global wizard: wizard that launch each other.
- dhcpd, dns, ftp, apache, time wizards, ssh.

%package base
Summary: Base of Wizard Launcher
Group: System/Configuration/Other
Conflicts: drakwizard < 3.0-1mdk

%description base
Base package for drakwizard.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/$RPM_PACKAGE_NAME

%files base -f %{name}.lang
%defattr(-,root,root)
%doc TODO README.adding_wizard
%config(noreplace) %_sysconfdir/gnome-vfs-2.0/vfolders/*
%_sbindir/drakwizard
%{perl_vendorlib}/MDK/Wizard/Apache.pm
%{perl_vendorlib}/MDK/Wizard/Varspaceval.pm
%{perl_vendorlib}/MDK/Wizard/Wizcommon.pm
%{perl_vendorlib}/MDK/Wizard/Wizcommon_gtk2.pm
%{perl_vendorlib}/MDK/Wizard/IFCFG.pm
%_datadir/wizards/desktop/*

%files -f %{name}.lang
%defattr(-,root,root)
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


