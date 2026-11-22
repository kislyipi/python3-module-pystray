%define upstream_name pystray
%define pypi_name pystray

Name: python3-module-pystray
Version: 0.19.5
Release: alt1
BuildArch: noarch

Summary: Provides systray integration
License: LGPL-3.0-or-later
Group: Development/Python3
Url: https://github.com/moses-palmer/pystray
VCS: https://github.com/moses-palmer/pystray

Source0: %name-%version.tar

Autoreq: yes, nocpp

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# tests are not shipped in PyPI sdist; upstream tests require GUI/X11
true

%files
%doc README.rst
%python3_sitelibdir/pystray/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Nov 21 2026 Maxim Olyunin <maximilian.kislyi@gmail.com> 0.19.5-alt1
- Initial build for ALT Linux
