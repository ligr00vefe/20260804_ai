from d02_db.dao.DaoSet import DaoSet

con = DaoSet().connect()
if con != None:
  print('Succeeded Connection!')
else:
  print('Connection Failed!')