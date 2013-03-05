%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           comar-api
Version:        2.4.9
Release:        1%{?dist}
Summary:        Utility functions for Comar scripts

Group:          Development/Languages
License:        GPLv2+
URL:            https://github.com/Pardus-Linux/COMAR
Source0:        https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.gz
Patch0:         add-stopdependencies.patch

BuildRequires:  python-devel

Requires:       python
Requires:       pardus-python

%description
Generic utility library for common Comar script operations.


%prep
%setup -qn %{name}-%{version}

%patch0 -p1


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#%dir %{python_sitearch}
#%{python_sitearch}/comar*
/usr/lib/python2.7/site-packages/comar*


%changelog
* Mon Mar 04 2013 Anıl Özbek <ozbekanil@gmail.com> comar-api-2.4.9-1
- first version
