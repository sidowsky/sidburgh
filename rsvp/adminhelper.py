#!/usr/bin/python

import cgi
import MySQLdb
import credentials
from utilities import *
from sets import Set

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
event = fields.getvalue('event')
category = fields.getvalue('category')

print "Content-Type: text/html"
print
print "<html lang=\"en\">"
print "<head>"
print "</head>"
print "<body>"

sql = "select g.first, g.last, g.first2, g.last2, g.email, r.attending, r.rsvp, r.notes from guest g, rsvp r, event e, event_guest eg where e.user_id = r.user_id and e.user_id=g.user_id and e.user_id=eg.user_id and eg.event_id=e.event_id and eg.guest_id=g.guest_id and r.guest_id=g.guest_id and g.tags='" + str(category)  +"' and e.name='" + str(event) + "' order by r.rsvp desc, g.last"

if category == 'ALL':
  sql = "select g.first, g.last, g.first2, g.last2, g.email, r.attending, r.rsvp, r.notes from guest g, rsvp r, event e, event_guest eg where e.user_id = r.user_id and e.user_id=g.user_id and e.user_id=eg.user_id and eg.event_id=e.event_id and eg.guest_id=g.guest_id and r.guest_id=g.guest_id and e.name='" + str(event) + "' order by r.rsvp desc, g.last"

try:
  cur.execute(sql)

  results = cur.fetchall()

  for row in results:
    first = row[0]
    last = row[1]
    first2 = row[2]
    last2 = row[3]
    email = row[4]
    attending = row[5]
    rsvp = row[6]
    notes = row[7]

    print "<tr>"
    print "<td>"
    print first
    print "</td>"

    print "<td class=w3-centered>" + last  + "</td>"

    '''if first2 != "" and last2 != "":
      print "<td class=w3-centered>" + first2 + " " + last2  + "</td>"
    else:
      print "<td class=w3-centered></td>"

    print "<td class=w3-centered>" + email  + "</td>"'''

    if rsvp == -1:
      print "<td class=w3-centered><strong><font color=blue>N/A</font></strong></td>"
    elif rsvp == 0:
      print "<td class=w3-centered><strong><font color=red>NO</font></strong></td>"
    elif rsvp == 1:
      print "<td class=w3-centered><strong><font color=green>YES</font></strong></td>"

    print "<td class=w3-centered>" + str(attending)  + "</td>"

    #if address != "":
      #url = "https://www.google.com/maps/place/" + address.replace("\n"," ").replace(" ", "+")
      #print "<td class=w3-centered><a target=\"_blank\" href=\"" + url + "\">" + address  + "</a></td>"
    #else:
    print "<td class=w3-centered>" + notes.replace("\n","<br>")  + "</td>"

    print "</tr>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()


print "</body>"
print "</html>"

