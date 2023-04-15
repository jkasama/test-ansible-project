#!/usr/bin/python3

import testinfra

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

def test_httpd_is_installed(host):
    httpd = host.package("httpd")
    assert httpd.is_installed
    assert httpd.version.startswith("2.4")

def test_httpd_is_running(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled


