%define name                    dvd+rw-tools
%define version			7.1
%define release                 %mkrel 7

Summary:	Tools for burning on DVD+RW compliant burner
Group:          Archiving/Cd burning
Name: 		%{name}
Version:	%{version}
Release:        %{release}
License:	GPLv2
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.gz
Source1:	dvd+rw-mediainfo.1
# (fc) use genisoimage, not mkisofs by default (SUSE)
Patch0:		growisofs-genisoimage.patch
# fix build with gcc 4.3
Patch2:		dvd+rw-tools-limits.h_fix.diff
# (fc) Allow burn small images on DVD-DL (Fedora bug #476154)
Patch3:		dvd+rw-tools-7.0-dvddl.patch
# (fc) fix widechar overflow (Fedora bug #426068)
Patch4:		dvd+rw-tools-7.0-wctomb.patch
# (fc) fix exit status of dvd+rw-format (Fedora bug #243036)
Patch5:		dvd+rw-tools-7.0-wexit.patch
# (fc) use rpm_opt_flags (SUSE)
Patch6:		rpm_opt_flags.diff
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

%setup -q
%patch0 -p1 -b .genisoimage
%patch2 -p1 -b .limits
%patch3 -p1 -b .dvddl
%patch4 -p1 -b .wctomb
%patch5 -p1 -b .wexit
%patch6 -p1 -b .rpm_opt_flags

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



