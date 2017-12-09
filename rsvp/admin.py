#!/usr/bin/python

import cgi
import MySQLdb
import credentials
from utilities import *
from sets import Set
import sys

host = credentials.getHost()
user = credentials.getUser()
passwd = credentials.getPasswd()
dbname = credentials.getDB()

createHeader("ADMIN: Rahul & Reshma")

fields = cgi.FieldStorage()

print "<form action=\"http://www.sidburgh.com/rsvp/adminhome.py\" method=\"post\">"
print "Password: <input type=\"password\" name=\"passwd\"/><br>"
print "<input type=\"hidden\" name=\"user\" value=\"1\"/>"
print "</form>"
