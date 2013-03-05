%define name zemberek
%define version 2.1.1

Summary:       Zemberek NLP library
Name:          %{name}
Version:       %{version}
Release:       4%{?dist}
License:       MPL
Group:         Development/Java
URL:           http://zemberek.googlecode.com
Source:        http://zemberek.googlecode.com/files/%{name}-%{version}-src.zip
Source1:       zemberek-demo
BuildRequires: java-1.7.0-openjdk-devel
BuildRequires: ant
BuildRoot:     %{_tmppath}/%{name}-buildroot
Requires:      java-1.7.0-openjdk

%description
Zemberek is an open source, platform independent, general purpose Natural Language Processing 
library and toolset designed for Turkic languages, especially Turkish.

%prep
%setup -q -n %{name}-%{version}-src

%build
ant jar-cekirdek jar-demo jar-tr

%install
%{__mkdir_p}  %{buildroot}%{_libdir}/%{name}
for jar in cekirdek demo tr; do
    cp -v dagitim/jar/%{name}-${jar}-%{version}.jar %{buildroot}%{_libdir}/%{name}/%{name}2-${jar}.jar
done

%{__install}  -D -m 755 %{S:1}   %{buildroot}%_bindir/%{name}-demo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/%{name}/*
%doc surumler.txt dokuman/lisanslar/zemberek-license.txt


%changelog
* Sat Jun 09 2012 Anıl Özbek <ozbekanil@gmail.com> zemberek-2.1.1-4
- Some small fixes for Fedora 17

* Tue Apr 14 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.com> zemberek-2.1.1-3
- Fixed some wrong specifications of .spec file 

* Thu Mar 11 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.com> zemberek-2.1.1-2
- Fixed some specifications of .spec file 

* Thu Jan 28 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.com> zemberek-2.1.1-1
- Inıtial RPM
- Ported to Mandriva
