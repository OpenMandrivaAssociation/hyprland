Name:           hyprland
Version:        0.40.0
Release:        1
Summary:        Dynamic tiling Wayland compositor
Group:          Hyprland
License:        BSD-3-Clause
URL:            https://hyprland.org/
Source0:        https://github.com/hyprwm/Hyprland/releases/download/v%{version}/source-v%{version}.tar.gz
#Patch1:         0001-fixed-patchd-wlroots-build.patch
# Source: https://github.com/hyprwm/Hyprland/pull/3589. Will be included in the next release.
#Patch2:         fix_ia86_std_clamp.patch
Patch0:         https://src.fedoraproject.org/rpms/hyprland/blob/rawhide/f/no-git.patch
Patch1:		fix-build.patch
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  jq
BuildRequires:  meson
BuildRequires:	hyprlang
BuildRequires:	pkgconfig(hyprcursor)
BuildRequires:	pkgconfig(hyprwayland-scanner) = 0.3.4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.118
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:	pkgconfig(libliftoff)
BuildRequires:  pkgconfig(libseat) >= 0.2.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:	pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.26
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xcb-errors)

Requires:	hyprcursor

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots
that doesn't sacrifice on its looks.

It supports multiple layouts, fancy effects, has a very flexible IPC
model allowing for a lot of customization, and more.

#package devel
#Summary:        Files required to build Hyprland plugins
#Requires:       %{name}

#description devel
#This package contains the neccessary files that are required to
#build plugins for hyprland.

%prep
%autosetup -n %{name}-source -p1
#patch -p1 -d subprojects/wlroots/ < subprojects/packagefiles/wlroots-meson-build.patch

%build
%meson \
	 -Dwlroots:xcb-errors=enabled
%meson_build

%install
%meson_install --tags runtime,man
# Disable devel for now
#devel
#rm %{buildroot}/%{_libdir}/libwlroots.a %{buildroot}/%{_libdir}/pkgconfig/wlroots.pc

%files
%license LICENSE
%doc README.md
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_bindir}/hyprpm
%{_datadir}/%{name}/
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/%{name}.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_datadir}/bash-completion/hyprctl
%{_datadir}/bash-completion/hyprpm
%{_datadir}/fish/vendor_completions.d/hyprctl.fish
%{_datadir}/fish/vendor_completions.d/hyprpm.fish
%{_datadir}/zsh/site-functions/_hyprctl
%{_datadir}/zsh/site-functions/_hyprpm
%{_mandir}/man1/Hyprland.*
%{_mandir}/man1/hyprctl.*

#files devel
#{_includedir}/%{name}
#{_includedir}/wlr/
#{_datadir}/pkgconfig/%{name}.pc
