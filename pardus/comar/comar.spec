# Copyright (c) 2010 Gökçen Eraslan <gokcen@pardus.org.tr>
# Copyright (c) 2013 Anıl Özbek <ozbekanil@gmail.com>

Name:           comar
Version:        3.0.3
Release:        1%{?dist}
Summary:        Manages system configuration

Group:          System/Base
License:        GPLv2
Url:            https://github.com/Pardus-Linux/COMAR
Source:         https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.bz2
Patch0:         fix-flags.patch
Patch1:         update-system-manager-model.patch

BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  polkit-devel

Requires:       dbus
Requires:       python
Requires:       polkit
Requires:       comar-api

%description
ÇOMAR (pronounced chow-mar), is the COnfiguration MAnageR that helps
the installed software operate flawlessly. Çomar knows the tasks 
that can be provided by each application, together with the 
functionality they depend on and other information. Different
applications may adapt themselves according to the presence and 
capability of their peers.


%prep
%setup -qn %{name}-%{version}

%patch0 -p1
%patch1 -p1

%build
%cmake
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/sbin/comar
/var/db/comar3/models
/var/db/comar3/modules
%{_datadir}/dbus-1/system-services/tr.org.pardus.comar.service
%{_datadir}/dbus-1/system-services/tr.org.pardus.comar2.service
%{_datadir}/polkit-1/actions
%{_sysconfdir}/dbus-1/system.d/tr.org.pardus.comar.conf
%{_prefix}/bin/hav
%{_prefix}/bin/comar2to3

%changelog
* Mon Mar 04 2013 Anıl Özbek <ozbekanil@gmail.com> comar-3.0.3
- version bump

* Sat Jul 13 2010 Gökçen Eraslan <gokcen@pardus.org.tr> comar-2.9.9
- first version
