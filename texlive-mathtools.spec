%global tl_name mathtools
%global tl_revision 78251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.31
Release:	%{tl_revision}.1
Summary:	Mathematical tools to use with amsmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathtools
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathtools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathtools.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathtools.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsmath)
Requires:	texlive(tools)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Mathtools provides a series of packages designed to enhance the
appearance of documents containing a lot of mathematics. The main
backbone is amsmath, so those unfamiliar with this required part of the
LaTeX system will probably not find the packages very useful. Mathtools
provides many useful tools for mathematical typesetting. It is based on
amsmath and fixes various deficiencies of amsmath and standard LaTeX. It
provides: Extensible symbols, such as brackets, arrows, harpoons, etc.;
Various symbols such as \coloneqq (:=); Easy creation of new tag forms;
Showing equation numbers only for referenced equations; Extensible
arrows, harpoons and hookarrows; Starred versions of the amsmath matrix
environments for specifying the column alignment; More building blocks:
multlined, cases-like environments, new gathered environments; Maths
versions of \makebox, \llap, \rlap etc.; Cramped math styles; and
more... Mathtools requires mhsetup.

