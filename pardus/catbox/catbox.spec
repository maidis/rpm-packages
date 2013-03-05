%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           catbox
Version:        1.6
Release:        1%{?dist}
Summary:        Python sandboxing module

Group:          Development/Languages
License:        GPLv2+
URL:            https://github.com/Pardus-Linux/catbox
Source0:        https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.gz

BuildRequires:  python-devel

Requires:       python

%description
catbox is a Python sandboxing module commonly used by
the package management system of Pardus, PiSi.


%prep
%setup -qn %{name}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Fix permissions
chmod 755 $RPM_BUILD_ROOT%{python_sitearch}/*.so


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README OKUBENİ
%dir %{python_sitearch}
%{python_sitearch}/%{name}*
%{_bindir}/catbox


%changelog
* Sun Mar 03 2013 Anıl Özbek <ozbekanil@gmail.com> catbox-1.6-1
- version bump

* Sat Jul 13 2012 Anıl Özbek <ozbekanil@gmail.com> catbox-1.2-1
- first version
