#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE8BCD7866AFCF978 (nicolas@petton.fr)
#
Name     : emacs-x11
Version  : 27.1
Release  : 43
URL      : https://mirrors.kernel.org/gnu/emacs/emacs-27.1.tar.xz
Source0  : https://mirrors.kernel.org/gnu/emacs/emacs-27.1.tar.xz
Source1  : https://mirrors.kernel.org/gnu/emacs/emacs-27.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: emacs-x11-bin = %{version}-%{release}
Requires: emacs-x11-data = %{version}-%{release}
Requires: emacs-x11-license = %{version}-%{release}
Requires: emacs = %{version}
BuildRequires : ImageMagick-dev
BuildRequires : acl-dev
BuildRequires : alsa-lib-dev
BuildRequires : gmp-dev
BuildRequires : gnutls-dev
BuildRequires : gpm-dev
BuildRequires : gtk3-dev
BuildRequires : lcms2-dev
BuildRequires : libXfixes-dev
BuildRequires : libXinerama-dev
BuildRequires : libXrandr-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : librsvg-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(xpm)
BuildRequires : systemd-dev
BuildRequires : texinfo
BuildRequires : valgrind

%description
See the end of the file for license conditions.
This directory tree holds version 27.1 of GNU Emacs, the extensible,
customizable, self-documenting real-time display editor.

%package bin
Summary: bin components for the emacs-x11 package.
Group: Binaries
Requires: emacs-x11-data = %{version}-%{release}
Requires: emacs-x11-license = %{version}-%{release}

%description bin
bin components for the emacs-x11 package.


%package data
Summary: data components for the emacs-x11 package.
Group: Data

%description data
data components for the emacs-x11 package.


%package license
Summary: license components for the emacs-x11 package.
Group: Default

%description license
license components for the emacs-x11 package.


%prep
%setup -q -n emacs-27.1
cd %{_builddir}/emacs-27.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597159954
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --without-m17n-flt \
--without-libotf \
--without-xaw3d \
--with-xpm=yes \
--with-gif=no \
--with-tiff=no \
--with-imagemagick \
--with-modules \
--with-dumping=unexec
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1597159954
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/emacs-x11
cp %{_builddir}/emacs-27.1/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/etc/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/leim/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/lib-src/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/lib/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/lisp/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/lwlib/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/msdos/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/nt/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/emacs-27.1/src/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/ctags
rm -f %{buildroot}/usr/bin/ebrowse
rm -f %{buildroot}/usr/bin/emacsclient
rm -f %{buildroot}/usr/bin/etags
rm -f %{buildroot}/usr/bin/grep-changelog
rm -f %{buildroot}/usr/include/emacs-module.h
rm -f %{buildroot}/usr/lib64/systemd/user/emacs.service
rm -f %{buildroot}/usr/share/appdata/emacs.appdata.xml
rm -f %{buildroot}/usr/share/metainfo/emacs.appdata.xml
rm -f %{buildroot}/var/games/emacs/snake-scores
rm -f %{buildroot}/var/games/emacs/tetris-scores
## install_append content
rm -rf %{buildroot}/usr/libexec/emacs
rm -rf %{buildroot}/usr/share/emacs
rm -rf %{buildroot}/usr/share/icons
rm -rf %{buildroot}/usr/share/info
rm -rf %{buildroot}/usr/share/man
emacsbin=$(realpath -e %{buildroot}/usr/bin/emacs)
mv "$emacsbin" %{buildroot}/usr/bin/emacs-x11
rm %{buildroot}/usr/bin/emacs
sed -i 's/Exec=emacs/Exec=emacs-x11/' %{buildroot}/usr/share/applications/emacs.desktop
ln -s emacs-x11 %{buildroot}/usr/bin/xemacs
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/emacs-x11
/usr/bin/xemacs

%files data
%defattr(-,root,root,-)
/usr/share/applications/emacs.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
