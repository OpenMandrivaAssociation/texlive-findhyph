# revision 26313
# category Package
# catalog-ctan /support/findhyph
# catalog-date 2012-02-06 17:29:05 +0100
# catalog-license gpl
# catalog-version 3.0
Name:		texlive-findhyph
Version:	3.0
Release:	2
Summary:	Find hyphenated words in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/findhyph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-findhyph.bin = %{EVRD}

%description
Findhyph is a Perl script that will analyse the log file from
running your document with \tracingparagraphs=1 set. The output
contains enough context to enable you to find the hyphenated
word that's being referenced.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/findhyph
%{_texmfdistdir}/scripts/findhyph/findhyph
%doc %{_texmfdistdir}/doc/support/findhyph/Makefile.doc
%doc %{_texmfdistdir}/doc/support/findhyph/README
%doc %{_texmfdistdir}/doc/support/findhyph/findhyph.bat
%doc %{_texmfdistdir}/doc/support/findhyph/findhyph.txt
%doc %{_mandir}/man1/findhyph.1*
%doc %{_texmfdir}/doc/man/man1/findhyph.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/findhyph/findhyph findhyph
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0-2
+ Revision: 812261
- Update to latest release.
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0-1
+ Revision: 772063
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 751894
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718442
- texlive-findhyph
- texlive-findhyph
- texlive-findhyph
- texlive-findhyph

