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

createScript("adminrsvp.js")

print "<div>"



try:
  
  sql = "SELECT name from event where user_id=1"
  cur.execute(sql)
  results = cur.fetchall()

  print "<fieldset>"
  print "<legend>Event</legend>"

  for row in results:
    event = row[0]
    print "<label for=\"radio-" + str(event) + "\">" + str(event)  + "</label>"
    print "<input type=\"radio\" name=\"radio-event\" id=\"radio-" + str(event) + "\" value=\"" + str(event) + "\" onclick=getStats()>"


  print "</fieldset>"
  print "<br>"
  print "<fieldset>"
  print "<legend>Category</legend>"

  sql = "SELECT distinct(tags) from guest where user_id = 1"
  cur.execute(sql)
  results = cur.fetchall()

  for row in results:
    tag = row[0]
    print "<label for=\"radio-" + str(tag) + "\">" + str(tag)  + "</label>"
    print "<input type=\"radio\" name=\"radio-tag\" id=\"radio-" + str(tag) + "\" value=\"" + str(tag) + "\" onclick=getStats()>"

  print "<label for=\"radio-all\">ALL</label>"
  print "<input type=\"radio\" name=\"radio-tag\" id=\"radio-all\" value=\"ALL\" onclick=getStats()>"

  print "</fieldset>"
  print "</div>"

  print "<br>"

  print "<div>"

  print "<table id=stats class=\"tablesorter w3-table w3-bordered w3-striped\">"
  print "<thead>"
  print "<tr class=w3-theme>"
  print "<th class=w3-centered>First</th>"
  print "<th class=w3-centered>Last</th>"
  print "<th class=w3-centered>Other</th>"
  print "<th class=w3-centered>Email</th>"
  print "<th class=w3-centered>RSVP</th>"
  print "<th class=w3-centered>Count</th>"
  print "<th class=w3-centered>Address</th>"
  print "</tr>"
  print "</thead>"
  print "<tbody id=\"results\">"
  print "</tbody>"

  print "</div>"

  print "<div id=\"dialog\"></div>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

