%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           pardus-python
Version:        0.4.8
Release:        1%{?dist}
Summary:        Python modules for Pardus

Group:          Development/Languages
License:        GPLv2+
URL:            https://github.com/Pardus-Linux/pardus-python
Source0:        https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  libX11-devel

Requires:       python
Requires:       libX11

%description
Python Modules for Pardus are the generic modules used (or to be used)
by Pardus projects.


%prep
%setup -qn %{name}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README
%dir %{python_sitearch}
%{python_sitearch}/pardus*


%changelog
* Mon Mar 04 2013 Anıl Özbek <ozbekanil@gmail.com> pardus-python-0.4.8-1
- first version
