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

createHeader("Standings")
createNavigation()

sql = "SELECT L.league_id,L.year,  St.team_id,  T.owner,T.team_name,St.wins,St.losses,St.champ,SUM(round(Sc.team_pts,2)) AS pts, SUM(round(Sc.opponent_team_pts,2)) AS opp_pts FROM  standings St,  league L,  teams T,  schedule Sc WHERE  St.league_id = L.league_id  AND St.league_id = T.league_id   AND St.league_id = Sc.league_id   AND L.league_id = T.league_id   AND L.league_id = Sc.league_id   AND T.league_id = Sc.league_id   AND St.team_id = T.team_id   AND St.team_id = Sc.team_id   AND T.team_id = Sc.team_id   AND Sc.is_playoffs = 0 GROUP BY   L.league_id,  L.year,  St.team_id,  T.owner,  T.team_name,  St.wins,  St.losses,  St.champ ORDER BY   L.year DESC  ,  St.wins DESC  ,  St.losses,  pts DESC"

print "<div id=\"tabs\">"

print "<ul>"

standings_html = ""

try:
  cur.execute(sql)

  results = cur.fetchall()

  years = []

  num = 0

  for row in results:
    league_id = row[0]
    year = row[1]
    team_id = row[2]
    owner = row[3]
    team_name = row[4]
    team_html = team_name
    wins = row[5]
    losses = row[6]
    champ = row[7]
    pts = row[8]
    opp_pts = row[9]

    if year not in years:
      if len(years) > 0:
        standings_html += "</tbody></table></div>"

      print "<li><a href=\"#tabs-" + str(year) + "\">" + str(year) + "</a></li>"

      standings_html += "<div id=tabs-" + str(year) + ">"
      years.append(year)

      standings_html += "<table class=\"w3-table w3-striped w3-bordered\">"
      standings_html += "<thead>"
      standings_html += "<tr class=w3-theme>"
      standings_html += "<th width=170></th>"
      standings_html += "<th class=w3-centered width=30>W</th>"
      standings_html += "<th class=w3-centered width=30>L</th>"
      standings_html += "<th class=w3-centered width=50>Pts</th>"
      standings_html += "<th class=w3-centered width=50>PA</th>"
      standings_html += "</tr>"
      standings_html += "</thead>"
      standings_html += "<tbody>"

    if num % 2 == 0:
      standings_html += "<tr>"
    else:
      standings_html += "<tr bgcolor=#CCCCCC>"


    standings_html += "<td width=250>"

    if champ == 1:   
      team_html = "<strong>" + team_html + " (champion)</strong>"

    standings_html += "<a href=\"schedule.py?year=" + str(year)  + "&team_id=" + str(team_id) + "\">"
    standings_html += team_html
    standings_html += "</a>"
    standings_html += "</td>"
    standings_html += "<td class=w3-centered width=30>" + str(int(wins)) + "</td>"
    standings_html += "<td class=w3-centered width=30>" + str(int(losses)) + "</td>"
    standings_html += "<td class=w3-centered width=50>" + str(pts) + "</td>"
    standings_html += "<td class=w3-centered width=50>" + str(opp_pts) + "</td>"
    standings_html += "</tr>"

    num = num + 1

  if len(years) > 0:
    standings_html += "</div>"

  print "</ul>"
  print standings_html

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

