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

createHeader("ADMIN: Rahul & Reshma",True)
createNavigation()

createScript("adminguests.js")

try:
  
  print "<div>"
  print "<br>"

  print "<table id=stats class=\"tablesorter w3-table w3-bordered w3-striped\">"
  print "<thead>"
  print "<tr class=w3-theme>"
  print "<th class=w3-centered></th>"
  print "<th class=w3-centered></th>"
  print "<th class=w3-centered>First</th>"
  print "<th class=w3-centered>Last</th>"
  print "<th class=w3-centered>First</th>"
  print "<th class=w3-centered>Last</th>"
  print "<th class=w3-centered>Address</th>"
  print "<th class=w3-centered>Email</th>"
  print "<th class=w3-centered>Max</th>"
  print "<th class=w3-centered>Category</th>"
  print "</tr>"
  print "</thead>"
  print "<tbody>"

  sql = "SELECT * from guest where user_id=1"
  cur.execute(sql)
  results = cur.fetchall()

  for row in results:
    guest_id = row[1]
    first = row[2]
    last = row[3]
    first2 = row[4]
    last2 = row[5]
    address = row[6]
    email = row[7]
    max_guests = row[8]
    category = row[9]

    print "<tr>"
    print "<td id=\"results_%s\">" % guest_id
    print "</td>"

    print "<td>"
    print "<a href=\"#\" onclick=\"saveGuest(\'%s\')\">" % guest_id
    print "<i class=\"fa fa-save\" style=\"font-size:24px;color:white\"></i>"
    print "</a>"
    #print "<input type=submit value=\"Save\" onclick=\"saveGuest(\'%s\')\"/>" % guest_id
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=15 size=10 id=\"first_%s\" value=%s>" % (guest_id, first)
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=15 size=10 id=\"last_%s\" value=%s>" % (guest_id, last)
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=15 size=10 id=\"first2_%s\" value=%s>" % (guest_id, first2)
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=15 size=10 id=\"last2_%s\" value=%s>" % (guest_id, last2)
    print "</td>"

    print "<td>"
    print "<textarea cols=25 rows=3 id=\"address_%s\">%s</textarea>" % (guest_id, address)
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=30 size=25 id=\"email_%s\" value=%s>" % (guest_id, email)
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=2 size=2 id=\"max_%s\" value=%s>" % (guest_id, max_guests)
    print "</td>"

    print "<td>"
    print "<input style=\"font-size: 12px\" type=text maxlength=10 size=10 id=\"tag_%s\" value=%s>" % (guest_id, category)
    print "</td>"


    print "</tr>"

  print "</tbody>"

  print "</div>"

  print "<div id=\"dialog\"></div>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

