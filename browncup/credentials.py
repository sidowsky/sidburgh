def getHost():
  f = open("../../config/.host")
  value = f.readline().rstrip()
  f.close()
  return value


def getUser():
  f = open("../../config/.dbuser")
  value = f.readline().rstrip()
  f.close()
  return value


def getPasswd():
  f = open("../../config/.dbpasswd")
  value = f.readline().rstrip()
  f.close()
  return value


def getDB():
  f = open("../../config/.db")
  value = f.readline().rstrip()
  f.close()
  return value
