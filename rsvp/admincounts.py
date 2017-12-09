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
player_id = fields.getvalue('player_id')
year = fields.getvalue('year')

print "Content-Type: text/html"
print
print "<html lang=\"en\">"
print "<head>"
print "</head>"
print "<body>"

print "<table class=\"w3-table w3-striped w3-bordered\" style=\"font-size: 10px;\">"
print "<tr class=w3-theme>"

try:
  sql = "select P.name from player P, league L where P.league_id = L.league_id and L.year=" + str(year)  +  " and P.player_id = " + str(player_id)
  cur.execute(sql)

  results = cur.fetchall()

  for row in results:
    name = row[0]
except:
  print "<h3>Error</h3>"

print "<th>" + str(year)  + "</th><th>" + name + "</th><th></th>"
print "</th>"
print "</tr>"
print "<tr class=w3-theme>"
print "<th>Week</th><th>Team</th><th>Points</th>"
print "</th>"
print "</tr>"
print "<tbody>"

sql = "select P.name, T.team_name, G.week, G.points from player P, league L, teams T, game_stats_new G where P.league_id = L.league_id and P.league_id = T.league_id and P.league_id = G.league_id and T.team_id = G.team_id and P.player_id = G.player_id and L.year=" + str(year)  +  " and P.player_id = " + str(player_id) + " and P.bye <> G.week and G.exclude = 0 order by G.week"

try:
  cur.execute(sql)

  results = cur.fetchall()


  for row in results:
    name = row[0]
    team = row[1]
    week = row[2]
    points = row[3]

    print "<tr>"
    print "<td class=w3-centered>" + str(week)  + "</td>"
    print "<td class=w3-centered>" + str(team)  + "</td>"
    print "<td class=w3-centered>" + str(points)  + "</td>"
    print "</tr>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()

print "</tbody>"
print "</table>"
print "</body>"
print "</html>"

