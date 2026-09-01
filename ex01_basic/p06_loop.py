print("{0:=^20}".format("반복문"))
print(f'{"반복문":=^20}')
'''
for 변수 in 리스트(또는 튜플, 문자열):
  수행 문장1
  수행 문장2
  ...
'''
ls = ['one', 'two', 'three']
for i in ls:
    print(i, end=' ')
print()
# 파이썬에서는 아래와 같은 패턴은 비권장
for i in range(len(ls)):
    print('index:', i, ' / item:', ls[i], end='\n')
print()

a = [(97, 'a'), [98, 'b'], (99, 'c')]
for (k, v) in a:
    print("{} : {}".format(v, k), end="\n")

for i in range(97, 97 + 26):
    if (i != 97): print('', end=',');
    print(chr(i), end='');
    if (i == 97 + 25): print();

marks = [90, 25, 67, 45, 80]
print('marks에서 60점 이상인 점수만 출력하시오')
for mark in marks:
    # if mark > 60: print(mark, end=' ')
    if mark < 60: continue
    print(mark)
for i in range(1, 11):
    if i == 5:
        print("5를 찾았습니다.")
        break
    print(i, end=' ')

a = "12ㄱ345"
if a.isnumeric():
    print(type(a))
else:
    print("Not a Number")

# 파이썬에서 for, if문은 새로운 지역 scope(영역)을 만들지 않음.
for i in a:
    if not i.isnumeric(): break
    result = "Not a Number"  # 지역변수 아님, 전역변수
print(result)
print(i)


# 함수안의 변수는 지역변수의 영역을 가짐.
def test():
    for idx in "123":
        result2 = "Not a Number"
    print(result2)
    print(idx)


test()
# print(result2) 외부에서 출력이 안됨.
# print(idx)

print(f'{"구구단":=^20}')
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i}*{j}={i * j:2}')  # 2칸을 사용해라!
    print()

# range(start, stop, step)
for i in range(2, 10, 3):
    for j in range(1, 10):
        for k in range(0, 3):
            if not ((i + k) == 10):
                print(f'{i + k} * {j} = {(i + k) * j:2}', end='\t')
        print()
    print()

print(f'{"역순 출력":=^20}')
for i in range(10, 0, -1):
    print(i)

# for else문은 break를 만나지 않는다면 else문 진행
for i in range(1, 5):
  print(i, end=', ')
else:
  print("모든 원소 출력")

for i in [1, 2, 3, 4]:
  if i % 3:
    print(i)
  else:
    break  # for의 else문은 실행되지 않음
else:  # 문제가 생기면 for의 else문은 실행 안됨.
  print("모든 원소 출력")

a = "12ㄱ345"
for i in a:
    # if not i.isnumeric(): break
    try:
        b = int(i)
        print(b)
    except:
        print("숫자가 아닌 문자열이 포함되어 있습니다.")
        break
    result = "Not a Number"
else:
    print("print all")
print(result)

a = list(range(1, 11))
print(a)
i = 0
while i < len(a):
  print("짝수" if a[i] % 2 == 0 else "홀수", end=' ');
  i += 1
print()

i = 0
while (i < 5):
  i += 1
  # if i % 3 == 0: break
  print(i)
else: # 반복문에서 break를 만나지 않으면 else문 실행
  print("💥1~4까지 모든 숫자가 출력")

# Python에는 do while문이 없다.
secret_word = "python"
counter = 0

while True:  # 무조건 1번은 실행
  word = input("암호를 입력하세요: ").lower()
  counter = counter + 1
  if word == secret_word:
    print("Well done!")
    break
  if word != secret_word and counter > 7:
    break

c = 5
while c:
  print(c)
  c -= 1

while True:
  response = input('숫자를 입력하세요:')
  result = int(response) % 10
  if result == 0:
    # continue
    break
  print("10으로 나눈 나머지는 {}입니다.".format(result))

# enumerate는 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
  print(p)

for i, v in enumerate(t):
    print(i, v)