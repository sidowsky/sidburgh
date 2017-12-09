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
team_id = fields.getvalue('team_id')
year = fields.getvalue('year')

flag = 0


sql2 = "SELECT L.league_id,L.year,T.team_id from league L,teams T where T.league_id=L.league_id and T.owner = (SELECT T.owner from league L,teams T where T.league_id=L.league_id and T.team_id=" + str(team_id) + " and L.year=" + str(year)  +  ")"

p_yr_html = "" 
n_yr_html = "" 

try:
  cur.execute(sql2)
  results = cur.fetchall()

  for row in results:
    l_id = row[0]
    yr = row[1]
    t_id = row[2]

    if yr == (int(year)-1):
      p_yr_html = "<a style=\"color:white;text-decoration: none\" href=\"schedule.py?year=" + str(yr) + "&team_id=" + str(t_id) + "\">&#8656;</a>" 

    if yr == (int(year)+1):
      n_yr_html =  "<a style=\"color:white;text-decoration: none\" href=\"schedule.py?year=" + str(yr) + "&team_id=" + str(t_id) + "\">&#8658;</a>"

except:
  print "<h3>Error</h3>"




sql = "SELECT Sc.week, Sc.team_id, T.team_name, Sc.team_pts, Sc.opponent_team_id, T2.team_name as opponent_team_name, Sc.opponent_team_pts, Sc.is_playoffs, Sc.is_finals FROM  league L,  teams T, teams T2,  schedule Sc WHERE  L.league_id = T.league_id   AND L.league_id=T2.league_id AND L.league_id = Sc.league_id  AND T.league_id = Sc.league_id AND T2.league_id = Sc.league_id  AND T.team_id = Sc.team_id AND T2.team_id=Sc.opponent_team_id  and Sc.team_id=" + str(team_id)  + " and L.year = " + str(year)  + " ORDER BY   L.year  ,  Sc.week "

try:
  cur.execute(sql)

  results = cur.fetchall()


  for row in results:
    week = row[0]
    week_html = str(week)
    team_id = row[1]
    team_name = row[2]
    team_pts = row[3]
    opponent_team_id = row[4]
    opponent_team_name = row[5]
    opponent_team_pts = row[6]
    is_playoffs = row[7]
    is_finals = row[8]

    if flag == 0:
      createHeader(team_name + " - " + year + " Schedule")
      createNavigation()

      print "<script>"
      print
      print "  function showMatchup(url, element)"
      print "  {"
      print "    var xhttp = new XMLHttpRequest();"
      print "    xhttp.onreadystatechange = function() {"
      print "      if (xhttp.readyState == 4 && xhttp.status == 200) {"
      print "        document.getElementById(\"dialog\").innerHTML = xhttp.responseText;"
      print "        $(\"#dialog\").dialog( { position: {  my : 'center top', at : 'center top', of : element } } );"
      print "        $(\"#dialog\").dialog(\"open\");"
      print "      }"
      print "    };"
      print "    xhttp.open(\"GET\", url, true);"
      print "    xhttp.send();"
      print "  }"
      print "</script>"


      print "<div>"
      print "<table class=\"w3-table w3-bordered w3-striped\"><thead><tr class=w3-theme><th class=w3-centered width=50>" + str(year) + "</th><th class=w3-centered width=150>" + p_yr_html + " " + team_name + " " + n_yr_html  + "</th><th class=w3-centered width=150></th></tr><tr class=w3-theme><th class=w3-centered width=50>Week</th><th class=w3-centered width=150>Opponent</th><th class=w3-centered width=150>Result</th></tr></thead>"


      flag = 1

    if is_playoffs == 1:
      week_html = week_html + "*" 

    score_html = "<a href=\"javascript:showMatchup('matchup.py?team_id=" + str(team_id) + "&opponent_team_id=" + str(opponent_team_id) + "&year=" + str(year) + "&week=" + str(week) + "',this)\">" + str(team_pts) + "-" + str(opponent_team_pts) + "</a>"

    if team_pts > opponent_team_pts:
      score_html = "W " + score_html
    elif team_pts < opponent_team_pts:
      score_html = "L " + score_html

    if is_finals == 1 and team_pts > opponent_team_pts:
      score_html = "<strong style=color:#FF4500>" + score_html + "</strong>"
    
    opponent_html = "<a href=\"schedule.py?year=" + str(year) + "&team_id=" + str(opponent_team_id) + "\">" + opponent_team_name + "</a>"

    print "<tbody><tr><td class=w3-centered width=50>" + week_html+ "</td><td class=w3-centered width=150>" + opponent_html + "</td>"
    print "<td class=w3-centered width=150>" + score_html + "</td></tr></tbody>"

  print "</div>"

  print "<div id=\"dialog\"></div>"

  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

