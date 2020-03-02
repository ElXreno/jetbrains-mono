# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/JetBrains/JetBrainsMono
Version:            1.0.3
%forgemeta

Release: 3%{?dist}
URL:     https://jetbrains.com/mono/

%global foundry           JetBrains
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE
%global fontdocs          *md

%global fontfamily        JetBrains Mono
%global fontsummary       A mono-space font family containing coding ligatures
%global fonts             ttf/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
JetBrains Mono is a developer-oriented font family.

Its forms are simple and free from unnecessary details. Rendered in small
sizes, the text looks crisper. The easier the forms, the faster the eye
perceives them and the less effort the brain needs to process them.

The shape of ovals approaches that of rectangular symbols. This makes the whole
pattern of the text more clear-сut. The outer sides of ovals ensure there are
no additional obstacles for your eyes as they scan the text vertically.

Characters remain standard in width, but the height of the lowercase is
maximized. This approach keeps code lines to the length that developers expect,
and it helps improve rendering since each letter occupies more pixels.

JetBrains Mono uses a 9° italic angle; this maintains the optimal contrast to
minimize distraction and eye strain. The usual angle is about 11°–12°.

The inclusion of coding ligatures will enhance source code rendering at the
expense of everything else.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0.3-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0.3-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.03-1
✅ Initial packaging
