# Set (중복과 순서가 없는 자료형)
# 순서가 없기 때문에 인덱싱이 지원 안됨
# 중괄호를 사용
# 데이터의 중복을 제거하기 위한 필터로 종종 사용
import random

s = set()
print(s,type(s))

s = set([1,2,3,4,5]) # list => set
print(s, type(s))
l1 = list(s) # set => list
print(l1, type(l1))

s = set("HELLO")
print(s, type(s))

s = set(range(5))
print(s)

s = set('기러기')
print(s)

s = {} # 주의 빈 중괄호는 dict가 됨!
print("s = {}", type(s))

# set은 list, dict와 달리 set안에 set을 넣을 수 없다.
# s = {
#   {1,2,3},
#   {3,4,5}
# }
# print(s)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

print(f'합집합: s1 ∪ s2')
print(s1.union(s2))
print(set.union(s1, s2, {6,7,8,9}))
print(s1 | s2)

print(s1 , s2)
print(f'교집합: s1 ∩ s2')
print(s1.intersection(s2))
print(set.intersection(s1,s2, {6,7,8,9}))
print(s1 & s2)

print(f'차집합: s1 - s2')
print(s1.difference(s2))
print(set.difference(s1, s2, {6,7,8,9}))
print(s1 - s2)

print(f'대칭차집합(XOR): s1 ^ s2')
print(s1.symmetric_difference(s2))
#3개 이상의 집합을 매개변수로 전달 안됨.
print(set.symmetric_difference(s1, {3,4,5,6,7}))
print(s1 ^ s2)

print('할당연산자:기존의 집합에 연산을 진행함으로 주소 동일:대입연산자 사용시')
a = {1,2,3,4}; print(id(a))
a |= {3,4,5,6}    # 주소가 동일
print('a |=', a, id(a))
a = a | {3,4,5,6} # 주소가 다르게 나옴
print('a = a |', a, id(a))

a = {1,2,3,4,5}; print(id(a))
a &= {3,4,5,6}
print('a &=', a, id(a))
a = a & {3,4,5,6}
print('a = a &', a, id(a))

a = {1,2,3,4}; print(a, id(a))
a -= {3,4,5,6} # 3은 3을 찾아서 제거,역시 4도 마찬가지. 결과는 1,2
print('a-= ', a, id(a))
a = a - {3,4,5,6}
print('a=a- ', a, id(a))

a = {1,2,3,4};
a ^= {3,4,5,6}
print('^ ', a) # 같은것(3,4)는 제거됨.

print('set의 관계 연산')
a = {1,2,3,4}
print('부분집합 <= ', a <= {1,2,3,4})
print('부분집합 issubset', a.issubset({1,2,3,4,5}))
print('진부분집합 < ', a < {1,2,3,4,5})
print('상위집합 >= ', a >= {1,2,3,4})
print('상위집합 issuperset', a.issuperset({1,2,3,4}))
print('진상위집합 >= ', a >= {1,2,3})

print(a == {1,2,3,4}); print(a == {3,2,1,4})
print('겹침여부아닐경우true isdisjoint: ', a.isdisjoint({5,6,7,8}))
print('겹침여부아닐경우true isdisjoint: ', a.isdisjoint({3,4,5,6}))

print(f'{" set 함수 ":=^20}')
print(a, type(a))
a.add(5); print(a)
a.remove(5); print(a) # element가 없으면 에러
a.discard(9); print(a)# element가 없으도 OK
a.pop(); print(a) # 임의의 element를 삭제
print(len(a))

print(f'{"Shallow Copy":=^20}')
a = {1,2,3,4,5}; print(a)
a = {1,2,3,4}; print("a", a, id(a))
b = a; # 주소를 복사 a와 b가 동일
print("b", b, id(b))
print(a is b)
b.add(5)
print(a, b)

print(f'{"Deep Copy":=^20}')
a = {1,2,3,4}; print("a", a, id(a))
b = a.copy() # a와 b는 다른 set
print("b", b, id(b))
print(a is b)
b.add(5)
print(a, b)

a = {1,2,3,4}
for i in a: print(i, end=" ")
print()
for i in {1,2,3,4}: print(i, end=" ")
print()
a = {i for i in 'pineapple' if i not in 'apl'}
print(a, type(a))
a = set(i for i in 'pineapple' if i not in 'apl')
print(a, type(a))

#집합의 내용 수정 안됨, 2 차원 이상 생성 가능
a = frozenset(range(5))
a = frozenset({0,1,2,3,4})
print(a, type(a))
a = frozenset({
  frozenset({1,2}), frozenset(range(3,5))
})
print(">>",a)

lotto = set()
while len(lotto) < 6:
  ball = int(random.random() * 45) + 1
  lotto.add(ball)
lotto = sorted(lotto) # set을 정렬할 때
print(lotto)

print(f'{"set의 함수":=^20}')
s = set()
s.add(1)
s.add(2)
print(s, type(s))
s.update([2, 3])
print(s, type(s))
s.remove(2) # 원소를 제거, 없으면 에러 발생
s.discard(2) # 원소를 제거, 없어도 에러 없음
print(s, type(s))
s.pop() # 맨 앞에 내용 삭제
print(s, type(s))

print(1 in s)
print(1 not in s)

# Set 표현식
words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
print(type({word for word in words}))
print(type(words))
# Set 표현식 if 필터링
print({len(word) for word in words if len(word)> 3})