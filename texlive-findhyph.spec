Name:		texlive-findhyph
Version:	2.0
Release:	1
Summary:	Find hyphenated words in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/findhyph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-findhyph.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Findhyph is a Perl script that will analyse the log file from
running your document with \tracingparagraphs=1 set. The output
contains enough context to enable you to find the hyphenated
word that's being referenced.

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
%{_bindir}/findhyph
%{_texmfdistdir}/scripts/findhyph/findhyph
%doc %{_texmfdistdir}/doc/support/findhyph/Makefile
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
