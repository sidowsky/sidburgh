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

db = MySQLdb.Connection(host,
                user,
                passwd,
                dbname)

cur = db.cursor()

createHeader("Scores")
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
print "  function showTopPerformers(url, element)"
print "  {"
print "    var xhttp = new XMLHttpRequest();"
print "    xhttp.onreadystatechange = function() {"
print "      if (xhttp.readyState == 4 && xhttp.status == 200) {"
print "        document.getElementById(\"dialog\").innerHTML = xhttp.responseText;"
print "        $(\"#dialog2\").dialog( { position: {  my : 'center top+15%', at : 'center top', of : element } } );"
print "        $(\"#dialog2\").dialog(\"open\");"
print "      }"
print "    };"
print "    xhttp.open(\"GET\", url, true);"
print "    xhttp.send();"
print "  }"
print "</script>"


sql = "SELECT L.year, Sc.week, Sc.team_id, T.team_name, Sc.team_pts, Sc.opponent_team_id, T2.team_name as opponent_team_name, Sc.opponent_team_pts, Sc.is_playoffs, Sc.is_finals FROM  league L,  teams T, teams T2,  schedule Sc WHERE  L.league_id = T.league_id   AND L.league_id=T2.league_id AND L.league_id = Sc.league_id  AND T.league_id = Sc.league_id AND T2.league_id = Sc.league_id  AND T.team_id = Sc.team_id AND T2.team_id=Sc.opponent_team_id  and Sc.team_pts > Sc.opponent_team_pts ORDER BY   L.year DESC  ,  Sc.week DESC, Sc.team_pts DESC "

print "<div id=\"tabs\">"


try:
  cur.execute(sql)

  results = cur.fetchall()

  years = []
  year_html = ""
  weeks = []

  print "<ul>"
  for row in results:
    year = row[0]
    week = row[1]
    week_html = str(week)
    team_id = row[2]
    team_name = row[3]
    team_pts = row[4]
    opponent_team_id = row[5]
    opponent_team_name = row[6]
    opponent_team_pts = row[7]
    is_playoffs = row[8]
    is_finals = row[9]

    if is_finals == 1:
      week_html = week_html + " (championship)"
    elif is_playoffs == 1:
      week_html = week_html + " (playoffs)"

    week_html = week_html + " <a style=\"color:white;text-decoration: none\" href=\"javascript:showMatchup('weeklystats.py?week="+str(week)+"&year="+str(year)+"',this)\">&#9733;</a>"

    if year not in years:
      if len(years) > 0:
        year_html += "</table></div>"
        weeks = []

      year_html += "<div id=\"tabs-" + str(year) + "\">"

      print "<li><a href=\"#tabs-" + str(year) + "\">" + str(year) + "</a></li>"
      years.append(year)

    if week not in weeks:
      if len(weeks) > 0:
        year_html +=  "</table>"

      year_html += "<table class=\"w3-table w3-bordered w3-striped\"><thead><tr class=w3-theme><th width=200>Week " + week_html + "</th><th width=75></th></th><th width=200></th></tr></thead>"
      weeks.append(week)

    year_html += "<tbody><tr><td width=200>" + team_name + "</td><td class=w3-centered width=75><a href=\"javascript:showMatchup('matchup.py?team_id=" + str(team_id) + "&opponent_team_id=" + str(opponent_team_id) + "&year=" + str(year) + "&week=" + str(week) + "',this)\">" + str(team_pts) + "-" + str(opponent_team_pts) + "</a></td>"
    year_html += "<td width=200>" + opponent_team_name + "</td></tr></tbody>"


  print "</ul>"
  print year_html

  print "</div>"

  print "<div id=\"dialog\"></div>"
  print "<div id=\"dialog2\"></div>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

