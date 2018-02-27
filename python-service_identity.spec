%define	oname	service_identity

Name:		python-%{oname}
Version:	17.0.0
Release:	1
Summary:	Service identity verification for pyOpenSSL
Source0:	http://pypi.python.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/pyca/service_identity
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:	python-setuptools

%description
===========================================
Service Identity Verification for pyOpenSSL
===========================================

%package -n python2-%{oname}
Summary:        Python 2.x library for service identity
Group:          Development/Python

%prep
%setup -q -n %{oname}-%{version}
mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
pushd python2
python2 setup.py build
popd
pushd python3
python3 setup.py build
popd

%install
pushd python2
python2 setup.py install --root=%{buildroot}
popd

pushd python3
python3 setup.py install --root=%{buildroot}
popd

%files
%doc python3/AUTHORS.rst
%doc python3/LICENSE
%doc python3/README.rst
%doc python3/docs/changelog.rst
%doc python3/docs/license.rst
%{py3_puresitedir}/service_identity/*.py*
%{py3_puresitedir}/service_identity*.egg-info

%files -n python2-%{oname}
%doc python2/AUTHORS.rst
%doc python2/LICENSE
%doc python2/README.rst
%doc python2/docs/changelog.rst
%doc python2/docs/license.rst
%{py2_puresitedir}/service_identity/*.py*
%{py2_puresitedir}/service_identity*.egg-info
