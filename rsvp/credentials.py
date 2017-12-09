import os
import Cookie
import sys
import traceback

def getHost():
  f = open("../../config-rsvp/.host")
  value = f.readline().rstrip()
  f.close()
  return value


def getUser():
  f = open("../../config-rsvp/.dbuser")
  value = f.readline().rstrip()
  f.close()
  return value


def getPasswd():
  f = open("../../config-rsvp/.dbpasswd")
  value = f.readline().rstrip()
  f.close()
  return value


def getDB():
  f = open("../../config-rsvp/.db")
  value = f.readline().rstrip()
  f.close()
  return value


def authenticate(db,cur):
  try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

    sql = "select session_id from user where user_id = 1"

    cur.execute(sql)
    results = cur.fetchall()

    for row in results:
      db_session_id = row[0]


    if cookie["session"].value == db_session_id:
      return
  except:
    db.close()

  print "Content-Type: text/html"
  print
  print "<html>"
  print "<head>"
  print "<meta http-equiv=\"Refresh\" content=\"0;url=http://www.sidburgh.com/rsvp/admin.py\">"
  print "</head>"
  print "<body>"
  print "</body>"
  print "</html>"
  sys.exit()

def authenticateUser(cur, passwd, user, admin):
  if admin:
    field = "admin_passwd"
  else:
    field = "guest_passwd"

  sql = "SELECT " + field + " from user where user_id = " + str(user)

  try:
    cur.execute(sql)

    results = cur.fetchall()

    for row in results:
      check_passwd = row[0]

    if passwd == check_passwd:
      return True
  except:
    print "<h3>Error</h3>"
  
  print "<h3>Invalid Credentials!</h3>"

  return False

