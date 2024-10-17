%define rbname rcov
%define version 0.9.9
%define release %mkrel 1

Summary: Code coverage for Ruby
Name: ruby-%{rbname}
Version: %{version}
Release: %{release}
Group: Development/Ruby
License: GPLv2+ or Ruby License
URL: https://github.com/relevance/rcov
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
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
%setup -q
tar xmf data.tar.gz

%build
%gem_build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%gem_install

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/rcov
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/rcovrt.so
