#!/usr/bin/python

import MySQLdb
import os
import sys
import credentials

def createDBConnection():
  host = credentials.getHost()
  user = credentials.getUser()
  passwd = credentials.getPasswd()
  dbname = credentials.getDB()

  db = MySQLdb.Connection(host,user,passwd,dbname)

  return db  

def createScript(path):
  print "  <script src=\"%s\"></script>" % path

def createHeader(title, admin=False, session=""):
  print "Content-Type: text/html"
  print session
  print
  print "<html lang=\"en\">"
  print "<head>"
  print "  <title>" + title + "</title>"
  print "  <meta charset=\"text/html; charset=ISO-8859-1\">"
  #print "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=yes\">"
  print "  <link rel=\"stylesheet\" href=\"//code.jquery.com/ui/1.12.0/themes/smoothness/jquery-ui.css\">"
  print "  <link rel=\"stylesheet\" href=\"css/sidburgh.css\">"
  print "  <link rel=\"stylesheet\" href=\"css/w3.css\">"
  print "  <link rel=\"stylesheet\" href=\"css/w3-theme-green.css\">"
  print "  <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">"

  if not admin:
    print "  <link rel=\"stylesheet\" href=\"http://www.rahulandreshma.com/css/rahulandreshma.css\">"
  print "  <link rel=\"stylesheet\" href=\"http://visualidiot.com/files/real-world.css\">"
  print "  <script src=\"https://code.jquery.com/jquery-1.12.4.js\"></script>"
  print "  <script src=\"https://code.jquery.com/ui/1.12.0/jquery-ui.js\"></script>"
  print "  <script src=\"https://cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js\"></script>"
  print "  <script src=\"https://cdn.datatables.net/1.10.12/js/dataTables.jqueryui.min.js\"></script>"
  print "  <script src=\"http://www.tablesorter.com/__jquery.tablesorter.js\"></script>"
  print "  <script>"
  print "    $( function() {"
  print "      $( \"#accordion\" ).accordion();"
  print "      $( \"#tabs\" ).tabs();"
  print "      $( \"input\" ).checkboxradio();"
  print "      $( \"fieldset\" ).controlgroup();"
  print "      $( \"#stats\" ).tablesorter();"
  print "      $( \"#dialog\" ).dialog( {width:'auto', autoOpen: false}  );"
  print "    } );"
  print "  </script>"
  print "</head>"
  print "<body>"
  print "<div class=content>"

  if not admin:
    print "<div class=contentbgstory></div>"
    print "<br>"
    print "<h1 class=top>Reshma & Rahul</h1>"
    print "<div>"
    print "<img class=story src=\"IMG_6066.JPG\"></img>"
    print "<img class=story src=\"IMG_6059.JPG\"></img>"
    print "<img class=story src=\"IMG_6067.JPG\"></img>"
    print "</div>"
    print "<br>" 
    print "<br>"

def createNavigation():
  print "<div>"
  print "<ul class=\"topnav\" id=\"myTopnav\">"
  print "<li><a href=\"adminrsvp.py\">RSVP</a></li>"
  print "<li><a href=\"adminguests.py\">Guests</a></li>"
  print "<li><a href=\"adminsummary.py\">Summary</a></li>"
  print "<li><a href=\"\">None</a></li>"
  print "</ul>"
  print "</div>"

def createFooter():
  print "</div>"
  print "</body>"
  print "</html>"

def escape(input_str):
  result = input_str.replace("'","\\'")
  result = result.replace("\"","\\\"")
  return result

