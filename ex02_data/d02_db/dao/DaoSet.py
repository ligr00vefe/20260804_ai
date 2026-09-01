import pymysql
# pip install pymysql

class DaoSet:
  def connect(self):
    self.con = pymysql.connect(host='localhost', user='db7', password='1234',
                               db="db7", charset='utf8')
    return self.con

  def disconnect(self):
    try:
      if self.con != None:
        self.con.close()
      if self.cursor != None:
        self.cursor.close();
    except Exception as e:
      print(e)