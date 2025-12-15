%define module service-identity
%define uname service_identity

Name:		python-%{uname}
Version:	24.2.0
Release:	2
Summary:	Service Identity Verification for pyOpenSSL & cryptography
Source0:	https://github.com/pyca/service-identity/archive/refs/tags/%{version}/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/pyca/service_identity
BuildSystem: python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(cryptography)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(idna)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyopenssl)
BuildRequires:	python%{pyver}dist(pyasn1)
BuildRequires:	python%{pyver}dist(pyasn1-modules)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(attrs)
Requires:	python%{pyver}dist(cryptography)
Requires:	python%{pyver}dist(pyasn1)
Requires:	python%{pyver}dist(pyasn1-modules)
Suggests:	python%{pyver}dist(idna)
Suggests:	python%{pyver}dist(pyopenssl)


%description
Use this package if:

  You want to verify that a PyCA cryptography certificate is valid for a
  certain hostname or IP address,

  Or if you use pyOpenSSL and don’t want to be MITMed,

  Or if you want to inspect certificates from either for service IDs.

service-identity aspires to give you all the tools you need for verifying
whether a certificate is valid for the intended purposes.

In the simplest case, this means host name verification.

However, service-identity implements RFC 6125 fully.

%files
%{py_puresitedir}/%{uname}
%{py_puresitedir}/%{uname}-%{version}*.dist-info
%license LICENSE
