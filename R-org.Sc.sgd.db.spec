%global packname  org.Sc.sgd.db
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.6.4
Release:          1
Summary:          Genome wide annotation for Yeast
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods R-AnnotationDbi 
Requires:         R-methods R-AnnotationDbi 
Requires:         R-annotate 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-AnnotationDbi
BuildRequires:    R-methods R-AnnotationDbi 
BuildRequires:    R-annotate 

%description
Genome wide annotation for Yeast, primarily based on mapping using ORF
identifiers from SGD.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
