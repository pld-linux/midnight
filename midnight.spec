Summary:	Midi/Karaoke player
Summary(pl):	Odtwarzacz Midi/Karaoke
Name:		midnight
Version:	0.9.6
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://midnight.linuxbox.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-time_h.patch
URL:		http://midnight.linuxbox.com
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

%build
./configure --prefix=%{_prefix} --with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/midnight
%attr(755,root,root) %{_bindir}/xmidnight
