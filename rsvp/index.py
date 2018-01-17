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

createHeader("Rahul & Reshma")

print "<form action=\"http://www.sidburgh.com/rsvp/address.py\" method=\"post\">"
print "<input placeholder=\"First\" type=\"text\" name=\"first\"/><br>"
print "<input placeholder=\"Last\" type=\"text\" name=\"last\"/><br>"
print "<input placeholder=\"Password\" type=\"password\" name=\"passwd\"/><br><br>"
print "<input type=\"hidden\" name=\"user\" value=\"1\"/>"
print "<input type=\"submit\" value=\"Submit\"/>"
print "</form>"



createFooter()

