#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pathspec
Version  : 0.9.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/f6/33/436c5cb94e9f8902e59d1d544eb298b83c84b9ec37b5b769c5a0ad6edb19/pathspec-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f6/33/436c5cb94e9f8902e59d1d544eb298b83c84b9ec37b5b769c5a0ad6edb19/pathspec-0.9.0.tar.gz
Summary  : Utility library for gitignore style pattern matching of file paths.
Group    : Development/Tools
License  : MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: pathspec-license = %{version}-%{release}
Requires: pathspec-python = %{version}-%{release}
Requires: pathspec-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
*pathspec*: Path Specification
==============================
*pathspec* is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself is
derived from Rsync's wildmatch. Git uses wildmatch for its `gitignore`_
files.

%package license
Summary: license components for the pathspec package.
Group: Default

%description license
license components for the pathspec package.


%package python
Summary: python components for the pathspec package.
Group: Default
Requires: pathspec-python3 = %{version}-%{release}

%description python
python components for the pathspec package.


%package python3
Summary: python3 components for the pathspec package.
Group: Default
Requires: python3-core
Provides: pypi(pathspec)

%description python3
python3 components for the pathspec package.


%prep
%setup -q -n pathspec-0.9.0
cd %{_builddir}/pathspec-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626730608
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pathspec
cp %{_builddir}/pathspec-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/pathspec/9744cedce099f727b327cd9913a1fdc58a7f5599
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pathspec/9744cedce099f727b327cd9913a1fdc58a7f5599

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
