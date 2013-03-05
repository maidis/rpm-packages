%define name zemberek-server
%define version 0.7.1
%define mydir %{buildroot}/%{_libdir}/%{name}

Summary:        Turkish spell checker server
Name:           %{name}
Version:        %{version}
Release:        2%{?dist}
License:        MPL
Group:          Text tools
URL:            http://zemberek.googlecode.com
Source:         http://zemberek.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        zemberek-server
Source2:        zemberek-server.init
BuildRequires:  ant
BuildRequires:  apache-mina
BuildRequires:  java-1.7.0-openjdk-devel
Requires:       dbus-java
Requires:       zemberek
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
A Turkish spell checker server based on Zemberek NLP library.

%prep
%setup  -c -n %{name}

%build
ant dist

%install
%{__mkdir_p} %{mydir}
cp dist/zemberek-server-0.7.1.jar %{mydir}/%{name}.jar
cp dist/lib/mina-core-1.1.0.jar %{mydir}/mina-core.jar
cp dist/lib/slf4j-nop.jar %{mydir}/slf4j-nop.jar
mkdir -p %{buildroot}/%{_sysconfdir}/dbus-1/system.d/
cp dist/config/%{name}.conf %{buildroot}/%{_sysconfdir}/dbus-1/system.d/%{name}.conf
cp config/conf.ini %{buildroot}/%{_sysconfdir}/%{name}.ini
%{__install}  -D -m 755 %{S:1}   %{buildroot}/%{_bindir}/%{name}
%{__install}  -D %{S:2}   %{buildroot}/%{_sysconfdir}/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%preun
%_preun_service %{name}

%post
%_post_service %{name}


%files
%defattr(-,root,root)
#%doc surumler.txt dokuman/lisanslar/zemberek-license.txt

%{_libdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}.ini
%{_sysconfdir}/dbus-1/system.d/%{name}.conf
%{_sysconfdir}/rc.d/init.d/%{name}
%{_bindir}/%{name}

%changelog
* Sat Jun 09 2012 Anıl Özbek <ozbekanil@gmail.com> zemberek-server-0.7.1-2
- Some small fixes for Fedora 17

* Thu Mar 11 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.com> zemberek-server-0.7.1-1
- Inıtial RPM
- Ported to Mandriva
- Fixed zemberek-server shell script due to changes of libmatthew-java libs
