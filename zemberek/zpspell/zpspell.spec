Name:    zpspell
Summary: Zemberek-Pardus spell checker interface
Version: 0.4.3
Release: 1%{?dist}

License: GPLv2
URL:     http://www.pardus.org.tr
Source0: http://cekirdek.pardus.org.tr/~baris/zpspell/zpspell-0.4.3.tar.bz2
Patch1:  add-gobject-linkage-11566.diff
Patch2:  find_path-GLIB_CONFIG_DIR.diff

BuildRequires: dbus-glib-devel
BuildRequires: gobject-introspection-devel

Requires: zemberek-server

%description
Zemberek-Pardus spell checker interface uses zemberek-server.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
%defattr(-,root,root)
%{_bindir}/*
%doc AUTHORS README COPYING*

%changelog
* Sat Jun 09 2012 Anıl Özbek <ozbekanil@gmail.com> zpspell-0.4.3-1
- first try
