Summary:	Easily serialize dataclasses to and from JSON
Summary(pl.UTF-8):	Łatwa serializacja dataclass do/z JSON-a
Name:		python3-dataclasses-json
Version:	0.6.7
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dataclasses-json/
Source0:	https://files.pythonhosted.org/packages/source/d/dataclasses-json/dataclasses_json-%{version}.tar.gz
# Source0-md5:	bfcfcd66a85092c89e7b04ed8fa07a9e
URL:		https://pypi.org/project/dataclasses-json/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-poetry-core >= 1.2.0
BuildRequires:	python3-poetry-dynamic-versioning
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a simple API for encoding and decoding
dataclasses to and from JSON.

%description -l pl.UTF-8
Ta biblioteka udostępnia proste API do kodowania i dekodowania
dataclass do/z JSON-a.

%prep
%setup -q -n dataclasses_json-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/dataclasses_json
%{py3_sitescriptdir}/dataclasses_json-%{version}.dist-info
