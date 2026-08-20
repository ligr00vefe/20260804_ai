import copy
import random

'''
 list  순서 있고 중복 허용, muttable
 다양한 자료형을 순차적으로 저장하는 집합적 자료형
 list 는 [] 대괄호로 작성되어지며, 내부 원소는 ,로 구분
 리스트는 마지막 원소뒤에 콤마를 남겨도 에러가 나지 않는다.
 보통 편의를 위해 마지막에 콤마를 찍기를 권장.
'''

# range는 값을 확인하기 위해서 다른 순서 있는 컬렉션으로 변환
# range(시작숫자, 종료숫자, step)의 형태로 리스트 슬라이싱과 유사
# range의 결과는 시작숫자부터 종료숫자 바로 앞 숫자까지 컬렉션을 만듦
a = list(range(10, 20, 2))
print("a:", a)

print(f"{' list 선언 ':=^20}")
list1 = [1, 2, 3, 4, 5, 6]
print("list1:", list1, id(list1))

list1 = list(range(1, 5))
print("list1:", list1, id(list1))

# list의 원소에 접근하기
print(list1)
print(list1[0])
print(list1[2])
for idx in range(len(list1)):  # 인덱스로 접근
    print(list1[idx], end=' ')
    if idx == len(list1) - 1: print()

for item in list1:  # 원소에 접근
    print(item, end=' ')
print()

# list +연산
list2 = ["Love", 'is', "Great", "and", "Holy"]
print(list2, type(list2))
list3 = list1 + list2  # 순서가 있음
print(list3, type(list3))

print(f'{"list의 slicing":=^20}')
print("list1: ", list1)
print("0:3 ", list1[0:3])
print(":3 ", list1[:3])
print(": ", list1[:])  # 전체 출력
print("5:20 ", list1[5:20])  # 인덱스가 넘어가도 에러발생 없음
print("1:4 ", list1[1:2])  # 끝자리 제외
print("-1 ", list1[-1])
print("-2 ", list1[-2])
print("-4:-2 ", list1[-4:-2])

print(f'{"list의 기타 함수":=^20}')
s = "Love is Great and Holy"
print(s[1:-1])  # ove is Great and Hol
print(s[3:])
print(s[:3])
print(s.index('is'))
print(s.count('a'))
print("reverse: ", s[::-1])
print(s)  # 원본의 변화는 없다.
y = sorted(s)
print("y:", y, type(y))
y = sorted(s, key=str.lower)
print("y:", y, type(y))
y = ''.join(sorted(s))
print(y, type(y))
full_slice = s[:]
print(full_slice, type(full_slice))
print(full_slice == s)
print(full_slice is s)

s = ["Love", 'is', "Great", "and", "Holy"]
print(s.index("Great"))
print(s.count("Love"))
print(s[::2])  # start:end:step
print(s[::-1])
u = s.copy()  # 깊은 복사
v = list(s)  # 깊은 복사
print(s, id(s))
print(u, id(u))
print(v, id(v))
x = s
print("x:", x, id(x))
s[0] = "주먹밥"
print(s)
print(x)

y = sorted(s)
print(y)


def keyld(s): return len(s)  # 길이만으로 정렬


y = sorted(s, key=keyld)
print("y:", y)
y = sorted(s, key=lambda s: (len(s), s))  # 조건2가지, 길이, 알파벳/가나다순
print("y:", y)
y = reversed(v)
print(y)
print(''.join(y))

print("== reverse 출력 방법 ==")
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# range(start, stop, step)
for i in range(len(list_a) - 1, -1, -1):
    print(list_a[i], end=' ')
    if (i == 0): print()
for item in reversed(list_a):
    print(item, end=' ')
print()

print(f"{'list의 연산':=^20}")
a = [1, 2, 3]
b = list(range(3, 7))  # list()와 range()로 list생성
print(a, ',', b)

# print(a + b) # 합
print('a+b', a + b)
print('b+a', b + a)
# print(a - b) # 차 X : unsupported operand
print(a * 3)  # 원소 각각이 아니고, 리스트 전체를 3번

print(f'{"shallow copy":=^20}')
a = [[2, 5]] * 3  # shallow copy 얕은 복사
print(a, type(a))
a[0].append(7)  # [[2, 5, 7], [2, 5, 7], [2, 5, 7]] 3
print(a, len(a))

print(f'{"deep copy":=^20}')
v = [[2, 5] for _ in range(3)]  # deep copy
v = [copy.copy([2, 5]) for _ in range(3)]  # deep copy
v = [copy.deepcopy([2, 5]) for _ in range(3)]  # deep copy
v = [[2, 5].copy() for _ in range(3)]  # deep copy
v = [[2, 5][:] for _ in range(3)]  # deep copy
print("deep copy:", v, type(v))
v[0].append(8)
print(v)

b[0] = 0  # 수정
print(b)
del b[0]  # 삭제 indexing
print(b)
del b[0:]
print(b)

print(f"{'list의 메서드':=^20}")
l = list();
l.append(1);  # 끝에 추가
print("l", l)
l.insert(9, 2);  # 원하는 곳에 추가
for i, v in enumerate(l): print(i, v)
print("l", l)
l.extend([3, 4, 5])  # list를 추가
print("l", l)
l = l + [6, 7]
print("l", l)
del l[len(l) - 1];  # 마지막 인덱스를 지움
# index('a') 'a'라는 원소를 찾은 후 그 인덱스를 반환
print("l >> ", l, len(l), l.index(len(l)))
del l[l.index(len(l))];  # del l[5] :: 6 원소의 인덱스값이 5
print("l del", l, len(l))  # index(원소) 해당 원소가 있는 위치를 인덱스로 반환
l.remove(5)  # 값으로 5라는 원소를 지울 때
print("l", l)
l.pop() # 끝에 있는 값 지울 때
print("l pop", l)
l.clear() # 완전 지울때
print("l", l)

for i in range(0, 10):
    l.append(i)
print("l", l)
l.append(True)
l.append("Python")
l.append(12.34)
lcopy = l.copy()
print(id(l), id(lcopy)) # deep copy

print(f'{"2차원배열":=^30}')
lists = [
    ['홍길동', '90', '100', '90'],
    ['고길동', '91', '90', '90'],
    ['강길동', '89', '95', '90'],
    ['김길동', '70', '92', '90'],
]
print(lists)
print(lists[0])
print(lists[1][3])


def print2Arr(arr):
    for row in arr:
        for col in row:
            print(f"{col:>4}", end=' ')
        print()
    print()


print2Arr(lists)

# 2차원 list 크기 초기화
lists2 = [[0 for c in range(5)] for r in range(5)]
for i in range(len(lists)):
    for j in range(len(lists[i])):
        lists2[i][j] = lists[i][j]
        if j != 0:
            lists2[len(lists)][j] += int(lists[i][j])
            lists2[i][len(lists[i])] += int(lists[i][j])
            lists2[len(lists)][len(lists[i])] += int(lists[i][j])
    print()
print()
lists2[len(lists)][0] = "총합계"

print2Arr(lists2)

print(f'{"리스트 표현식":=^30}')
words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
print([len(word) for word in words])  # 리스트 표현식
print(words)

length = []
for word in words:
    length.append(len(word))
print(length)

# 리스트 표현식 if 문에 의한 필터링
print([len(word) for word in words if len(word) > 3])

# 랜덤 생성
SIZE = 5
listArr = [random.randint(0, 255) for _ in range(SIZE)]
print("1차원 리스트 " + str(type(listArr)), listArr, sep="\n")
# listArr2 = []
# for _ in range(SIZE):
#   tmpList = []
#   for _ in range(SIZE):
#     tmpList.append(random.randint(0,255))
#   listArr.append(tmpList)
listArr2 = [
    [random.randint(0, 255) for _ in range(SIZE)]
    for _ in range(SIZE)
]
print2Arr(listArr2)

# 2차원 배열의 최대, 최소 값
min_val = min(map(min, listArr2))  # 2
max_val = max(map(max, listArr2))
print("최대, 최소 : ", min_val, max_val)

# 2차원 리스트를 1차원으로 평탄화 시켜 출력
arr1 = list(col for row in listArr2 for col in row)
print(arr1)
print(
    ', '.join(
        str(listArr2[i][j]) for i in range(len(listArr2)) for j in range(len(listArr2[i])))
    , " \n")
print(', '.join(str(i) for i in [1, 2, 3]))

# *: "unpacking 연산자", 리스트나 튜플 등의 위치 인자를 uppack!
# 시퀀스 자료형의 요소들을 하나하나 풀어서 함수의 인자로 넘겨주는 역할,
print([col for row in listArr2 for col in row])
print(*[col for row in listArr2 for col in row])
values = [1, 2, 3]
print(values)
print(*values)


# **: "unpacking 연산자", 딕셔너리의 키워드 인자(key=value)를 unpack!
def greet(name, age):
    print(f"이름: {name}, 나이: {age}")


info = {"name": "철수", "age": 20}
# 일반적인 함수 호출
greet(name="철수", age=20)
# 딕셔너리 unpacking 사용
greet(**info)

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = {**a, **b}
print(merged)
