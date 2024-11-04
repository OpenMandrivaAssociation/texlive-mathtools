Name:		texlive-mathtools
Version:	72487
Release:	1
Summary:	Mathematical tools to use with amsmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathtools
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathtools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathtools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathtools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Mathtools provides a series of packages designed to enhance the
appearance of documents containing a lot of mathematics. The
main backbone is amsmath, so those unfamiliar with this
required part of the LaTeX system will probably not find the
packages very useful. Mathtools provides many useful tools for
mathematical typesetting. It is based on amsmath and fixes
various deficiencies of amsmath and standard LaTeX. It
provides: Extensible symbols, such as brackets, arrows,
harpoons, etc.; Various symbols such as \coloneqq (:=); Easy
creation of new tag forms; Showing equation numbers only for
referenced equations; Extensible arrows, harpoons and
hookarrows; Starred versions of the amsmath matrix environments
for specifying the column alignment; More building blocks:
multlined, cases-like environments, new gathered environments;
Maths versions of \makebox, \llap, \rlap etc.; Cramped math
styles; and more... Mathtools requires mhsetup.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mathtools
%{_texmfdistdir}/tex/latex/mathtools
%doc %{_texmfdistdir}/doc/latex/mathtools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
