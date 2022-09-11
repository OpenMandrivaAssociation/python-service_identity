%define	oname	service_identity

Name:		python-%{oname}
Version:	21.1.0
Release:	1
Summary:	Service identity verification for pyOpenSSL
Source0:	https://files.pythonhosted.org/packages/9a/3d/9eb0563e066ea0540cf580695593ab079376e920016d4d1b3ff2fd8abf4b/service-identity-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/pyca/service_identity
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
Requires: python3dist(pyasn1-modules)

%description
===========================================
Service Identity Verification for pyOpenSSL
===========================================

%prep
%setup -q -n service-identity-%{version}

%build
%py_build

%install
%py_install

%files
%{py3_puresitedir}/service_identity/*.py*
%{py3_puresitedir}/service_identity*.egg-info
