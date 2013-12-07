# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eclbip
# catalog-date 2008-06-01 23:17:13 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-ecltree
Version:	1.1a
Release:	5
Summary:	Trees using epic and eepic macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eclbip
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecltree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecltree.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package recursively draws trees: each subtree is defined in
a 'bundle' environment, with a set of leaves described by
\chunk macros. A chunk may have a bundle environment inside it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 751319
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 718301
- texlive-ecltree
- texlive-ecltree
- texlive-ecltree
- texlive-ecltree

