Name:		python-s3fs
Version:	2023.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/s3fs/s3fs-%{version}.tar.gz
Summary:	Convenient Filesystem interface over S3
URL:		https://pypi.org/project/s3fs/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Convenient Filesystem interface over S3

%prep
%autosetup -p1 -n s3fs-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/s3fs
%{py_sitedir}/s3fs-*.*-info
