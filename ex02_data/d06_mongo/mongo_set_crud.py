from mongo_set import MongoSet

'''
고정된 형식 없이 BSON(Binary JSON) 형태로 유연하게 저장되면 아래처럼 계층 구조로 이루어짐
데이터베이스(Database), 컬렉션(Collection::table), 문서(Document::row), 필드(Field::column)
문서 지향(Document-oriented) NoSQL 데이터베이스
'''
class MongoCRUD:
  def __init__(self):
    self.mongo_set = MongoSet()
    self.collection = self.mongo_set.connect_collection()

  def create_document(self, document):
    try:
      result = self.collection.insert_one(document)
      print(f'삽입된 문서 ID: {result.inserted_id}')
    except Exception as e:
      print(f'삽입 중 에러 발생: {e}')

  def read_document(self, query):
    try:
      result = self.collection.find_one(query)
      print(f'조회된 문서: {result}')
    except Exception as e:
      print(f'조회 중 에러 발생: {e}')

  def update_document(self, query, new_values):
    try:
      result = self.collection.update_one(query, new_values)
      print(f'업데이트된 문서 수: {result.modified_count}')
    except Exception as e:
      print(f'업데이트 중 에러 발생: {e}')

  def delete_document(self, query):
    try:
      result = self.collection.delete_one(query)
      print(f'삭제된 문서 수: {result.deleted_count}')
    except Exception as e:
      print(f'삭제 중 에러 발생: {e}')

  def disconnect(self):
    self.mongo_set.disconnect_collection()


# 사용 예제
crud = MongoCRUD()

# Create
post = {'title': '새로운 글', 'content': 'CRUD 클래스로 추가한 글'}
crud.create_document(post)

# Read
crud.read_document({'title': '새로운 글'})

# Update
update_query = {'title': '새로운 글'}
new_values = {'$set': {'content': '업데이트된 내용'}}
crud.update_document(update_query, new_values)

# Delete
delete_query = {'title': '새로운 글'}
crud.delete_document(delete_query)

# Disconnect
crud.disconnect()