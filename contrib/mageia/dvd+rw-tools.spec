%define git_repo dvd+rw-tools
%define git_head HEAD


Summary:	Tools for burning on DVD+RW compliant burner
Group:          Archiving/Cd burning
Name:		dvd+rw-tools
Version:	%git_get_ver
Release:	%mkrel %git_get_rel2
License:	GPLv2
Source:		%git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
# (fc) use genisoimage, not mkisofs by default (SUSE)
# fix build with gcc 4.3
# (fc) Allow burn small images on DVD-DL (Fedora bug #476154)
# (fc) fix widechar overflow (Fedora bug #426068)
# (fc) fix exit status of dvd+rw-format (Fedora bug #243036)
# (fc) use rpm_opt_flags (SUSE)
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	cdrkit-genisoimage

%description
Even though a modified kernel can let you put for example an ext2 file
system on DVD+RW, it's probably not very practical, because you most
likely want to access the data on an arbitrary computer. Or in other
words you most likely want ISO9660. The trouble is that you might as
well want to add data now and then. And what options do you have in
the lack of multiple sessions (no, DVD+RW has no notion of multiple
sessions)? Complete re-mastering which takes more and more time as
data set grows? Well, yes, unless you employ growisofs! Growisofs
provides the way to both lay down and grow an ISO9660 file system on
(as well as to burn an arbitrary pre-mastered image to) all supported
optical media.

%prep

%git_get_source
%setup -q

%build

%make LDFLAGS="%{ldflags}"
%make rpl8 btcflash LDFLAGS="%{ldflags}"

%install

make install prefix=$RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -m755 rpl8 $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root) 
%doc index.html
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/*



