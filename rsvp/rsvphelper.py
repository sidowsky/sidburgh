#!/usr/bin/python

import cgi
import MySQLdb
import credentials
from utilities import *
from sets import Set
import sys
from email.mime.text import MIMEText
import traceback
from subprocess import Popen,PIPE

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
rsvp = fields.getvalue('rsvp')
attending = fields.getvalue('attending')
notes = fields.getvalue('notes')

sql = "update rsvp set rsvp = " + str(rsvp) + ", attending = " + str(attending)  + ", notes = '" + notes + "', rsvp_time=NOW() where user_id = " + user + " and guest_id = " + guest


print "Content-Type: text/html"
print
print "<html lang=\"en\">"
print "<head>"
print "</head>"
print "<body>"


try:
  cur.execute(sql)
  db.commit()

  print "<p>Thanks for your RSVP!</p>"


  sql = "select u.email,g.first,g.last from user u, guest g where u.user_id=g.user_id and u.user_id=" + str(user) + " and g.guest_id=" + str(guest)

  cur.execute(sql)
  results = cur.fetchall()

  for row in results:
    email = row[0]
    first = row[1]
    last = row[2]

    msg = MIMEText("Attending: " + attending + "\n\n" + notes)
    msg['Subject'] = "New RSVP - " + first + " " + last + " [" + ("YES" if rsvp == "1" else "NO")  +  "]"
    msg['To'] = email
    msg['From'] = 'admin@sidburgh.com'

    p = Popen(['/usr/sbin/sendmail', '-t', '-oi'], stdin=PIPE)
    p.communicate(msg.as_string())

except:
  print "<h3>Error</h3>"
  print traceback.print_exc()

finally:
  db.close()

print "</body>"
print "</html>"  


createFooter()

