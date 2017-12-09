#!/usr/bin/python

import cgi
import MySQLdb
import Cookie
import credentials
from utilities import *
from sets import Set
import sys
import uuid

host = credentials.getHost()
user = credentials.getUser()
passwd = credentials.getPasswd()
dbname = credentials.getDB()

fields = cgi.FieldStorage()

db = MySQLdb.Connection(host,
                user,
                passwd,
                dbname)

cur = db.cursor()


cookie = Cookie.SimpleCookie()
cookie["session"] = uuid.uuid4()
cookie["session"]["domain"] = ".sidburgh.com"
cookie["session"]["path"] = "/"
cookie["session"]["max-age"] = 3600

try:
  sql = "update user set session_id = '%s' where user_id = 1" % str(cookie["session"].value)

  cur.execute(sql)
  db.commit()
except:
  print
finally:
  db.close()

print "Content-Type: text/html"
print cookie.output()
print
print "<html>"
print "<head>"
print "<meta http-equiv=\"Refresh\" content=\"0;url=http://www.sidburgh.com/rsvp/adminrsvp.py\">"
print "</head>"
print "<body>"
print "</body>"
print "</html>"

