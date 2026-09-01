from pymongo import MongoClient

class MongoSet:
  def connect_collection(self):
    self.client = MongoClient('mongodb://book:1234@localhost:27017/admin')  # local 접속할 때
    self.db = self.client['db7']
    self.collection = self.db['test']
    return self.collection

  def disconnect_collection(self):
    try:
      if self.client is not None:
        self.client.close()
    except Exception as e:
      print(e)