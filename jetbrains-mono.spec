%global priority 60
%global fontname jetbrains-mono

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:           jetbrains-mono
Version:        1.0.3
Release:        1%{?dist}
Summary:        JetBrains Mono – the free and open-source typeface for developers

License:        ASL 2.0
URL:            https://www.jetbrains.com/lp/mono/
Source0:        https://github.com/JetBrains/JetBrainsMono/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        jetbrains-mono.metainfo.xml
Source2:        jetbrains-mono-fonts.conf

BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  fontpackages-devel >= 1.13
BuildRequires:  xorg-x11-font-utils
# Requires:       

%description
JetBrains Mono – the free and open-source typeface for developers.


%prep
%autosetup -n JetBrainsMono-%{version}


%build
# Empty


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_datadir}/fonts/%{fontname} %{buildroot}%{catalogue}/%{name}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{priority}-%{fontname}.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/jetbrains-mono.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{priority}-%{fontname}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{priority}-%{fontname}.conf

mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}



%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/appdata/*.metainfo.xml


%files
%doc README.md
%dir %{_datadir}/fonts/%{fontname}
%{_datadir}/fonts/%{fontname}/*.ttf
%{_datadir}/appdata/*.metainfo.xml
%{_datadir}/fontconfig/conf.avail/*-%{fontname}.conf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*-%{fontname}.conf
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}



%changelog
* Sun Feb 09 2020 ElXreno <elxreno@gmail.com> - 1.0.3-1
- Updated to version 1.0.3

* Sat Jan 18 2020 ElXreno <elxreno@gmail.com>
- Initial packaging
