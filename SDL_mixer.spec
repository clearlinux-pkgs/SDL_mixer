#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL_mixer
Version  : 1.2.12
Release  : 2
URL      : https://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-1.2.12.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-1.2.12.tar.gz
Summary  : Simple DirectMedia Layer - Sample Mixer Library
Group    : Development/Tools
License  : Artistic-1.0-Perl BSD-3-Clause GPL-2.0 LGPL-2.0
Requires: SDL_mixer-lib
BuildRequires : SDL-dev
BuildRequires : pkgconfig(vorbisfile)

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, SMPEG MP3, and libmad MP3 libraries.

%package dev
Summary: dev components for the SDL_mixer package.
Group: Development
Requires: SDL_mixer-lib
Provides: SDL_mixer-devel

%description dev
dev components for the SDL_mixer package.


%package lib
Summary: lib components for the SDL_mixer package.
Group: Libraries

%description lib
lib components for the SDL_mixer package.


%prep
cd ..
%setup -q -n SDL_mixer-1.2.12

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL/SDL_mixer.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
