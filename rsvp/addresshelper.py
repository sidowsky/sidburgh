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

fields = cgi.FieldStorage()
user = fields.getvalue('user')
guest = fields.getvalue('guest')
address = fields.getvalue('address')

sql = "update guest set address = '" + str(address) + "' where user_id = " + user + " and guest_id = " + guest


print "Content-Type: text/html"
print
print "<html lang=\"en\">"
print "<head>"
print "</head>"
print "<body>"


try:
  cur.execute(sql)


  sql = "select * from rsvp where user_id = " + user + " and guest_id = " + guest
  cur.execute(sql)

  if cur.rowcount == 0:
    sql = "insert ignore into rsvp (user_id,guest_id,rsvp,attending,notes) values (" + str(user) + "," + str(guest) + ",-1,0,'')"
    cur.execute(sql)

  db.commit()

  print "<p>Saved!</p>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()

print "</body>"
print "</html>"  


createFooter()

