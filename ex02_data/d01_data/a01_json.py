# json 라이브러리 포함시키기
import json

# json 문자열 데이터
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

# type() 함수로 자료형 확인하기
print(type(employee_string))

# 문자열을 객체로 변환하기
json_object = json.loads(employee_string)

# 새로운 자료형 확인하기 json으로 loads()를 하면 dict 타입으로 변형
print(type(json_object))

print(json_object["first_name"])

employees_string = '''
{
    "employees": [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"
       },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
       }
    ]
}
'''

# type() 함수로 자료형 확인하기
print(type(employees_string))

data = json.loads(employees_string)

print(type(data))

# first_name에 접근하기
for employee in data["employees"]:
    print(employee["first_name"])
