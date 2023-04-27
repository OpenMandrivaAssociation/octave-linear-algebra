%global octpkg linear-algebra

Summary:	Additional linear algebra code, including general SVD and matrix functions
Name:		octave-linear-algebra
Version:	2.2.3
Release:	2
License:	GPLv3+ and LGPLv3+ and BSD
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/linear-algebra/
Source0:	https://downloads.sourceforge.net/octave/linear-algebra-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Additional linear algebra code, including general SVD and matrix functions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

