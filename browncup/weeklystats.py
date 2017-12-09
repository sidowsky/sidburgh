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
week = fields.getvalue('week')
year = fields.getvalue('year')

print "Content-Type: text/html"
print
print "<html lang=\"en\">"
print "<head>"
print "</head>"
print "<body>"

print "<table class=\"w3-table w3-striped w3-bordered\" style=\"font-size: 10px;\">"
print "</tr>"
print "<tr class=w3-theme>"
print "<th>"+str(year)+"</th><th>Week "+str(week)+"</th><th></th>"
print "</th>"
print "</tr>"

sql = "select T.team_name, P.position, P.name, G.points, G.active from player P, game_stats_new G, teams T, league L where L.league_id=T.league_id and L.league_id=G.league_id and P.league_id = G.league_id and G.league_id = T.league_id and G.team_id = T.team_id and G.player_id = P.player_id and G.week=" + str(week) +  " and L.year = " + str(year) + " and G.team_id <> -1 order by field(position,'QB','RB','WR','TE','K','DEF'), points DESC"

maximum = {'QB': 3, 'RB': 5, 'WR' : 5, 'TE' : 3, 'K' : 2, 'DEF' : 2}

try:
  cur.execute(sql)

  results = cur.fetchall()

  count = 0
  curr_pos = None


  for row in results:
    team = str(row[0])
    pos = str(row[1])
    name = str(row[2])
    points = str(row[3])
    active = row[4]

    if pos in maximum and pos <> curr_pos:
      print "<tr class=w3-theme>"
      print "<th>"+pos+"</th><th>Team</th><th>Points</th>"
      print "</th>"
      print "</tr>"
      count = 0
      curr_pos = pos

    if pos not in maximum or count == maximum[pos]:
      continue

    count = count + 1

    if active == 0:
      name = "<strike>"+name+"</strike>"
      points = "<strike>"+points+"</strike>"

    print "<tr>"
    print "<td class=w3-centered>" + name  + "</td>"
    print "<td class=w3-centered>" + team  + "</td>"
    print "<td class=w3-centered>" + points  + "</td>"
    print "</tr>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()

print "</table>"
print "</body>"
print "</html>"

