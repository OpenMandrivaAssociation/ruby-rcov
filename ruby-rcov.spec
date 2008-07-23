%define rbname rcov
%define version 0.8.0.2
%define release %mkrel 3

Summary: Code coverage for Ruby
Name: ruby-%{rbname}
Version: %{version}
Release: %{release}
Group: Development/Ruby
License: GPL
URL: http://eigenclass.org/hiki.rb?rcov
Source0: %{rbname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-rake ruby-devel

%description
rcov is a tool for simple code coverage analysis in Ruby. It features:

  - fast execution: 20-300 times faster than previous tools
  - multiple analysis modes
  - fairly accurate coverage information through code linkage inference using
    simple heuristics
  - XHTML and several kinds of text reports
  - easy automation with Rake via a RcovTask
  - colorblind-friendliness

Code coverage shouldn't be abused (in few words, C0 coverage guarantees
nothing) but it's still useful for testing: it will at least tell you when your
tests need more work, and most importantly where.

%prep
%setup -q -n %{rbname}-%{version}

%build
ruby setup.rb config 
ruby setup.rb setup
RUBYLIB=$PWD/ext/rcovrt/ rake

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
ruby setup.rb install --prefix=%{buildroot}
chmod 0755 %{buildroot}%{ruby_sitearchdir}/rcovrt.so

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{ruby_sitearchdir}/rcovrt.so
%{ruby_sitelibdir}/rcov*
%{_bindir}/rcov
%doc THANKS README.* LICENSE LEGAL CHANGES test/
