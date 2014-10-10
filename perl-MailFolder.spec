%define upstream_name	 MailFolder
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A folder-independant interface to email folders
License:	Artistic
Group:     	Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/K/KJ/KJOHNSON/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		http://rt.cpan.org/Ticket/Attachment/106324/20147/MailFolder-0.07-0.071.patch

BuildRequires:	perl-devel
BuildRequires:	perl(File::Sync)
BuildRequires:	perl(MIME::Head)

BuildArch:	noarch

%description
This base class, and companion subclasses provide an object-oriented interface
to email folders independant of the underlying folder implementation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorlib}/Mail


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 403846
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.07-8mdv2009.0
+ Revision: 257684
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.07-7mdv2009.0
+ Revision: 245768
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.07-5mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-5mdv2008.0
+ Revision: 86539
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-4mdv2007.0
- Rebuild

* Mon Apr 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-3mdk
- buildrequires

* Sun Apr 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-2mdk
- spec rewrite
- drop initial patch, use CPAN patch instead to fix tests

* Sun Mar 27 2005 Bruno Cornec <bcornec@mandrake.org> 0.07-1mdk
- Initial build.

