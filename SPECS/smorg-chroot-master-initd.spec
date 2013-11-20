# Don't compress/strip/[compile python]
%define __os_install_post %{nil}
%define name smorg-chroot-master-initd
%define version 1.0.0
%define release 1
# RH6 is more strict (and it's right! - the 'wrapper's should be built here)
%define debug_package %{nil}

Summary: Package to deploy init scripts for a chroot'ed nagios
Name: smorg-chroot-master-initd
Version: 1.0.0
Release: 1
License: GPL
Group: Applications/System
Source: smorg-chroot-master-initd-1.tar.gz
#Requires: bash, grep, smorg-nagios-plugins, bc, sysstat, bind-utils
# PreReq: sh-utils
BuildRoot: %{_tmppath}/%{name}-buildroot
Packager: Mark Clarkson
Vendor: Smorg

%description
Copies init scripts that can start nagios related services in a chroot.

%prep
%setup -q

%pre

%post

%preun

%postun

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
#install -d -m 0755 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins
install -m 755 chroot-functions ${RPM_BUILD_ROOT}%{_initrddir}/chroot-functions
install -m 755 crond-chroot ${RPM_BUILD_ROOT}%{_initrddir}/crond-chroot
install -m 755 gearmand-chroot ${RPM_BUILD_ROOT}%{_initrddir}/gearmand-chroot
install -m 755 httpd-chroot ${RPM_BUILD_ROOT}%{_initrddir}/httpd-chroot
install -m 755 nagios-chroot ${RPM_BUILD_ROOT}%{_initrddir}/nagios-chroot
install -m 755 npcd-chroot ${RPM_BUILD_ROOT}%{_initrddir}/npcd-chroot
install -m 755 rsyslog-chroot ${RPM_BUILD_ROOT}%{_initrddir}/rsyslog-chroot
install -m 755 ssh-chroot ${RPM_BUILD_ROOT}%{_initrddir}/ssh-chroot
install -m 755 smorg-chroot ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/smorg-chroot


%files
%defattr(755,root,root,755)
%{_initrddir}/chroot-functions
%{_initrddir}/crond-chroot
%{_initrddir}/gearmand-chroot
%{_initrddir}/httpd-chroot
%{_initrddir}/nagios-chroot
%{_initrddir}/npcd-chroot
%{_initrddir}/rsyslog-chroot
%{_initrddir}/ssh-chroot
%config(noreplace) %{_sysconfdir}/sysconfig/smorg-chroot

%clean
%{__rm} -rf %{buildroot}

%changelog
* Wed Nov 20 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Initial
