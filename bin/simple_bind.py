#!/usr/bin/env python

import ldap

l = ldap.initialize('ldap://ldap1.example.com:1389')
l.protocol_version = ldap.VERSION3	
	
username = "uid=sjj,ou=People,dc=example,dc=com"
password  = "newpass"

try:
  l.simple_bind_s(username, password)
except ldap.LDAPError, e:
  print e

l.unbind_s()

