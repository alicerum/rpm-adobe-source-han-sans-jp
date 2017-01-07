%global fontname adobe-source-han-sans-hw-jp
%global fontconf 65-0-%{fontname}.conf

%global archivename SourceHanSansHWJ

Name:           %{fontname}-fonts
Version:        1.004R
Release:        1%{?dist}
Summary:        Adobe OpenType Pan-CJK font family for Japanese

License:        OFL
URL:            https://github.com/adobe-fonts/source-han-sans/
Source0:        https://github.com/adobe-fonts/source-han-sans/raw/%{version}/OTF/%{archivename}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Source Han Sans is a sans serif Pan-CJK font family 
that is offered in seven weights—ExtraLight, Light, 
Normal, Regular, Medium, Bold, and Heavy—and 
in several OpenType/CFF-based deployment configurations
to accommodate various system requirements or limitations.

As the name suggests, Japanese fonts are intended to
support the characters necessary to render or
display text in Simplified Chinese, Traditional Chinese,
Japanese, and Korean.


%prep
%setup -q -n %{archivename}

%build


%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.otf

%license LICENSE.txt


%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug  7 2015 Peng Wu <pwu@redhat.com> - 1.004-1
- Update to 1.004

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Peng Wu <pwu@redhat.com> - 1.002-1
- Update to 1.002

* Wed Oct  8 2014 Peng Wu <pwu@redhat.com> - 1.001-1
- Update to 1.001

* Tue Sep  9 2014 Peng Wu <pwu@redhat.com> - 1.000-4
- Work around monospace English characters issue

* Mon Aug  4 2014 Peng Wu <pwu@redhat.com> - 1.000-3
- Fontconfig changes from user feed back

* Mon Jul 21 2014 Peng Wu <pwu@redhat.com> - 1.000-2
- Improves spec

* Mon Jul 21 2014 Peng Wu <pwu@redhat.com> - 1.000-1
- Initial Version
