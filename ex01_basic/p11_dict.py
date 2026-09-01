# dict (키를 이용하여 값을 저장하는 자료형)
# 정수형 인덱스가 아닌 키로 값을 저장하기 때문에 저장된 순서는 무의미
# key(immutable)는 중복 불가, value(mutable)는 중복 가능
# {}를 사용, 빈 {}는 타입이 dict
# dictionary는 키가 중복되면 마지막이 표시되는 것에 유의

import copy
import pprint
from traceback import print_tb

d = dict()
print(d, type(d))
d = dict(a = 1, b = 2, c = 3)
print(d, type(d))

d = {"a": 1, "b": 2, 'c': 3}
print(d)
l = [["a", 1], ["b", 2],["c", 3]] # list
l = [("a", 1), ("b", 2),("c", 3)] # tuple in list
l = (("a", 1), ("b", 2),("c", 3)) # tuple
l = (["a", 1], ["b", 2],["c", 3]) # list in tuple
d = dict(l)
print("l to d",d, type(d))
d['a'] = 10 # 업뎃
print(d)
d['d'] = 4 # 항목 추가
print(d)
# print(d['k']) #없는 key는 에러
print("k", d.get('k')) #없는 경우 None
print("k", d.get('k', 100)) #없는 경우 default 적용

print(f'{"dict의 복사":=^20}')
print(d, id(d))
d2 = d.copy() # 깊은(deep) 복사
d2['a'] = 1
print(">>", d2, id(d2))
print(d, id(d))
d3 = dict(d) # 깊은(deep) 복사
d3['a'] = 1
print(d3, id(d3))
print(d, id(d))

print(f'{"dict 복사":=^20}')
d = {'a': [1,2], 'b': 2, 'c': 3}
print("1", d, id(d))
d4 = copy.copy(d) # 깊은(deep) 복사
d4['a'].append(3)
print("2", d4, id(d4))
print("1", d, id(d))
d5 = copy.deepcopy(d) # 깊은(deep) 복사
d5['a'].append(4)
print("3", d5, id(d5))
print("1", d, id(d))


print(d.keys())
print(d.values())
print(d.items()) # key, value 동시 출력
tmp = list(d.values())
print(tmp)
tmp = [i for i in d.values()]
print("tmp",tmp, type(tmp))

print("==for in문으로 key, value에 접근할 때==")
for k in d:
  print(k, d[k], sep=":", end=",")
print()
for k in d.keys():
  print(k, d.get(k), sep=":", end=",")
print()
for v in d.values():
  print(v, sep=":", end=",")
print()
for k, v in d.items():
  print(k, v, sep=":", end=",")
print()

print(f'{"dict 함수":=^20}')
# setdefault는 추가만, update는 수정, 추가 가능
d.setdefault('e') # value 없이 key만 넣을 때 값은 None
print("d",d, type(d))
d.setdefault('f', 5) # value 값을 넣을 경우
print(d)
d.update(a='One', g = 6) # key 없는 경우 추가됨.
print(d)
print(d.pop('a'))
print(d.pop('z', 100)) # 없는 key 인 경우 default
print(d)
del d['g']
print(d)
print("d.popitem(): ",d.popitem()) #python 3.6이상에서는 맨끝, 이하에서는 임의
print(d)
# print(d.pop()) # dict에는 pop()사용 안됨


print('a' in d) # False 출력
print('a' not in d) # True
pprint.pprint(d) # dict를 읽기 쉽게 출력해 주는 함수
d.clear()
print(d)

# Dictionary 표현식
country_capital = {'대한민국':'서울','영국' :'런던','미국' :'워싱턴','일본' :'도쿄'}
capital_country = {capital: country for country, capital in country_capital.items()}
print(capital_country, type(capital_country))

country = ['Sweden', 'Saudi', 'USA', 'Korea', 'Swiss']
result = { w[0] : w for w in country}
print(result) # 중복 배제 S

# set {1,2}, dict{a:1,b:2}, {}만으로 할 경우 dict
import os
import glob
from pprint import pprint as pp
file_info = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*.*')}
pp(file_info)
