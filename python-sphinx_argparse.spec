#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension that automatically documents argparse commands and options
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje argparse
Name:		python-sphinx_argparse
Version:	0.2.5
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-argparse/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx-argparse-%{version}.tar.gz
# Source0-md5:	b137944fbbe26c88d54ee106bf0569ab
Patch0:		%{name}-tests.patch
URL:		https://pypi.org/project/sphinx-argparse/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.2.0
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.2.0
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
Conflicts:	python-commonmark < 0.5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension that automatically documents argparse commands and
options.

%description -l pl.UTF-8
Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje
argparse.

%package -n python3-sphinx_argparse
Summary:	Sphinx extension that automatically documents argparse commands and options
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje argparse
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
Conflicts:	python3-commonmark < 0.5.6

%description -n python3-sphinx_argparse
Sphinx extension that automatically documents argparse commands and
options.

%description -n python3-sphinx_argparse -l pl.UTF-8
Rozszerzenie Sphinksa automatycznie dokumentujące polecenia i opcje
argparse.

%prep
%setup -q -n sphinx-argparse-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/sphinxarg
%{py_sitescriptdir}/sphinx_argparse-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_argparse
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/sphinxarg
%{py3_sitescriptdir}/sphinx_argparse-%{version}-py*.egg-info
%endif
