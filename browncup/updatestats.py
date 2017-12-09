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

createHeader("Stats")
createNavigation()

print "<script>"
print 
print "  function getStats()"
print "  {"
print "    var xhttp = new XMLHttpRequest();"
print "    xhttp.onreadystatechange = function() {"
print "      if (xhttp.readyState == 4 && xhttp.status == 200) {"
print "        document.getElementById(\"results\").innerHTML = xhttp.responseText;"
print "        $(\"#stats\").trigger(\"update\");"
print "      }"
print "    };"
print "    var year = $('input[name=\"radio-year\"]:checked').val();"
print "    var pos = $('input[name=\"radio-pos\"]:checked').val();"
print "    xhttp.open(\"GET\", \"statshelper.py?pos=\" + pos  + \"&year=\" + year, true);"
print "    xhttp.send();"
print "  }"
print "  function showPlayerStats(url, element)"
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

print "<div>"

sql = "SELECT L.year from league L order by year desc"

try:
  cur.execute(sql)

  results = cur.fetchall()


  print "<fieldset>"
  print "<legend>Year</legend>"

  for row in results:
    year = row[0]
    print "<label for=\"radio-" + str(year) + "\">" + str(year)  + "</label>"
    print "<input type=\"radio\" name=\"radio-year\" id=\"radio-" + str(year) + "\" value=\"" + str(year) + "\" onclick=getStats()>"

  print "</fieldset>"

  print "<br>"

  print "<fieldset>"
  print "<legend>Position</legend>"

  print "<label for=radio-qb>QB</label>"
  print "<input type=radio name=radio-pos id=radio-qb value=\"QB\" onclick=getStats()>"

  print "<label for=radio-rb>RB</label>"
  print "<input type=radio name=radio-pos id=radio-rb value=\"RB\" onclick=getStats()>"

  print "<label for=radio-wr>WR</label>"
  print "<input type=radio name=radio-pos id=radio-wr value=\"WR\" onclick=getStats()>"

  print "<label for=radio-te>TE</label>"
  print "<input type=radio name=radio-pos id=radio-te value=\"TE\" onclick=getStats()>"

  print "<label for=radio-k>K</label>"
  print "<input type=radio name=radio-pos id=radio-k value=\"K\" onclick=getStats()>"

  print "<label for=radio-def>DEF</label>"
  print "<input type=radio name=radio-pos id=radio-def value=\"DEF\" onclick=getStats()>"

  print "</fieldset>"


  print "</div>"

  print "<div>"

  print "<table id=stats class=\"tablesorter w3-table w3-bordered w3-striped\">"
  print "<thead>"
  print "<tr class=w3-theme>"
  print "<th class=w3-centered>Name</th>"
  print "<th class=w3-centered>G</th>"
  print "<th class=w3-centered>Total</th>"
  print "<th class=w3-centered>Avg</th>"
  print "<th class=w3-centered>Min</th>"
  print "<th class=w3-centered>Max</th>"
  print "<th class=w3-centered>StdDev</th>"
  print "</tr>"
  print "</thead>"
  print "<tbody id=\"results\">"
  print "</tbody>"

  print "</div>"

  print "<div id=\"dialog\"></div>"


  createFooter()
except:
  print "<h3>Error</h3>"
finally:
  db.close()

