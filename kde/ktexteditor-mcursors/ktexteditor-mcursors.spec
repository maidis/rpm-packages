Name:           ktexteditor-mcursors
Version:        0.1
Release:        1%{?dist}
Summary:        Multiple cursors plugin for KatePart based softwares

Group:          System/GUI/KDE
License:        GPL-2.0+
Url:            https://code.google.com/p/ktexteditor-mcursors
Source0:        https://dl.dropbox.com/u/1836567/fedora/%{name}-%{version}.tar.gz

BuildRequires:  kate-devel

Requires:       kate

%description
ktexteditor-mcursors is a plugin for KatePart based softwares
(KWrite, Kate, KDevelop, Quanta, etc.) that lets you add or
remove virtual cursor in a document. All texts will be repeated
or deleted in each of the cursors.

%prep
%setup -q

%build
%{cmake} -DBUILD_SHARED_LIBS:BOOL=OFF
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
# %doc COPYING README
%{_kde4_libdir}/kde4/ktexteditor_mcursors.so
%{_kde4_datadir}/kde4/apps/ktexteditor_mcursors/mcursorsui.rc
%{_kde4_datadir}/kde4/services/ktexteditor_mcursors*

%changelog
* Sun Mar 10 2013 Anıl Özbek <ozbekanil@gmail.com> - 0.1-1
- initial Fedora version
