#
# TODO: R,BR,/etc file
#
Summary:	Cluster SSH - Cluster Admin Via SSH
Name:		clusterssh
Version:	3.22
Release:	0.3
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/clusterssh/%{name}-%{version}.tar.gz
# Source0-md5:	f568c3ade1e586250ff22045a11eff37
URL:		http://sourceforge.net/projects/clusterssh
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-X11-Protocol
Suggests:	xterm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClusterSSH controls a number of xterm windows via a single graphical
console window to allow commands to be interactively run on multiple
servers over an ssh connection.

%prep
%setup -q

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_iconsdir}/hicolor/{48x48,32x32,24x24},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install clusterssh-32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32
install clusterssh-48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48
install clusterssh-24x24.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24
install clusterssh.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS

%attr(755,root,root) %{_bindir}/cssh
%{_mandir}/man1/cssh.*
%{_desktopdir}/clusterssh.desktop
%{_iconsdir}/hicolor/*/clusterssh-*.png
