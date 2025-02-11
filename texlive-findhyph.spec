Name:		texlive-findhyph
Version:	47444
Release:	2
Summary:	Find hyphenated words in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/findhyph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.doc.r%{version}.tar.xz
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
%doc %{_mandir}/man1/findhyph.1*
%doc %{_texmfdistdir}/doc/man/man1/findhyph.man1.pdf
%doc %{_texmfdistdir}/doc/support/findhyph/Makefile.doc
%doc %{_texmfdistdir}/doc/support/findhyph/README
%doc %{_texmfdistdir}/doc/support/findhyph/findhyph.bat
%doc %{_texmfdistdir}/doc/support/findhyph/findhyph.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/findhyph/findhyph findhyph
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
