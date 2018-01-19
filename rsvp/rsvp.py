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

createHeader("RSVP")
createScript("rsvp.js")

fields = cgi.FieldStorage()
passwd = fields.getvalue('passwd')
first = fields.getvalue('first')
last = fields.getvalue('last')
user = fields.getvalue('user')

if not credentials.authenticateUser(cur, passwd, user, False):
  db.close()
  sys.exit()

try:
  sql = "select g.*,e.* from user u,guest g,event e,event_guest eg where g.user_id=u.user_id and g.user_id=e.user_id and g.guest_id=eg.guest_id and e.event_id=eg.event_id and u.user_id=" + str(user) + " and ((g.first = '" + str(first) + "' and g.last = '" + str(last) + "') or (g.first2 = '" + str(first) + "' and g.last2 = '" + str(last) + "'))"

  cur.execute(sql)

  results = cur.fetchall()

  flag = 0

  for row in results:
    user_id = row[0]
    guest_id = row[1]
    first  = str(row[2])
    last  = str(row[3])
    first2  = str(row[4])
    last2  = str(row[5])
    address = str(row[6])
    email = str(row[7])
    guests = row[8]
    event = row[14]
    location = row[15]
    date = row[16] 

    if flag == 0:
      if first2 != "" and last2 != "":
        print "<h3 class=rsvp>Welcome, " + first + " " + last + " & " + first2 + " " + last2 + "!</h4>"
      else:
        print "<h3 class=rsvp>Welcome, " + first + " " + last + "!</h4>"
    
      flag = 1

    print "<br>"
    print "<h4 class=rsvp>"
    print event
    print "</h4>"

    print "<p class=rsvp>"
    print str(date.strftime("%A, %B %d, %Y %I:%M %p"))
    print "<br>"
    print location.replace("\n","<br>")
    print "</p>"

  print "<br>"
  print "<div id=\"results\">"
  print "RSVP:"
  print "<select id=\"rsvp\">"
  print "<option>YES</option>"
  print "<option>NO</option>"
  print "</select>"

  print "<select id=\"attending\">"

  for x in range(1,guests+1):
    print "<option>" + str(x)  + "</option>"

  print "</select>"


  print "<br>"
  print "<br>"
  print "<textarea id=\"notes\" placeholder=\"Notes\" maxlength=280 col=80 rows=4></textarea>"




  print "<br>"
  print "<br>"

  print "<input type=\"hidden\" id=\"guest\" value=\"" + str(guest_id) + "\"/>"
  print "<input type=\"hidden\" id=\"user\" value=\"" + str(user_id)  + "\"/>"
  print "<button type=\"submit\" onclick=\"submitRSVP()\"/>RSVP</button>"

  print "</div>"
  print "<br>"
  print "<br>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()

  


createFooter()

