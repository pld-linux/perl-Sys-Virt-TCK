#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test requires libvirtd)
#
%include	/usr/lib/rpm/macros.perl
Summary:	libvirt TCK - Technology Compatibility Kit
Summary(pl.UTF-8):	libvirt Technology Compatibility Kit - pakiet sprawdzający kompatybilność
Name:		perl-Sys-Virt-TCK
Version:	0.1.0
Release:	1
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://libvirt.org/libvirt/tck/Sys-Virt-TCK-%{version}.tar.gz
# Source0-md5:	1acffc328fb126bafd95fa3ddb00890c
URL:		http://libvirt.org/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	libvirt-daemon
BuildRequires:	perl-Config-Record >= 1.0.0
BuildRequires:	perl-Digest
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IO-Compress
BuildRequires:	perl-IO-String
BuildRequires:	perl-Sub-Uplevel
BuildRequires:	perl-Sys-Virt >= 0.2.0
BuildRequires:	perl-TAP-Formatter-HTML
BuildRequires:	perl-TAP-Harness-Archive
BuildRequires:	perl-Test-Harness >= 3.11
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-XML-Trig
BuildRequires:	perl-XML-Writer
BuildRequires:	perl-XML-XPath
BuildRequires:	perl-accessors
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libvirt TCK provides a framework for performing testing of the
integration between libvirt drivers, the underlying virt hypervisor
technology, related operating system services and system
configuration. The idea (and name) is motivated by the Java TCK.

%description -l pl.UTF-8
libvirt TCK udostępnia szkielet do wykonywania testów integracji
między sterownikami libvirt, leżącymi poniżej ich hipernadzorcami,
powiązanymi usługami systemów operacyjnych oraz konfiguracją systemu.
Idea (i nazwa) została zainspirowana przez Java TCK.

%prep
%setup -q -n Sys-Virt-TCK-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT \
	--install_path pkgdata=%{_datadir}/libvirt-tck/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/libvirt-tck
%dir %{_sysconfdir}/libvirt-tck
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libvirt-tck/default.cfg
%dir %{perl_vendorlib}/Sys/Virt
%{perl_vendorlib}/Sys/Virt/TCK.pm
%{perl_vendorlib}/Sys/Virt/TCK
%{_datadir}/libvirt-tck
%{_mandir}/man1/libvirt-tck.1p*
