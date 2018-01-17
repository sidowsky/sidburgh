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

db = MySQLdb.Connection(host,
                user,
                passwd,
                dbname)

cur = db.cursor()

createHeader("Reshma & Rahul")

print "<br>"
print "<h3 class=faq>"
print "Please RSVP by March 30"
print "</h3>"

print "<form action=\"http://www.sidburgh.com/rsvp/rsvp.py\" method=\"post\">"
print "<input type=\"text\" placeholder=\"First\" name=\"first\"/><br>"
print "<input type=\"text\" placeholder=\"Last\" name=\"last\"/><br>"
print "<input type=\"password\" placeholder=\"Password\" name=\"passwd\"/><br>"
print "<input type=\"hidden\" name=\"user\" value=\"1\"/>"
print "<br>"
print "<input type=\"submit\" value=\"Continue\"/>"
print "</form>"



createFooter()

