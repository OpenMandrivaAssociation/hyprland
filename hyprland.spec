Name:           hyprland
Version:        0.47.2
Release:        4
Summary:        Dynamic tiling Wayland compositor
Group:          Hyprland
License:        BSD-3-Clause
URL:            https://hyprland.org/
Source0:        https://github.com/hyprwm/Hyprland/releases/download/v%{version}/source-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  jq
BuildRequires:  meson
BuildRequires:	hyprlang
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:	pkgconfig(hyprcursor)
BuildRequires:	pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:	pkgconfig(hyprgraphics)
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
BuildRequires:	pkgconfig(re2)
BuildRequires:	pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.26
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:	pkgconfig(aquamarine)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:	glaze-devel

Requires:	hyprcursor
Requires:	hyprgraphics
Requires:	aquamarine

Recommends:	uwsm
Recommends:	xdg-desktop-portal-hyprland
Recommends:	kitty
Recommends:     wofi
Recommends:     playerctl
Recommends:     brightnessctl
Recommends:     hyprland-qtutils
Recommends:     mesa-dri-drivers
Recommends:     polkit

%description
Hyprland is a dynamic tiling Wayland compositorthat doesn't sacrifice on its looks.

It supports multiple layouts, fancy effects, has a very flexible IPC
model allowing for a lot of customization, and more.

%prep
%autosetup -n %{name}-source -p1

rm -rf subprojects/{tracy,hyprland-protocols}
# don't run generateVersion.sh, release tarballs have pregenerated version.h
sed -i '/scripts\/generateVersion.sh/d' meson.build

%build
# This CrapLANG crashing during compilation time. I dont wana see it here anymore. Switch to GCC.
# Also aquamarine compiled with CrapLANG crashing at runtime. What a shitty compiler.
export CC=gcc
export CXX=g++
%meson \
	 -Dwlroots:xcb-errors=enabled
%meson_build

%install
%meson_install --tags runtime,man

%files
%license LICENSE
%doc README.md
%{_bindir}/Hyprland
%{_bindir}/hyprland
%{_bindir}/hyprctl
%{_bindir}/hyprpm
%{_datadir}/hypr/hyprland.conf
%{_datadir}/hypr/wall0.png
%{_datadir}/hypr/wall1.png
%{_datadir}/hypr/wall2.png
%{_datadir}/hypr/lockdead.png
%{_datadir}/hypr/lockdead2.png
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/wayland-sessions/hyprland-uwsm.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_datadir}/bash-completion/completions/hyprctl
%{_datadir}/bash-completion/completions/hyprpm
%{_datadir}/fish/vendor_completions.d/hyprctl.fish
%{_datadir}/fish/vendor_completions.d/hyprpm.fish
%{_datadir}/zsh/site-functions/_hyprctl
%{_datadir}/zsh/site-functions/_hyprpm
%{_mandir}/man1/Hyprland.*
%{_mandir}/man1/hyprctl.*
