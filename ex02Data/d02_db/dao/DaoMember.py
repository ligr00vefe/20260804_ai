from d02_db.dao.DaoSet import DaoSet as dao

'''
CREATE TABLE member7
(
    memno INT PRIMARY KEY AUTO_INCREMENT,
    NAME  VARCHAR(20) NOT NULL,
    id    VARCHAR(20) NOT NULL,
    pw    VARCHAR(20) NOT NULL
);
'''


class DaoMember(dao):
    def __init__(self):
        self.con = dao.connect(self)
        self.cursor = self.con.cursor()

	def __del__(self):
		try:
			self.disconnect()
		except Exception as e:
			print(e)

	def get_all(self):
		cur = self.con.cursor()
		sql = "select * from member7 "
		cur.execute(sql)
		return cur.fetchall()

	def login_check(self, mem):
		rs = self.cursor.execute(f"select * from member7 "
								 f"where id='{mem.id}' and pw='{mem.pw}'")
		return rs

	def insert_one(self, mem):
		self.cursor.execute(f"insert into member7 (id, name, pw) "
							f"values('{mem.id}','{mem.name}','{mem.pw}') ")
		self.con.commit()
		return self.cursor.rowcount