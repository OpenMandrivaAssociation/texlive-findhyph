%global tl_name findhyph
%global tl_revision 47444

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.4
Release:	%{tl_revision}.1
Summary:	Find hyphenated words in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/findhyph
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/findhyph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(findhyph.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Findhyph is a Perl script that will analyse the log file from running
your document with \tracingparagraphs=1 set. The output contains enough
context to enable you to find the hyphenated word that's being
referenced.

