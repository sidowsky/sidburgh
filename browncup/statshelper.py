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
position = fields.getvalue('pos')
year = fields.getvalue('year')

print "Content-Type: text/html"
print
print "<html lang=\"en\">"
print "<head>"
print "</head>"
print "<body>"

sql = "select P.name, round(sum(G.points),2) as total, round(avg(G.points),2) as average, round(min(G.points),2) as minimum, round(max(G.points),2) as maximum, round(stddev(G.points),2) as stddev, count(G.points) as games, P.player_id, P.position, P.nfl_team, GROUP_CONCAT(distinct(T.team_name)) from league L, player P, game_stats_new G, teams T where L.league_id = G.league_id and L.league_id = P.league_id and L.league_id = G.league_id and L.league_id = T.league_id and G.team_id = T.team_id and P.player_id = G.player_id and G.week <> P.bye and G.exclude = 0 and L.year = " + str(year) + " and P.position = '" + position + "' group by P.name order by average desc"

if position == 'ALL':
  sql = "select P.name, round(sum(G.points),2) as total, round(avg(G.points),2) as average, round(min(G.points),2) as minimum, round(max(G.points),2) as maximum, round(stddev(G.points),2) as stddev, count(G.points) as games, P.player_id, P.position, P.nfl_team, GROUP_CONCAT(distinct(T.team_name)) from league L, player P, game_stats_new G, teams T where L.league_id = G.league_id and L.league_id = P.league_id and L.league_id = G.league_id and L.league_id = T.league_id and G.team_id = T.team_id and P.player_id = G.player_id and G.week <> P.bye and G.exclude = 0 and L.year = " + str(year) + " group by P.name order by average desc"

if position == 'FLEX':
  sql = "select P.name, round(sum(G.points),2) as total, round(avg(G.points),2) as average, round(min(G.points),2) as minimum, round(max(G.points),2) as maximum, round(stddev(G.points),2) as stddev, count(G.points) as games, P.player_id, P.position, P.nfl_team, GROUP_CONCAT(distinct(T.team_name)) from league L, player P, game_stats_new G, teams T where L.league_id = G.league_id and L.league_id = P.league_id and L.league_id = G.league_id and L.league_id = T.league_id and G.team_id = T.team_id and P.player_id = G.player_id and G.week <> P.bye and G.exclude = 0 and L.year = " + str(year) + " and P.position in ('RB','TE','WR') group by P.name order by average desc"

try:
  cur.execute(sql)

  results = cur.fetchall()


  for row in results:
    name = row[0]
    total = row[1]
    average = row[2]
    minimum = row[3]
    maximum = row[4]
    stddev = row[5]
    games = row[6]
    player_id = row[7]
    pos = row[8]
    nfl = row[9]
    team = row[10]

    if team.count(',') > 1:
      team = "2+ Teams"

    print "<tr>"
    print "<td>"
    print "<strong style=font-size:10>" + pos + "</strong>"
    print "<strong style=font-size:10>" + nfl + "</strong>"
    print "<a href=\"javascript:showPlayerStats('playerstats.py?player_id=" + str(player_id) + "&year=" + str(year) + "',this)\">"
    print name
    print "</a>"
    print "</td>"

    print "<td class=w3-centered>" + str(games)  + "</td>"
    print "<td class=w3-centered>" + str(total)  + "</td>"
    print "<td class=w3-centered>" + str(average)  + "</td>"
    print "<td class=w3-centered>" + str(minimum)  + "</td>"
    print "<td class=w3-centered>" + str(maximum)  + "</td>"
    print "<td class=w3-centered>" + str(stddev)  + "</td>"
    print "<td class=w3-centered>" + team  + "</td>"

    print "</tr>"

except:
  print "<h3>Error</h3>"
finally:
  db.close()


print "</body>"
print "</html>"

