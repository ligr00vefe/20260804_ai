from pymongo import MongoClient

# 이 파일은 단순하게 MongoDB에 접속하여 CRUD를 사용하는 방법입니다.
# client = MongoClient('mongodb://root:1234@localhost:27018') # docker 접속할 때
client = MongoClient('mongodb://book:1234@localhost:27017/admin')  # local 접속할 때

# 데이터베이스와 컬렉션 선택
db = client['mydatabase']
print(">>>", db)
collection = db['blog']

# Create (데이터 추가)
post = {
    'title': '첫 번째 글',
    'content': '파이썬과 몽고디비로 만든 블로그 글입니다.'
}
result = collection.insert_one(post)
print(f'삽입된 문서 ID: {result.inserted_id}')

# Read (데이터 조회)
retrieved_post = collection.find_one({'title': '첫 번째 글'})
print(f'조회된 문서: {retrieved_post}')

# Update (데이터 업데이트)
update_query = {'title': '첫 번째 글'}
new_values = {'$set': {'content': '업데이트된 내용'}}
collection.update_one(update_query, new_values)
print('데이터 업데이트 완료')

# Read again (업데이트된 데이터 조회)
updated_post = collection.find_one({'title': '첫 번째 글'})
print(f'업데이트 후 조회된 문서: {updated_post}')

# Delete (데이터 삭제)
# delete_query = {'title': '첫 번째 글'}
# collection.delete_one(delete_query)
# print('데이터 삭제 완료')

# 종료
client.close()