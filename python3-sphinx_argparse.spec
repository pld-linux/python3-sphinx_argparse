#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx extension that automatically documents argparse commands and options
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje argparse
Name:		python3-sphinx_argparse
Version:	0.4.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-argparse/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx_argparse-%{version}.tar.gz
# Source0-md5:	db32f8c3208cf136b29268d1bdf61f71
URL:		https://pypi.org/project/sphinx-argparse/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.2.0
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
Conflicts:	python3-commonmark < 0.5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension that automatically documents argparse commands and
options.

%description -l pl.UTF-8
Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje
argparse.

%prep
%setup -q -n sphinx_argparse-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinxarg
%{py3_sitescriptdir}/sphinx_argparse-%{version}-py*.egg-info
