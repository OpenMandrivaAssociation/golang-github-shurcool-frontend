# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/frontend
%global commit          e6633c2dc9c5d0f64511d5f12b86b0a331ef6cad

%global common_description %{expand:
Common frontend code.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Common frontend code
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gopherjs/gopherjs/js)
BuildRequires: golang(github.com/shurcooL/component)
BuildRequires: golang(github.com/shurcooL/go/gopherjs_http)
BuildRequires: golang(github.com/shurcooL/go/gopherjs_http/jsutil)
BuildRequires: golang(github.com/shurcooL/home/component)
BuildRequires: golang(github.com/shurcooL/htmlg)
BuildRequires: golang(github.com/shurcooL/httpfs/httputil)
BuildRequires: golang(github.com/shurcooL/httpfs/vfsutil)
BuildRequires: golang(github.com/shurcooL/reactions)
BuildRequires: golang(github.com/shurcooL/reactions/component)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gite6633c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gite6633c2
- First package for Fedora

