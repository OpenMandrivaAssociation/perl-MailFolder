%define module	MailFolder
%define name	perl-%{module}
%define version 0.07
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A folder-independant interface to email folders
license:	Artistic
Group:     	Development/Perl
Source:		http://www.cpan.org/authors/id/K/KJ/KJOHNSON/%{module}-%{version}.tar.bz2
Patch:		http://rt.cpan.org/Ticket/Attachment/106324/20147/MailFolder-0.07-0.071.patch
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRequires:	perl(File::Sync)
BuildRequires:	perl(MIME::Head)

%description
This base class, and companion subclasses provide an object-oriented interface
to email folders independant of the underlying folder implementation.

%prep
%setup -q -n %{module}-%{version} 
%patch -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/Mail

