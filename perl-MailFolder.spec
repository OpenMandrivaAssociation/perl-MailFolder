%define upstream_name	 MailFolder
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A folder-independant interface to email folders
License:	Artistic
Group:     	Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/K/KJ/KJOHNSON/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		http://rt.cpan.org/Ticket/Attachment/106324/20147/MailFolder-0.07-0.071.patch

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRequires:	perl(File::Sync)
BuildRequires:	perl(MIME::Head)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This base class, and companion subclasses provide an object-oriented interface
to email folders independant of the underlying folder implementation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1

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
