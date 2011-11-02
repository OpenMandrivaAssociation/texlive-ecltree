Name:		texlive-ecltree
Version:	1.1a
Release:	1
Summary:	Trees using epic and eepic macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eclbip
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecltree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecltree.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package recursively draws trees: each subtree is defined in
a 'bundle' environment, with a set of leaves described by
\chunk macros. A chunk may have a bundle environment inside it.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ecltree/ecltree.sty
%doc %{_texmfdistdir}/doc/latex/ecltree/ecltreesample.pdf
%doc %{_texmfdistdir}/doc/latex/ecltree/ecltreesample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
