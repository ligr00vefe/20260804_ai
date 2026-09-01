# def : define
# 중복된 코드를 줄일 수 있고, 코드의 가독성을 높이고, 유지보수성을 향상
# Processing 들의 묶음
'''
def 함수이름(매개변수1, 매개변수2, ...):
    함수본문
    return 반환값
'''


# 1) 함수 정의(매개변수 없고, 리턴타입 없음)
def lines():
    print("==" * 12)


lines()


# 2) 함수 정의(매개변수 있고, 리턴타입 없음)
def lines(str):
    print(f'{" " + str + " ":=^30}')


# lines() # 에러: 파이썬에는 overloading이 없기 때문에 최종 함수로 적용
lines("Title")


# 3) 함수 정의(매개변수가 없고, 리턴타입 있음)
def lines():
    return f"{'':=^30}"


print(lines())


# 4) 함수 정의(매개변수가 있고, 리턴타입 있음)
def lines(str):
    return f"{" " + str + " ":=^30}"


print(lines("python"))


# default arguments, positional arguments
def calculator(a, b, c=0):
    return a + b + c


print(calculator(1, 2))
# print(calculator(1)) #positional argument error

print(f'{"함수의 인자 전달":=^30}')
m = [1, 5, 7]


def modify(k):
    k.append(10)
    print("k = ", k)
    for i, v in enumerate(k):
        k[i] += 10


# 함수에 mutable한 객체를 인자로 전달하면,
# 함수내부에서 변형이 이루어지면, 외부에서도 영향을 받음
modify(m)
print(m)

r = [10, 15, 20]
print(r, id(r))


def replace(s):
    s = [25, 30, 35]  # 새로운 주소가 할당됨.
    print("s =", s, id(s))


replace(r)
print("r: ", r)


# print("s: ",s) 함수의 지역변수는 외부에서 사용안됨.

def replace(s):
    s = [25, 30, 35]  # 새로운 주소가 할당됨.
    print("s =", s, id(s))
    return s


r = replace(r)
print("r: ", r, id(r))

total = 0


# * 개수 제한 없는 인자 전달하려고 할 때 사용, tuple로 자동변환
def add(*args):
    print(type(args))
    global total
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4, 5, 6))
print(add(1, 2, 3, ))
print(add(1))


# **는 dict, 키와 밸류의 형태를 가진 개수 제한 없는 수집을 할때
def print_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_info(name="python", age=20)


def f1(): print("f1", var)


def f2():
    var = 10;
    print("f2", var)


def f3(inputVar):
    global var  # global 위치에 상관없이 변수 호출가능
    var = inputVar
    print("f3 local var", var)


var = 100

f1();
f2();
f3(10000);
print(var)  # 실행 시점에 선언이 되기 때문에 호출가능


# 파이썬의 이름 찾기 규칙 (LEGB Rule)
# Local (함수 내부 지역 변수)
# Enclosing (중첩 함수 상위 함수 스코프)
# Global (현재 파일의 전역 변수)
# Built-in (파이썬 내장 함수들)

def print_all_elements(list_of_things):
    ## 중첩함수 선언 :: 내부적으로 사용하기 위한 함수
    def print_each_element(things):  # 리스트 요소를 하나씩 꺼내주는 함수
        for thing in things:
            print(thing, end=' ')
        print()

    if len(list_of_things) > 0:
        print_each_element(list_of_things)
    else:
        print("There is nothing!")


print_all_elements([1, 2, 3, 4, 5, 6])


# 중첩함수가 부모 함수의 변수나 정보를 가두어 사용하는 것을 Closure
def outer(x):
    def inner(y):
        return x + y

    return inner


add_five = outer(5)
print("중첩", add_five(3))
print("중첩", add_five(4))
print("중첩", add_five(5))
print("중첩", add_five(6))
print("중첩", add_five(7))

print(f'{"lambda 식":=^20}')
print("조건1: 단일 표현식이어야 함, 오직 1개의 식만 작성")
print("조건2: return 사용 안됨")
print("조건3: 변수 할당, 반복문, 조건문등은 사용불가(반환하지 않는 문장만 사용불가)")
def square(x): return x ** 2
# lambda (익명 함수)
square = lambda x: x ** 2

add = lambda x, y: x + y
print(add(2, 3))   # 5

is_even = lambda x: "짝수" if x % 2 == 0 else "홀수"
print(is_even(10))  # 짝수

students = [("Alice", 25),("Bob", 20),("Chris", 22)]
print(type(students), type(students[0]))
# 나이로 정렬 sorted(목록, key=정렬기준) s1: 튜플의 두번째 값으로 정렬
def function(student):
  return student[1]

# sorted 내장 함수, default 오름차순
sorted_students = sorted(students, key=function)
sorted_students = sorted(students, key=lambda s: s[1])
print(sorted_students)

nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 10, nums))
print(result)  # [10, 20, 30, 40]

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

words = ["apple", "banana", "kiwi", "avocado"]
sorted_words = sorted(words, key=lambda w: (len(w), w))
print(sorted_words)
# 단어 길이 → 알파벳 순 두 가지 기준으로 정렬 ['kiwi', 'apple', 'banana', 'avocado']

def calc(fn, num):
  return fn(num)
print(calc(lambda x: x * 3, 5))  # 15

funcs = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
print([f(5) for f in funcs])
# [6, 10, 25]

# Decorator: 기존 함수 수정하지 않고 기능을 추가하는 함수. 클로저와 고차 함수가 기반
# @my_decorator는 say_hello = my_decorator(say_hello)와 같음
def my_decorator(func):
  def wrapper():
    print("Before function")
    func()
    print("After function")
  return wrapper

@my_decorator
def say_hello():
  print("Hello ")
  print("World!")

say_hello()