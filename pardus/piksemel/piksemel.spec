%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           piksemel
Version:        1.3.1
Release:        1%{?dist}
Summary:        Python binding for iksemel

Group:          Development/Languages
License:        GPLv2+
URL:            https://svn.pardus.org.tr/uludag/trunk/piksemel
Source0:        https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.bz2

BuildRequires:  python-devel
BuildRequires:  iksemel-devel

Requires:       python
Requires:       iksemel

%description
piksemel is a simple, fast, small and robust XML parser
for Python, based on iksemel.


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
%doc README
%dir %{python_sitearch}
%{python_sitearch}/%{name}*


%changelog
* Sat Jul 13 2012 Anıl Özbek <ozbekanil@gmail.com> piksemel-1.3.1-1
- first version
