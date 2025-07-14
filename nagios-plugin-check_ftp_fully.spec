%define		plugin	check_ftp_fully
Summary:	Nagios plugin to check FTP transfers
Summary(pl.UTF-8):	Wtyczka Nagiosa sprawdzająca ...
Name:		nagios-plugin-%{plugin}
Version:	0.1
Release:	3
License:	GPL v2+
Group:		Networking
Source0:	http://www.deathwing00.org/nagios/check_ftp_fully
# Source0-md5:	821dbac0cc911e8250e41d7cca56cc62
Source1:	%{plugin}.cfg
Patch0:		args.patch
Patch1:		bashisms.patch
Patch2:		get-path.patch
URL:		http://exchange.nagios.org/directory/Plugins/Network-Protocols/FTP/check_ftp_fully/details
Requires:	lftp
Requires:	mktemp >= 1.5
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		nrpeddir	/etc/nagios/nrpe.d
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
This script uses lftp, a sophisticated ftp/http client, to check not
only that a give FTP account is accessible, but that it is also able
to list files and directories, to get and put files and to delete
files. This simple script is fast, easy to configure, flexible and can
be extended easily.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
