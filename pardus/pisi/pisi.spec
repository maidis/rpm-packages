%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           pisi
Version:        2.4
Release:        1%{?dist}
Summary:        Package management system of Pardus

Group:          Development/Languages
License:        GPLv2+
URL:            https://github.com/Pardus-Linux/pisi

Patch0:         disable-sandbox-for-emul32-builds.patch
Patch1:         kerneltools-fix.patch
Patch2:         better_cleaning_perl_packages.patch
Patch3:         improve_emul32.diff
Patch4:         add_python3_support.diff
Patch5:         WorkDir.patch
#Patch6:         preinstall-issues.patch
Patch7:         verbose-index.patch
Patch8:         assign-devel-and-doc-packages.patch
Patch9:         bugzilla-address.diff

Source0:        https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.bz2
Source1:        https://dl.dropbox.com/u/1836567/fedora/pisi/manager.py
Source2:        https://dl.dropbox.com/u/1836567/fedora/pisi/package.py
Source3:        https://dl.dropbox.com/u/1836567/fedora/pisi/mirrors.conf
Source4:        https://dl.dropbox.com/u/1836567/fedora/pisi/pisi.conf-i686
Source5:        https://dl.dropbox.com/u/1836567/fedora/pisi/pisi.conf-x86_64
Source6:        https://dl.dropbox.com/u/1836567/fedora/pisi/pisi.xml
Source7:        https://dl.dropbox.com/u/1836567/fedora/pisi/sandbox.conf

Source8:        https://dl.dropbox.com/u/1836567/fedora/pisi/pisi-128x128.png
Source9:        https://dl.dropbox.com/u/1836567/fedora/pisi/pisi-64x64.png
Source10:       https://dl.dropbox.com/u/1836567/fedora/pisi/pisi-48x48.png
Source11:       https://dl.dropbox.com/u/1836567/fedora/pisi/pisi-32x32.png
Source12:       https://dl.dropbox.com/u/1836567/fedora/pisi/pisi-16x16.png

BuildRequires:  python-devel
BuildRequires:  gettext-devel
BuildRequires:  comar
BuildRequires:  comar-api
BuildRequires:  piksemel
BuildRequires:  catbox

Requires:       python
Requires:       gettext
Requires:       comar
Requires:       comar-api
Requires:       piksemel
Requires:       catbox


%description
PiSi is a modern package management system implemented in Python.
Some of its main features are: package sources are written in
XML and python, implements all functions through a
simple-to-use API, integrates low-level and high-level
package management features.


%prep
%setup -qn %{name}-%{version}

%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p0
#%patch6 -p1
%patch7 -p0
%patch8 -p0
%patch9 -p1


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
#%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib=%{_libdir}/pardus
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE6} %{buildroot}%{_datadir}/mime/packages/pisi.xml

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p %{SOURCE8} %{buildroot}%{_datadir}/pixmaps/pisi.png

mkdir -p %{buildroot}%{_datadir}/icons/Pardus/128x128/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/Pardus/64x64/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/Pardus/48x48/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/Pardus/32x32/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/Pardus/16x16/mimetypes

cp -p %{SOURCE8} %{buildroot}%{_datadir}/icons/Pardus/128x128/mimetypes/application-x-pisi.png
cp -p %{SOURCE9} %{buildroot}%{_datadir}/icons/Pardus/64x64/mimetypes/application-x-pisi.png
cp -p %{SOURCE10} %{buildroot}%{_datadir}/icons/Pardus/48x48/mimetypes/application-x-pisi.png
cp -p %{SOURCE11} %{buildroot}%{_datadir}/icons/Pardus/32x32/mimetypes/application-x-pisi.png
cp -p %{SOURCE12} %{buildroot}%{_datadir}/icons/Pardus/16x16/mimetypes/application-x-pisi.png

mkdir -p %{buildroot}%{_sysconfdir}/pisi
cp -p %{SOURCE3} %{buildroot}%{_sysconfdir}/pisi/mirrors.conf
cp -p %{SOURCE5} %{buildroot}%{_sysconfdir}/pisi/pisi.conf
cp -p %{SOURCE7} %{buildroot}%{_sysconfdir}/pisi/sandbox.conf

ln -sf /usr/bin/pisi-cli       ${RPM_BUILD_ROOT}%{_bindir}/pisi

%find_lang %{name} --all-name


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ApiPlan AUTHORS ChangeLog* CODING COPYING README RefactorPlan TODO
/usr/share/doc/pisi

#%dir %{_libdir}/pardus
#%{_libdir}/pardus/*
%dir /usr/lib/python2.7/site-packages
/usr/lib/python2.7/site-packages/*

%{_bindir}/*

%config(noreplace) %{_sysconfdir}/pisi/mirrors.conf
%config(noreplace) %{_sysconfdir}/pisi/pisi.conf
%config(noreplace) %{_sysconfdir}/pisi/sandbox.conf

%{_datadir}/pixmaps/pisi.png
%{_datadir}/icons/Pardus/*/mimetypes/application-x-pisi.png
%{_datadir}/mime/packages/pisi.xml


%post
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/Pardus &>/dev/null || :


%postun
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Pardus &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Pardus &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Pardus &>/dev/null || :


%changelog
* Sat Jul 13 2012 Anıl Özbek <ozbekanil@gmail.com> pisi-2.4-1
- first version
