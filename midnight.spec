Summary:	Midi/Karaoke player
Summary(pl.UTF-8):   Odtwarzacz Midi/Karaoke
Name:		midnight
Version:	0.9.6
Release:	2
License:	GPL
Group:		Applications/Sound
#Source0:	http://midnight.linuxbox.com/%{name}-%{version}.tar.gz
Source0:	http://tucowslinux.tiscali.dk/files/x11/media/%{name}-%{version}.tar.gz
# Source0-md5:	59a3a3a70b60ffa68d513182f05db472
Patch0:		%{name}-time_h.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://midnight.linuxbox.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midnight is a midi player with karaoke capabilities. While it plays
midi as any midi player does, karaoke-enhanced midi files (often
suffixed with .kar instead of .mid) are automatically recognized, and
the lyrics are displayed in a visual eye-candy panel. Midnight
features a highly configurable karaoke panel, automagical charset
conversion, midi device selection at runtime, etc.

%description -l pl.UTF-8
Midnight to odtwarzacz midi z możliwościami karaoke. Oprócz odtwarzania
plików midi jak każdy inny odtwarzacz midi, pliki midi z rozszerzeniem
karaoke (zazwyczaj z rozszerzeniem .kar zamiast .mid) są automatycznie
rozpoznawane i teksty są wyświetlane na panelu. Midnight ma wysoko
konfigurowalny panel karaoke, automatyczną konwersję zestawów znaków,
ustawianie urządzenia midi itp.

%prep
%setup -q
%patch0
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO examples
%attr(755,root,root) %{_bindir}/*
