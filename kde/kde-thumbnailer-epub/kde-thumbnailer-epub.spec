Name:           kde-thumbnailer-epub
Version:        0.2
Release:        1%{?dist}
Summary:        KDE Thumbnailer for ePub Files

Group:          System/GUI/KDE
License:        GPL-2.0+
Url:            http://kde-apps.org/content/show.php/KDE+ePub+Thumbnailer?content=151210
Source0:        http://kde-apps.org/CONTENT/content-files/151210-%{name}-%{version}.tar.gz

BuildRequires:  ebook-tools-devel
BuildRequires:  kdelibs-devel
BuildRequires:  desktop-file-utils

%description
KDE thumbnailer plugin for the ePub file format.

%prep
%setup -q

%build
%{cmake} -DBUILD_SHARED_LIBS:BOOL=OFF
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING README TODO
%{_kde4_libdir}/kde4/epubthumbnail.so
%{_kde4_datadir}/kde4/services/epubthumbnail.desktop

%changelog
* Mon Aug 29 2012 Anıl Özbek <ozbekanil@gmail.com> - 0.2-1
- initial Fedora version
