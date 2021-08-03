%global commit 0c3868052024a1c6256383294e92baeeedcb44e9

Name:           medialibrary
Version:        0.6.0
Release:        4%{?dist}
Summary:        Cross platform media library

License:        GPLv2+
URL:            https://code.videolan.org/videolan/medialibrary
Source0:        %{url}/repository/%{version}/archive.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         gcc-10.patch

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
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Tue Sep  5 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file
