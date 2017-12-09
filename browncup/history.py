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

createHeader("History")
createNavigation()

print "<script>"
print
print "  function showMatchup(url, element)"
print "  {"
print "    var xhttp = new XMLHttpRequest();"
print "    xhttp.onreadystatechange = function() {"
print "      if (xhttp.readyState == 4 && xhttp.status == 200) {"
print "        document.getElementById(\"dialog\").innerHTML = xhttp.responseText;"
print "        $(\"#dialog\").dialog( { position: {  my : 'center top+15%', at : 'center top', of : element } } );"
print "        $(\"#dialog\").dialog(\"open\");"
print "      }"
print "    };"
print "    xhttp.open(\"GET\", url, true);"
print "    xhttp.send();"
print "  }"
print "</script>"



sql = "select T.owner,L.year,S.wins,S.losses,S.champ,S.runner_up,S.playoffs,T.team_name,T.team_id from league L, teams T, standings S where L.league_id = T.league_id and L.league_id = S.league_id and T.team_id = S.team_id order by owner, year"

print "<div id=\"tabs\">"

print "<ul>"

history_html = ""

try:
  cur.execute(sql)

  results = cur.fetchall()

  owners = []

  for row in results:
    owner = row[0]
    year = row[1]
    wins = row[2]
    losses = row[3]
    champ = row[4]
    runner_up = row[5]
    playoffs = row[6]
    team_name = row[7]
    team_id = row[8]

    if owner not in owners:
      if len(owners) > 0:
        history_html += "</tbody></table>" + owners[len(owners)-1] + "_MATCHUP</div>"

      print "<li><a href=\"#tabs-" + owner + "\">" + owner + "</a></li>"

      history_html += "<div id=tabs-" + owner + ">"
      owners.append(owner)

      history_html += "<table class=\"w3-table w3-striped w3-bordered\">"
      history_html += "<thead>"
      history_html += "<tr class=w3-theme>"
      history_html += "<th width=30>Year</th>"
      history_html += "<th class=w3-centered width=75>Team</th>"
      history_html += "<th class=w3-centered width=30>W</th>"
      history_html += "<th class=w3-centered width=30>L</th>"
      history_html += "<th class=w3-centered width=150>Playoffs</th>"
      history_html += "</tr>"
      history_html += "</thead>"
      history_html += "<tbody>"

    history_html += "<tr>"


    history_html += "<td class=w3-centered width=30>"
    history_html += "<a href=\"standings.py#tabs-" + str(year) + "\">" + str(year) + "</a>"
    history_html += "</td>"
    history_html += "<td class=w3-centered width=75>"
    history_html += "<a href=\"schedule.py?year=" + str(year)  + "&team_id=" + str(team_id) + "\">"
    history_html += team_name
    history_html += "</a>"
    history_html += "</td>"
    history_html += "<td class=w3-centered width=30>" + str(int(wins)) + "</td>"
    history_html += "<td class=w3-centered width=30>" + str(int(losses)) + "</td>"

    result = ""

    if champ == 1:
      result = "<strong><i style=color:#FF4500>Champion</i></strong>"
    elif runner_up == 1:
      result = "<i style=color:#4682B4>Lost in Finals</i>"
    elif playoffs == 1:
      result = "<i style=color:grey>Made playoffs</i>"

    history_html += "<td class=w3-centered width=150>" + result + "</td>"
    history_html += "</tr>"

  print "</ul>"

  history_html += "</tbody></table>" + owner + "_MATCHUP</div>"

  #print "<div id=tabs-matchups>"

  #print "<div id=accordion>"

  sql = "select T.owner, T2.owner, sum(case when S.team_pts > S.opponent_team_pts then 1 else 0 end) as W, sum(case when S.team_pts < S.opponent_team_pts then 1 else 0 end) as L from schedule S, league L, teams T, teams T2 where S.league_id = L.league_id and S.league_id = T.league_id and S.league_id = T2.league_id and S.team_id = T.team_id and S.opponent_team_id = T2.team_id and T.owner <> T2.owner group by T.owner, T2.owner order by T.owner,W desc, L"

  cur.execute(sql)

  results = cur.fetchall()

  owners = []

  matchup_html = ""

  for row in results:
    owner = row[0]
    opponent_owner = row[1]
    wins = row[2]
    losses = row[3]

    if owner not in owners:
      if len(owners) > 0:
        matchup_html += "</tbody></table>"
        history_html = history_html.replace(owners[len(owners)-1]+"_MATCHUP", matchup_html)
        #print "<strong>" + owners[len(owners)-1]+"_MATCHUP" + "</strong>"
        matchup_html = ""
      #matchup_html += "<h3>" + owner + "</h3>"
      #matchup_html += "<div>"
      matchup_html += "<br><br><table class=\"w3-table w3-bordered w3-striped\">"
      matchup_html += "<thead><tr class=w3-theme><th>Record versus</th><th>W</th><th>L</th></tr></thead>"
      matchup_html += "<tbody>"
      owners.append(owner)

    matchup_html += "<tr><td><a href=\"javascript:showMatchup('matchuphist.py?owner=" + owner + "&owner2=" + opponent_owner + "',this)\"</a>" + opponent_owner + "</td><td>" + str(wins) + "</td><td>" + str(losses) + "</td></tr>"

  matchup_html += "</tbody></table></div>"

  history_html = history_html.replace(owner+"_MATCHUP", matchup_html)

  print history_html

  print "</div>"

  print "<div id=dialog></div>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

