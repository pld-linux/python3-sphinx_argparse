#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Sphinx extension that automatically documents argparse commands and options
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje argparse
Name:		python3-sphinx_argparse
Version:	0.5.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-argparse/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx_argparse-%{version}.tar.gz
# Source0-md5:	d12461005ef9b3a160053fa6f7aa75a2
URL:		https://pypi.org/project/sphinx-argparse/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.7
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-Sphinx >= 5.1.0
BuildRequires:	python3-docutils >= 0.19
BuildRequires:	python3-lxml >= 4.9
BuildRequires:	python3-pytest >= 8.0
BuildRequires:	python3-typing_extensions >= 4.9
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-commonmark >= 0.5.6
BuildRequires:	python3-furo >= 2024
BuildRequires:	sphinx-pdg-3 >= 5.1.0
%endif
Requires:	python3-modules >= 1:3.10
Conflicts:	python3-commonmark < 0.5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension that automatically documents argparse commands and
options.

%description -l pl.UTF-8
Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje
argparse.

%package apidocs
Summary:	API documentation for Sphinx argparse extension
Summary(pl.UTF-8):	Dokumentacja API rozszerzenia Sphinksa argparse
Group:		Documentation

%description apidocs
API documentation for Sphinx argparse extension.

%description apidocs -l pl.UTF-8
Dokumentacja API rozszerzenia Sphinksa argparse.

%prep
%setup -q -n sphinx_argparse-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.rst README.rst
%{py3_sitescriptdir}/sphinxarg
%{py3_sitescriptdir}/sphinx_argparse-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
