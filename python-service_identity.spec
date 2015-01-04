%define	oname	service_identity

Name:		python-%{oname}
Version:	14.0.0
Release:	1
Summary:	Service identity verification for pyOpenSSL
Source0:	http://pypi.python.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/pyca/service_identity
BuildArch:	noarch
BuildRequires:	pythonegg(setuptools)
Requires:	pythonegg(characteristic) >= 14.3.0
Requires:	pythonegg(pyasn1-modules)

%description
===========================================
Service Identity Verification for pyOpenSSL
===========================================

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS.rst
%doc LICENSE
%doc README.rst
%doc docs/changelog.rst
%doc docs/license.rst
%{py_puresitedir}/service_identity/*.py*
%{py_puresitedir}/service_identity*.egg-info
