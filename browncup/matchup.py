#!/usr/bin/python

import cgi
import MySQLdb
import credentials
from utilities import *
from sets import Set

def processResults(results, team_pts):
  print "<table class=\"w3-table w3-striped w3-bordered\" style=\"font-size: 10px;\">"

  flag = 0

  for row in results:
    team_name = row[0]
    player_name = row[1]
    position = row[2]
    points = row[3]
    active = row[4]
    player_html = position + " " + player_name

    if active == 0:
      player_html = "<strike>" + player_html  + "</strike>"

    if flag == 0:
      print "<tr class=w3-theme>"
      print "<th>"
      print team_name
      print "</th><th>" + str(team_pts) + "</th>"
      print "<tbody>"
      flag = 1

    print "<tr>"
    print "<td>" + player_html + "</td>"
    print "<td>" + str(points) + "</td>"
    print "</tr>"

  print "</tbody>"
  print "</table>"
  return




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
team_id = fields.getvalue('team_id')
opponent_team_id = fields.getvalue('opponent_team_id')
week = fields.getvalue('week')
year = fields.getvalue('year')

createHeader("Matchup")
#createNavigation()

print "<table class=\"w3-table w3-striped w3-bordered\" style=\"font-size: 10px;\">"
print "<tr class=w3-theme>"
print "<th>" + str(year) + " - Week " + str(week) + "</th><th></th>"
print "</tr>"
print "<tbody>"

try:
  sql = "select team_pts, opponent_team_pts from schedule S, league L where L.league_id = S.league_id and L.year = " + str(year)  + " and S.week = " + str(week) + " and S.team_id = " + str(team_id) + " and S.opponent_team_id = " + str(opponent_team_id)

  cur.execute(sql)

  results = cur.fetchall()

  for row in results:
    pts = row[0]
    opp_pts = row[1]


  sql = "select T.team_name, P.name, P.position, G.points, G.active from league L, teams T, game_stats_new G, player P where L.league_id=T.league_id and L.league_id=G.league_id and L.league_id=P.league_id and T.team_id = G.team_id and G.player_id = P.player_id and L.year = " + str(year)  +  " and G.week = " + str(week) + " and T.team_id = " + str(team_id) + " order by active desc, points desc"

  cur.execute(sql)

  results = cur.fetchall()

  print "<tr>"
  print "<td>"

  processResults(results, pts)

  print "</td>"
  print "<td>"

  sql = "select T.team_name, P.name, P.position, G.points, G.active from league L, teams T, game_stats_new G, player P where L.league_id=T.league_id and L.league_id=G.league_id and L.league_id=P.league_id and T.team_id = G.team_id and G.player_id = P.player_id and L.year = " + str(year)  +  " and G.week = " + str(week) + " and T.team_id = " + str(opponent_team_id) + " order by active desc, points desc"

  cur.execute(sql)

  results = cur.fetchall()

  print "<table class=\"w3-table w3-striped w3-bordered\" style=\"font-size: 10px;\">"

  processResults(results, opp_pts)

  print "</td>"
  print "</tr>"

  print "</tbody>"
  print "</table>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()


