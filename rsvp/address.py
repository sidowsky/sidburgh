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

createHeader("Enter Address")
createScript("address.js")

fields = cgi.FieldStorage()
passwd = fields.getvalue('passwd')
first = fields.getvalue('first')
last = fields.getvalue('last')
user = fields.getvalue('user')

if not credentials.authenticateUser(cur, passwd, user,False):
  db.close()
  sys.exit()

sql = "select g.* from user u,guest g where g.user_id=u.user_id and u.user_id=" + str(user) + " and ((g.first = '" + str(first) + "' and g.last = '" + str(last) + "') or (g.first2 = '" + str(first) + "' and g.last2 = '" + str(last) + "'))"

try:
  cur.execute(sql)

  results = cur.fetchall()

  for row in results:
    user_id = row[0]
    guest_id = row[1]
    first  = str(row[2])
    last  = str(row[3])
    first2  = str(row[4])
    last2  = str(row[5])
    address = str(row[6])
    address2 = str(row[7])
    city = str(row[8])
    state = str(row[9])
    post = str(row[10])
    country = str(row[11])
    email = str(row[12])
    guests = row[13]

    if first2 != "" and last2 != "":
      print "<h3 class=rsvp>Welcome, " + first + " " + last + " & " + first2 + " " + last2 + "!</h3>"
    else:
      print "<h3 class=rsvp>Welcome, " + first + " " + last + "!</h3>"
    

    print "<br>"
    print "<div id=\"results\">"
    print "Enter Mailing Address:"
    print "<br>"
    #print "<textarea id=\"address\" col=80 rows=6>" + address  +  "</textarea>"
    print "<input placeholder=\"Street Address\" type=\"text\" id=\"street1\" size=40 maxlength=40 value=\"%s\"/>" % address
    print "<br>"
    print "<input placeholder=\"\" type=\"text\" id=\"street2\" size=40 maxlength=40 value=\"%s\"/>" % address2
    print "<br>"
    print "<br>"
    print "<input placeholder=\"City\" type=\"text\" id=\"city\" size=40 maxlength=40 value=\"%s\"/>" % city
    print "<br>"
    print "<input placeholder=\"State/Territory\" type=\"text\" id=\"state\" size=40 maxlength=40 value=\"%s\"/>" % state
    print "<br>"
    print "<br>"
    print "<input placeholder=\"Postcode\" type=\"text\" id=\"post\" size=20 maxlength=20 value=\"%s\"/>" % post
    print "<br>"
    print "<input placeholder=\"Country\" type=\"text\" id=\"country\" size=20 maxlength=20 value=\"%s\"/>" % country
    print "<br>"
    print "<br>"
    print "<input type=\"hidden\" id=\"guest\" value=\"" + str(guest_id) + "\"/>"
    print "<input type=\"hidden\" id=\"user\" value=\"" + str(user_id)  + "\"/>"
    print "<button type=\"submit\" onclick=\"updateAddress()\"/>Submit</button>"
    print "</div>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()

  


createFooter()

