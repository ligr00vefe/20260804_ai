from pymongo import MongoClient

conn = MongoClient('mongodb://book:1234@localhost:27017/admin')  # local 접속할 때
print(conn.list_database_names())
db_name = "db7"
db = conn.get_database(db_name)
print(db)

# def connect():