Name: petit
Summary: Log analysis tool for syslog, apache and raw log files
Version: 1
Release: e1
License: GPL
Group: Applications/System
URL: http://www.eyemg.com/opensource
Source0: petit.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}       
BuildArch: i386                                            
Autoreq: 0                                                 
Requires: python

%description
Log analysis tool which is useful to systems administrators & systems analysts
This tool interact with syslog and apache logs to clarify what is happening in logs.

%prep
echo Building %{name}-%{version}-%{release}

#%setup -q -n %{name}-%{version}

%build
tar xvfz %{SOURCE0}

%install
# Remove old BUILD ROOT
rm -rf ${RPM_BUILD_ROOT}
install -d ${RPM_BUILD_ROOT}/usr/bin
install src/bin/petit ${RPM_BUILD_ROOT}/usr/bin/petit

%clean
#rm -fr $RPM_BUILD_ROOT


%files
/usr/bin/petit

%defattr(-,root,root,-)

%changelog
* Tue Jul 31 2009 Scott McCarty <smccarty@eyemg.com>
- First working version