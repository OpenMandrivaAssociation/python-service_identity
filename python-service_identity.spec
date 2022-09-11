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

%description
===========================================
Service Identity Verification for pyOpenSSL
===========================================

%prep
%setup -q -n service-identity-%{version}

%build
python3 setup.py build


%install

pushd python3
python3 setup.py install --root=%{buildroot}

%files
%doc python3/AUTHORS.rst
%doc python3/LICENSE
%doc python3/README.rst
%doc python3/docs/changelog.rst
%doc python3/docs/license.rst
%{py3_puresitedir}/service_identity/*.py*
%{py3_puresitedir}/service_identity*.egg-info
