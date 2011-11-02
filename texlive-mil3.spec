Name:		texlive-mil3
Version:	20110310
Release:	1
Summary:	Samples from Math into LaTeX, third edition
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/mil3
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mil3.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mil3.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Examples, samples and templates from the third edition of
Gratzer's book.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/mil3/README
%doc %{_texmfdistdir}/doc/latex/mil3/ams-alph.bst
%doc %{_texmfdistdir}/doc/latex/mil3/ams-pln.bst
%doc %{_texmfdistdir}/doc/latex/mil3/amsart.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/article.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/article2.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/contents
%doc %{_texmfdistdir}/doc/latex/mil3/fonttbl.tex
%doc %{_texmfdistdir}/doc/latex/mil3/gallery.tex
%doc %{_texmfdistdir}/doc/latex/mil3/german.tex
%doc %{_texmfdistdir}/doc/latex/mil3/ggamsart.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/ggart.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/ggart2.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/gratzer
%doc %{_texmfdistdir}/doc/latex/mil3/inbibl.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/intrart.tex
%doc %{_texmfdistdir}/doc/latex/mil3/intrarti.tex
%doc %{_texmfdistdir}/doc/latex/mil3/lattice.sty
%doc %{_texmfdistdir}/doc/latex/mil3/letter.tex
%doc %{_texmfdistdir}/doc/latex/mil3/master.tex
%doc %{_texmfdistdir}/doc/latex/mil3/math.tex
%doc %{_texmfdistdir}/doc/latex/mil3/mathb.tex
%doc %{_texmfdistdir}/doc/latex/mil3/multline.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/note1.tex
%doc %{_texmfdistdir}/doc/latex/mil3/note1b.tex
%doc %{_texmfdistdir}/doc/latex/mil3/note2.tex
%doc %{_texmfdistdir}/doc/latex/mil3/noteslug.tex
%doc %{_texmfdistdir}/doc/latex/mil3/sampart.tex
%doc %{_texmfdistdir}/doc/latex/mil3/sampartb.bib
%doc %{_texmfdistdir}/doc/latex/mil3/sampartb.tex
%doc %{_texmfdistdir}/doc/latex/mil3/sampartu.tex
%doc %{_texmfdistdir}/doc/latex/mil3/sample.html
%doc %{_texmfdistdir}/doc/latex/mil3/svsing2e.sty
%doc %{_texmfdistdir}/doc/latex/mil3/svsing6.cls
%doc %{_texmfdistdir}/doc/latex/mil3/template.bib
%doc %{_texmfdistdir}/doc/latex/mil3/textenv.tpl
%doc %{_texmfdistdir}/doc/latex/mil3/topmat.tpl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
