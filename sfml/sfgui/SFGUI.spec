Name:           SFGUI
Version:        0.4.0
Release:        1%{?dist}
Summary:        Graphical user interface (GUI) library for programs that use SFML for rendering

License:        zlib
Url:            https://github.com/TankOs/SFGUI
#Source0:        https://github.com/TankOs/%{name}/archive/%{version}.tar.gz
Source0:        SFGUI-0.4.0.tar.gz

BuildRequires:  SFML-devel
BuildRequires:  cmake
Requires:       ell-devel
Requires:       SFML

%description
SFGUI is a GUI (Graphical User Interface) C++ library especially
designed for programs and games that use SFML for rendering.

The library has been designed with flexibility and performance
in mind. Several features get you started really quick and make
using the library easy: The automatic layout takes care of
positioning and sizing widgets properly. Even if you have to deal
with different screen resolutions, SFGUI will always try to pick
the best layout.

Included are a lot of widgets, like buttons, toggle buttons,
check buttons, radio buttons, drop down boxes, entries, scrollbars
and some more. At any time you can extend the library by custom widgets.

The widgets' visuals are completely separated from their implementations.
SFGUI makes use of so called "widget rendering engines" to create the
visuals. One engine is included in the release, called BREW, which
uses simple shapes and solid colors to paint the widgets. The shapes,
colors, fonts etc. can be modified by setting style properties, which
can be done directly in C++ or by loading external theme files, which
look similar to CSS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       ell-devel
 
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

# fixup non needed executable permission on regular files
find -type f -print0 | xargs -0 chmod -x
# use system-wide extlibs; so, delete everything modulo libELL header files
find extlibs/ -type f ! -name 'libELL*' -print0 | xargs -0 rm
 

%build
%{cmake} -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release .
make %{?_smp_mflags}

%install
%make_install
mkdir $RPM_BUILD_ROOT%{_libdir}/cmake
mkdir $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}
cp $RPM_BUILD_ROOT%{_datadir}/%{name}/cmake/* $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}/
ln -s %{_libdir}/libSFGUI.so $RPM_BUILD_ROOT%{_libdir}/libSFGUI.so.0.4.0
ln -s %{_libdir}/libSFGUI.so $RPM_BUILD_ROOT%{_libdir}/libSFGUI.so.0.4
ln -s %{_libdir}/libSFGUI.so $RPM_BUILD_ROOT%{_libdir}/libSFGUI.so.0
ln -s %{_libdir}/libSFGUI.so $RPM_BUILD_ROOT%{_libdir}/libsfgui.so

%files
%doc *.md
%{_libdir}/*.so*

%files devel
%{_libdir}/cmake/%{name}/*.cmake
%{_includedir}/%{name}/
%{_libdir}/libSFGUI.so
%{_datadir}/%{name}

%changelog
* Mon Feb 25 2019 Anıl Özbek <ozbekanil@gmail.com> - 0.4.0-1
- initial Fedora version
