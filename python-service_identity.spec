%define	oname	service_identity

Name:		python2-%{oname}
Version:	14.0.0
Release:	3
Summary:	Service identity verification for pyOpenSSL
Source0:	http://pypi.python.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/pyca/service_identity
BuildArch:	noarch
BuildRequires:	python2-setuptools
Requires:	pythonegg(characteristic) >= 14.3.0
Requires:	pythonegg(pyasn1-modules)
%rename		python-%oname

%description
===========================================
Service Identity Verification for pyOpenSSL
===========================================

%prep
%setup -q -n %{oname}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc AUTHORS.rst
%doc LICENSE
%doc README.rst
%doc docs/changelog.rst
%doc docs/license.rst
%{py2_puresitedir}/service_identity/*.py*
%{py2_puresitedir}/service_identity*.egg-info
