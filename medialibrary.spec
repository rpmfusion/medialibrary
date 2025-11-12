%global commit 8c56e26c625d757994cffeea84d2a0a2e6033dee

Name:           medialibrary
Version:        0.13.2
Release:        1%{?dist}
Summary:        Cross platform media library

License:        GPLv2+
URL:            https://code.videolan.org/videolan/medialibrary
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libtool

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(libjpeg)
#BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(libvlcpp)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  cmake
BuildRequires:  meson


%description
Cross platform media library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n medialibrary-%{version}

%build
%meson -Dlibvlc=disabled
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete

%check
%meson_test

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/medialibrary
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Nov 12 2025 Nicolas Chauvet <kwizart@gmail.com> - 0.13.2-1
- Update to 0.13.2

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 01 2025 Sérgio Basto <sergio@serjux.com> - 0.13.1-1
- Update medialibrary to 0.13.1

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.13.0-1
- Update to 0.13.0

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Sérgio Basto <sergio@serjux.com> - 0.12.3-1
- Update medialibrary to 0.12.3
- Disable libvlc fix the build (tip from Debian package)

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

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
