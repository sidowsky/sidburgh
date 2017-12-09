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
owner = fields.getvalue('owner')
owner2 = fields.getvalue('owner2')

createHeader("Matchup History")
#createNavigation()

print "<table class=\"w3-table w3-striped w3-bordered\" style=\"font-size: 10px;\">"
print "<thead><tr class=w3-theme>"
print "<th>Year</th><th>Week</th><th></th><th></th><th></th>"
print "</tr></thead>"
print "<tbody>"

try:
  sql = "select L.year, S.week, T.team_name, S.team_pts, S.opponent_team_pts, T2.team_name, S.is_playoffs from league L, schedule S, teams T, teams T2 where L.league_id = S.league_id and L.league_id = T.league_id and L.league_id = T2.league_id and S.team_id = T.team_id and S.opponent_team_id = T2.team_id and T.owner = '" + owner  + "' and T2.owner = '" + owner2 + "' order by year desc, week desc"


  cur.execute(sql)

  results = cur.fetchall()

  for row in results:
    year = str(row[0])
    week = str(row[1])
    team_name = row[2]
    pts = row[3]
    opp_pts = row[4]
    opp_name = row[5]
    is_playoffs = row[6]

    if pts > opp_pts:
      team_name = "<strong>" + team_name + "</strong>"
    elif pts < opp_pts:
      opp_name = "<strong>" + opp_name + "</strong>"

    if is_playoffs:
      week = week + "*"

    print "<tr><td class=w3-centered>" + year + "</td><td class=w3-centered>" + week + "</td><td>" + team_name + "</td><td class=w3-centered>" + str(pts) + "-" + str(opp_pts) + "</td><td>" + opp_name  + "</td></tr>"

  print "</tbody>"
  print "</table>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()


