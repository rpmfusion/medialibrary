%global commit 67797d1bb8e76d8e8fd4e0674eca199eabac3efc

Name:           medialibrary
Version:        0.2.0
Release:        1%{?dist}
Summary:        Cross platform media library

License:        GPLv2+
URL:            https://code.videolan.org/videolan/medialibrary
Source0:        %{url}/repository/%{version}/archive.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  libtool

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(libvlcpp)
BuildRequires:  pkgconfig(sqlite3)


%description
Cross platform media library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n medialibrary-%{version}-%{commit}
./bootstrap


%build
%configure --disable-static
%make_build V=1


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/medialibrary
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Feb 26 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Tue Sep  5 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file
