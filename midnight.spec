Summary:	Midi/Karaoke player
Summary(pl):	Odtwarzacz Midi/Karaoke
Name:		midnight
Version:	0.9.6
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
URL:		http://midnight.linuxbox.com/
Source0:	http://midnight.linuxbox.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-time_h.patch
Patch1:		%{name}-DESTDIR.patch
Requires:	gtk+ >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midnight midi/karaoke player

Midnight is a midi player with karaoke capabilities. While it plays
midi as any midi player does, karaoke-enhanced midi files (often
suffixed with .kar instead of .mid) are automatically recognized, and
the lyrics are displayed in a visual eye-candy panel. Midnight
features a highly configurable karaoke panel, automagical charset
conversion, midi device selection at runtime, etc.

%prep
%setup0 -q
%patch0
%patch1 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS"; export CXXFLAGS
LDFLAGS="-s"; export LDFLAGS
./configure --prefix=%{_prefix} --with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS NEWS README TODO 

%files
%defattr(644,root,root,755)
%doc BUGS.gz NEWS.gz README.gz TODO.gz examples
%attr(755,root,root) %{_bindir}/*
