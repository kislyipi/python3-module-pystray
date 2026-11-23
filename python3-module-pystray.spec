%define upstream_name pystray
%define pypi_name pystray

Name: python3-module-pystray
Version: 0.19.5
Release: alt1

Summary: Provides systray integration
License: LGPL-3.0-or-later
Group: Development/Python3
Url: https://github.com/moses-palmer/pystray
VCS: https://github.com/moses-palmer/pystray
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/pystray/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Nov 21 2026 Maxim Olyunin <kislyipi@altlinux.org> 0.19.5-alt1
- Initial build for ALT Linux.
