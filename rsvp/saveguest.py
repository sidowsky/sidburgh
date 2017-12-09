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

fields = cgi.FieldStorage()

db = MySQLdb.Connection(host,
                user,
                passwd,
                dbname)

cur = db.cursor()

credentials.authenticate(db,cur)

fields = cgi.FieldStorage()

guest_id = fields.getvalue('id')
first = fields.getvalue('name')
last = fields.getvalue('last')
first2 = fields.getvalue('first2') if fields.getvalue('first2') is not None else ''
last2 = fields.getvalue('last2') if fields.getvalue('last2') is not None else ''
address = fields.getvalue('address') if fields.getvalue('address') is not None else ''
email = fields.getvalue('email')
max_guests = fields.getvalue('max')
tag = fields.getvalue('tag')


try:
  sql = "update guest set first = '%s', last = '%s', first2 = '%s', last2 = '%s', address = '%s', email = '%s', max_guests = %s, tags = '%s' where guest_id = %s" % (first, last, first2, last2, address, email, max_guests, tag, guest_id)
  cur.execute(sql)
  db.commit()

  print "Content-Type: text/html"
  print
  #print "<html><body>%s</body></html>" % sql
  print "<i class=\"fa fa-check-circle\" style=\"font-size:24px;color:lime\"></i>"

except:
  print "Content-Type: text/html"
  print
  print "<i class=\"fa fa-times-circle\" style=\"font-size:24px;color:red\"></i>"

finally:
  db.close()

