Summary:	Wizard Launcher and its collection of wizards
Name:		drakwizard
Version:	3.7.4
Release:	19
License:	GPLv2
Group:		System/Configuration/Other
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/drakwizard/trunk/
Source0:	%{name}-%{version}.tar.lzma
Source1:	%{name}.png
Patch1:		drakwizard-3.7.4-apache2.4.patch
BuildArch:		noarch

BuildRequires:	gettext-base
BuildRequires:	perl-base
Requires:	perl-base
Requires:	usermode
Requires:	perl-Locale-gettext
Requires:	drakxtools
Requires:	perl-Libconf >= 0.39.19
Requires:	drakwizard-base = %{version}-%{release}
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

%description base
Base package for drakwizard.

%prep
%setup -q
%apply_patches

%build

%install
%makeinstall
%find_lang %{name}

%files base -f %{name}.lang
%doc TODO README.adding_wizard
%config(noreplace) %{_sysconfdir}/gnome-vfs-2.0/vfolders/*
%{_sbindir}/drakwizard
%{perl_vendorlib}/MDK/Wizard/Apache.pm
%{perl_vendorlib}/MDK/Wizard/Varspaceval.pm
%{perl_vendorlib}/MDK/Wizard/Wizcommon.pm
%{perl_vendorlib}/MDK/Wizard/Wizcommon_gtk2.pm
%{perl_vendorlib}/MDK/Wizard/IFCFG.pm
%{_datadir}/wizards/desktop/*

%files
%{perl_vendorlib}/MDK/Wizard/Bind.pm
%{perl_vendorlib}/MDK/Wizard/Dhcp.pm
%{perl_vendorlib}/MDK/Wizard/Ntp.pm
%{perl_vendorlib}/MDK/Wizard/Proftpd.pm
%{perl_vendorlib}/MDK/Wizard/Squid.pm
%{perl_vendorlib}/MDK/Wizard/Sshd.pm
%{_datadir}/wizards/sshd_wizard
%{_datadir}/wizards/dhcp_wizard
%{_datadir}/wizards/dns_wizard
%{_datadir}/wizards/ftp_wizard
%{_datadir}/wizards/proxy_wizard
