Summary:	Midi/Karaoke player
Summary(pl):	Odtwarzacz Midi/Karaoke
Name:		midnight
Version:	0.9.6
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://midnight.linuxbox.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-time_h.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://midnight.linuxbox.com/
BuildRequires:	gtk+-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midnight is a midi player with karaoke capabilities. While it plays
midi as any midi player does, karaoke-enhanced midi files (often
suffixed with .kar instead of .mid) are automatically recognized, and
the lyrics are displayed in a visual eye-candy panel. Midnight
features a highly configurable karaoke panel, automagical charset
conversion, midi device selection at runtime, etc.

%description -l pl
Midnight to odtwarzacz midi z mo¿liwo¶cimi karaoke. Oprócz odtwarzania
plików midi jak ka¿dy inny odtwarzacz midi, pliki midi z rozszerzeniem
karaoke (zazwyczaj z rozszerzeniem .kar zamiast .mid) s± automatycznie
rozpoznawane i teksty s± wy¶wietlane na panelu. Midnight ma wysoko
konfigurowalny panel karaoke, automatyczn± konwersjê zestawów znaków,
ustawianie urz±dzenia midi itp.

%prep
%setup -q
%patch0
%patch1 -p1

%build
%configure \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS NEWS README TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.gz NEWS.gz README.gz TODO.gz examples
%attr(755,root,root) %{_bindir}/*
