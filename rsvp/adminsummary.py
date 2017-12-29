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

rsvp = {}
rsvp[0]="<strong><font color=red>NO</font></strong>"
rsvp[1]="<strong><font color=lawngreen>YES</font></strong>"
rsvp[-1]="<strong><font color=lightgray>N/A</font></strong>"



try:
  
  sql = "select e.name,g.tags,r.rsvp,sum(attending) from user u,rsvp r,guest g,event e,event_guest eg where u.user_id=1 and u.user_id=r.user_id and r.guest_id=g.guest_id and r.guest_id=eg.guest_id and e.event_id=eg.event_id group by r.rsvp desc,g.tags,e.name"
  cur.execute(sql)
  results = cur.fetchall()

  print "<br>"

  print "<div>"

  print "<table id=stats class=\"tablesorter w3-table w3-bordered w3-striped\">"
  print "<thead>"
  print "<tr class=w3-theme>"
  print "<th class=w3-centered>Event</th>"
  print "<th class=w3-centered>Category</th>"
  print "<th class=w3-centered>RSVP</th>"
  print "<th class=w3-centered>Count</th>"
  print "</tr>"
  print "</thead>"
  print "<tbody id=\"results\">"

  for row in results:
    event = row[0]
    category = row[1]
    response = row[2]
    count = row[3]

    print "<tr>"

    print "<td>"
    print event
    print "</td>"

    print "<td>"
    print category
    print "</td>"

    print "<td>"
    print rsvp[response]
    print "</td>"

    print "<td>"
    print count
    print "</td>"

    print "</tr>"

  print "</tbody>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

