#
# spec file for package python-ec2uploadimg
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define upstream_name ec2uploadimg
Name:           python-ec2uploadimg
Version:        1.1.3
Release:        0
Summary:        Upload an image to EC2
License:        GPL-3.0+
Group:          System/Management
Url:            https://github.com/SUSE/Enceladus
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python
Requires:       python-boto3
Requires:       python-ec2utilsbase >= 2.0.2
Requires:       python-ec2utilsbase < 3.0.0
Requires:       python-paramiko
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Upload a compressed .raw disk image to Amazon EC2 and create a snapshot
or register and AMI

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/ec2uploadimg.1 %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/ec2uploadimg.1

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_mandir}/man*/*
%dir %{python_sitelib}/ec2utils
%dir %{python_sitelib}/%{upstream_name}-%{version}-py%{py_ver}*
%{python_sitelib}/*
%{_bindir}/*

%changelog
