%define		plugin	flowplayer
Summary:	Flowplayer - The video player for the Web
Name:		jquery-%{plugin}
Version:	5.4.3
Release:	1
# The free version comes with a GPL-based license and carries a Flowplayer logo. Commercial use is allowed.
License:	GPL v3 with additional term
Group:		Applications/WWW
Source0:	http://releases.flowplayer.org/%{version}/flowplayer-%{version}.zip
# Source0-md5:	da8ad2a064b6b6efb57fd70d1a29fe49
URL:		http://flowplayer.org/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jquery >= 1.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Flowplayer design is simple and minimalistic. The player will look as
good on your site as it looks on ours.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p %{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p %{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
cp -p %{plugin}.swf $RPM_BUILD_ROOT%{_appdir}
cp -a skin $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%{_appdir}
