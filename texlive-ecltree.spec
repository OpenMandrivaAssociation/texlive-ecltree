%global tl_name ecltree
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Trees using epic and eepic macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eclbip
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecltree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecltree.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package recursively draws trees: each subtree is defined in a
'bundle' environment, with a set of leaves described by \chunk macros. A
chunk may have a bundle environment inside it.

