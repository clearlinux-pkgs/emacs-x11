#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xE78DAE0F3115E06B (eliz@gnu.org)
#
Name     : emacs-x11
Version  : 29.0.92
Release  : 55
URL      : https://alpha.gnu.org/gnu/emacs/pretest/emacs-29.0.92.tar.xz
Source0  : https://alpha.gnu.org/gnu/emacs/pretest/emacs-29.0.92.tar.xz
Source1  : https://alpha.gnu.org/gnu/emacs/pretest/emacs-29.0.92.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: emacs-x11-bin = %{version}-%{release}
Requires: emacs-x11-data = %{version}-%{release}
Requires: emacs-x11-libexec = %{version}-%{release}
Requires: emacs-x11-license = %{version}-%{release}
Requires: emacs = %{version}
BuildRequires : ImageMagick-dev
BuildRequires : acl-dev
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-configure
BuildRequires : gmp-dev
BuildRequires : gnutls-dev
BuildRequires : gpm-dev
BuildRequires : gtk3-dev
BuildRequires : jansson-dev
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
BuildRequires : sqlite-autoconf-dev
BuildRequires : systemd-dev
BuildRequires : texinfo
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Rename-the-pdump-file.patch

%description
See the end of the file for license conditions.
This directory tree holds version 29.0.92 of GNU Emacs, the extensible,
customizable, self-documenting real-time display editor.

%package bin
Summary: bin components for the emacs-x11 package.
Group: Binaries
Requires: emacs-x11-data = %{version}-%{release}
Requires: emacs-x11-libexec = %{version}-%{release}
Requires: emacs-x11-license = %{version}-%{release}

%description bin
bin components for the emacs-x11 package.


%package data
Summary: data components for the emacs-x11 package.
Group: Data

%description data
data components for the emacs-x11 package.


%package libexec
Summary: libexec components for the emacs-x11 package.
Group: Default
Requires: emacs-x11-license = %{version}-%{release}

%description libexec
libexec components for the emacs-x11 package.


%package license
Summary: license components for the emacs-x11 package.
Group: Default

%description license
license components for the emacs-x11 package.


%prep
%setup -q -n emacs-29.0.92
cd %{_builddir}/emacs-29.0.92
%patch -P 1 -p1
pushd ..
cp -a emacs-29.0.92 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688064117
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --without-m17n-flt \
--without-libotf \
--without-xaw3d \
--with-xpm=yes \
--with-gif=no \
--with-tiff=no \
--with-imagemagick \
--with-modules \
--enable-link-time-optimization \
--with-cairo
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --without-m17n-flt \
--without-libotf \
--without-xaw3d \
--with-xpm=yes \
--with-gif=no \
--with-tiff=no \
--with-imagemagick \
--with-modules \
--enable-link-time-optimization \
--with-cairo
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1688064117
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/emacs-x11
cp %{_builddir}/emacs-%{version}/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/etc/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/leim/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/lib-src/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/lib/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/lisp/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/lwlib/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/msdos/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/nt/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/emacs-%{version}/src/COPYING %{buildroot}/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/ctags
rm -f %{buildroot}*/usr/bin/ebrowse
rm -f %{buildroot}*/usr/bin/emacsclient
rm -f %{buildroot}*/usr/bin/etags
rm -f %{buildroot}*/usr/bin/grep-changelog
rm -f %{buildroot}*/usr/include/emacs-module.h
rm -f %{buildroot}*/usr/lib64/systemd/user/emacs.service
rm -f %{buildroot}*/usr/share/appdata/emacs.appdata.xml
rm -f %{buildroot}*/usr/share/metainfo/emacs.appdata.xml
rm -f %{buildroot}*/var/games/emacs/snake-scores
rm -f %{buildroot}*/var/games/emacs/tetris-scores
rm -f %{buildroot}*/usr/share/metainfo/emacs.metainfo.xml
## install_append content
# pdmp files are required for emacs operation
find %{buildroot}/usr/libexec/emacs -type f ! -name '*.pdmp' -delete
find %{buildroot}/usr/libexec/emacs -type l -delete
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/emacs-29.0.92
/usr/bin/emacs-x11
/usr/bin/xemacs

%files data
%defattr(-,root,root,-)
/usr/share/applications/emacs-mail.desktop
/usr/share/applications/emacs.desktop
/usr/share/applications/emacsclient-mail.desktop
/usr/share/applications/emacsclient.desktop

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/emacs/29.0.92/x86_64-generic-linux-gnu/hexl
/V3/usr/libexec/emacs/29.0.92/x86_64-generic-linux-gnu/movemail
/usr/libexec/emacs/29.0.92/x86_64-generic-linux-gnu/emacs-x11-.pdmp

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/emacs-x11/31a3d460bb3c7d98845187c716a30db81c44b615
