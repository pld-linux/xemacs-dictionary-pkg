%define 	srcname	dictionary
Summary:	Emacs package for talking to a dictionary server
Summary(pl):	Pakiet emacsa do ³±czenia z serwerem s³owników
Name:		xemacs-%{srcname}-pkg
Version:	1.12
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	717517bbad4e241f18941fd6c289b868
URL:		http://www.xemacs.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emacs package for talking to a dictionary (DICT) server.

%description -l pl
Pakiet emacsa do ³±czenia z serwerem s³owników (DICT).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a lisp $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/%{srcname}/ChangeLog lisp/%{srcname}/README
%{_datadir}/xemacs-packages/lisp/*/*.el*
