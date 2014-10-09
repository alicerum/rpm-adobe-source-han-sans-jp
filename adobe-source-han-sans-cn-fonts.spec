%global fontname adobe-source-han-sans-cn
%global fontconf 65-0-%{fontname}.conf

%global archivename SourceHanSansCN-%{version}

Name:           adobe-source-han-sans-cn-fonts
Version:        1.001
Release:        1%{?dist}
Summary:        Adobe OpenType Pan-CJK font family for Simplified Chinese

License:        ASL 2.0
URL:            https://github.com/adobe-fonts/source-han-sans/
# the original upstream tar ball is too large, use the download script instead
Source0:        %{archivename}.zip
Source1:        %{name}-fontconfig.conf
Source2:        http://downloads.sourceforge.net/source-han-sans.adobe/LICENSE.txt
# the script to download fonts
Source3:        fetchcnfont.sh

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Source Han Sans is a sans serif Pan-CJK font family 
that is offered in seven weights—ExtraLight, Light, 
Normal, Regular, Medium, Bold, and Heavy—and 
in several OpenType/CFF-based deployment configurations
to accommodate various system requirements or limitations.

As the name suggests, Pan-CJK fonts are intended to
support the characters necessary to render or
display text in Simplified Chinese, Traditional Chinese,
Japanese, and Korean.


%prep
%setup -q -n %{archivename}

%build


%install

#install doc
install -m 0644 -p %{SOURCE2} .

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.otf

%doc LICENSE.txt


%changelog
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
