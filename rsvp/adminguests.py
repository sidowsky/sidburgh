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
  print "<th class=w3-centered>Email</th>"
  print "<th class=w3-centered>Address</th>"
  print "<th class=w3-centered>Address2</th>"
  print "<th class=w3-centered>City</th>"
  print "<th class=w3-centered>State</th>"
  print "<th class=w3-centered>Post</th>"
  print "<th class=w3-centered>Country</th>"
  print "<th class=w3-centered>Max</th>"
  print "<th class=w3-centered>Category</th>"
  print "</tr>"
  print "</thead>"
  print "<tbody>"

  sql = "SELECT * from guest where user_id=1 order by tags,last,first"
  cur.execute(sql)
  results = cur.fetchall()

  for row in results:
    guest_id = row[1]
    first = row[2]
    last = row[3]
    first2 = row[4]
    last2 = row[5]
    address = row[6]
    address2 = row[7]
    city = row[8]
    state = row[9]
    post = row[10]
    country = row[11]
    email = row[12]
    max_guests = row[13]
    category = row[14]

    print "<tr>"
    print "<td id=\"results_%s\">" % guest_id
    print "</td>"

    print "<td>"
    print "<a onclick=\"saveGuest(\'%s\')\">" % guest_id
    print "<i class=\"fa fa-save\" style=\"font-size:24px;color:black\"></i>"
    print "</a>"
    #print "<input type=submit value=\"Save\" onclick=\"saveGuest(\'%s\')\"/>" % guest_id
    print "</td>"

    print "<td class=g contenteditable=true id=\"first_%s\">" % guest_id
    print first
    print "</td>"

    print "<td class=g contenteditable=true id=\"last_%s\">" % guest_id
    print last
    print "</td>"

    print "<td class=g contenteditable=true id=\"first2_%s\">" % guest_id
    print first2
    print "</td>"

    print "<td class=g contenteditable=true id=\"last2_%s\">" % guest_id
    print last2
    print "</td>"

    print "<td class=g contenteditable=true id=\"email_%s\">" % guest_id
    print email
    print "</td>"

    print "<td class=ga contenteditable=true id=\"address_%s\">" % guest_id
    print address
    print "</td>"

    print "<td class=ga contenteditable=true id=\"address2_%s\">" % guest_id
    print address2
    print "</td>"

    print "<td class=ga contenteditable=true id=\"city_%s\">" % guest_id
    print city
    print "</td>"

    print "<td class=ga contenteditable=true id=\"state_%s\">" % guest_id
    print state
    print "</td>"

    print "<td class=ga contenteditable=true id=\"post_%s\">" % guest_id
    print post
    print "</td>"

    print "<td class=ga contenteditable=true id=\"country_%s\">" % guest_id
    print country 
    print "</td>"

    print "<td class=gm contenteditable=true id=\"max_%s\">" % guest_id
    print max_guests
    print "</td>"

    print "<td class=gc contenteditable=true id=\"tag_%s\">" % guest_id
    print category
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

