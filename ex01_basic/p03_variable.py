'''
정적타입 언어 : 자료형을 컴파일 타임에 결정하는 언어
동적타입 언어 : 자료형을 런타임(실행 시점)에 결정하는 언어
약타입 언어 : 자료형이 맞지 않을 시에 암묵적으로 타입을 변환하는 언어
강타입 언어 : 자료형이 맞지 않을 시에 에러 발생, 암묵적 변환을 지원하지 않음
Python은 동적타입이면서, 약타입 언어, 변수 타입을 강제 지정 불가
'''

print("=== 파이썬 변수의 자료형 ===")
'''
변수의 type
Scalar 타입 : int, float, None, bool 4가지: 단수의 값
Composite 타입 : str, list, tuple, dict, set: 복수의 값

불 자료형: True, False
숫자 자료형: int, float, complex
군집 자료형: str, list, tuple, dict, set
help(str) # 각타입별 설명 출력
'''

print("=== 변수의 명명규칙 ===")
'''
1) 변수나 함수는 Snake case, 클래스는 Pascal
2) _, 영문자(대소문자 구별), 숫자(시작 안됨) 사용, 그외 문자 불가
3) 예약어 안됨(if, for, ...)
4) 특수문자, 공백 X
5) null 대신 None을 사용
'''

# 변수의 재선언(O), 업데이트(O), 타입 고정(X)
a = 10
print(type(a))  # 객체지향적 언어
a = True
b = True
c = 3.14
print(type(a), type(b), type(c))

d = complex(3, -4)
print(d, type(d))
e = 10 + 3j + 5J
print(e, type(e))
print(type(d), type(e), d.real, d.imag)
s = 'hello'
print(s, type(s), )

# k = (a = 10 + 20) 할당문이 다른 할당문을 포함할 수 없다.
k = a = 10 + 20
print("k : {}, a : {}".format(k, a))
print(f"k : {k}, a : {a}")
print("k : %d, a : %d" % (k, a))

a = 1; b = 2;
print(f"교환전: a = {a} , b = {b}")
# tmp = a;a = b;c = tmp
a, b = b, a
print(f"교환전: a = {a} , b = {b}")

del a
# print(a)   a변수는 더이상 사용불가

# Python float는 내부적으로 C의 double을 그대로 사용
# Python에서 실수를 저장할때는 가까운 2진 부동소수점 형태로 변환.
# 소수점 16~17자리의 차이는 float 정밀도 한계라서
# 각각의 환경에 따라 반올림, 또는 근사값으로 반올림됨
a = 10.1234567890123455
b = 10.1234567890123452
print(a, type(a)) # 소수점 16자리에서 반올림 발생
print(b, type(b)) # 소수점 16자리에서 내림 발생
print(a == b)

import decimal
a = 10.1234567890123452
b = 10.1234567890123452
print(decimal.Decimal(a), type(a)) # 내부적으로 저장된 수
print(decimal.Decimal(b), type(b)) # 내부적으로 저장된 수
print(a == b)

from decimal import Decimal
a = 10.1234567890123452
b = 10.1234567890123452
print(decimal.Decimal(a), type(a)) # 내부적으로 저장된 수
print(decimal.Decimal(b), type(b)) # 내부적으로 저장된 수
print(a == b)
# 정확하게 소수를 표현하려면 Decimal()을 사용
a = Decimal("10.1234567890123452")
b = Decimal("10.1234567890123453")
print(a)
print(b)
print(a == b)

print("a={}".format(a))
print("a=%f" % a)
print(f'a={a}')
print(f'소수 첫째 자리 반올림: a={round(a,2)}')
print(f'소수 첫째 자리 반올림: a={a:.2f}')
print('소수 첫째 자리 반올림: a={:.2f}'.format(a))
print('소수 첫째 자리 반올림: a=%.2f' % a)

# 지수 표현
print("123e2 :", 123e2, type(123e2))
print("123e-2 :", 123e-2, type(123e-2))

# 복소수 표현
print(f"{"complex":=^20}")
a = 10 + complex(3)
print(a, type(a))
print(a.real, a.imag)

# None 표현
print(f"{"None":=^20}")
print(type(None), None)
print('' == None)
print(0 == None)
print(None == None)
word = None
print(word)  # None
a = None
# Python 3.10 이상, int 또는 None 할당 가능, Type Hint선언
# 3.9 이하에서 a: Union[int, None] 표기
a: int | None
print(a) # None
a = True
print(a, type(a))

print(f"{"형변환 함수":=^20}")
print("int(12.74): ", int(12.74), type(int(12.74))) #절삭
print("float(123): ", float(123), type(float(123)))
print("complex(3, 4): ", complex(3, 4), type(complex(3, 4)))
print("bool(-1): ", bool(-1))
print("bool(0): ", bool(0))
print("bool(1): ", bool(1))
print("bool(0.1): ", bool(0.1))
print("bool(''): ", bool(''))
print("bool(None): ", bool(None))
print("str(None): ", str(None))
print("str(97): ", str(97))
print("chr(97): ", chr(97))
print("ord('a'): ", ord('a'))
try:
  b = int("a10")  # 문자열, 수치자료를 int type 변경
  b = float("a0.12")  # 문자열, 수치자료를 float type 변경
except:
  print("숫자가 아닌 문자열이 포함되어 있습니다.")

print(f"{"문자형":=^20}")
print("hello", type("hello"))
string = "abc123def456"
number_string = ""
for char in string:
    if char.isdigit(): # 숫자가 맞으면
        number_string += char
number = int(number_string) # 형변환
print(number, type(number)) # 출력: 123456

a="A";
print(a, type(a))
print(ascii(a), end=' '); print(str(a), end=' '); print(ord(a));
a=65;
# chr()는 매개변수가 숫자여야만 함.
print(ascii(a), end=' '); print(str(a), end=' '); print(chr(a));

print("=" * 10)
print("Hello Python"[0])
print("Hello Python"[-3])
print("Hello Python"[0:12:3])  # [a:b:c] c폭

# python에는 상수가 없다.  python은 동적언어이기 때문에 상수가 불필요
from typing import Final
SIZE:Final = 5
SIZE = 10
print("final 재할당 가능 : ",SIZE)

import utils.Constant as const
const.PI = 3.14
print(const.PI)
# 에러 발생. 재할당이 안됨.
# const.PI = 3.141592

print(f'{"변수의 영역(scope) 확인":=^20}')
# 파이썬 변수 scope 룰을 LEGB 룰
# 변수가 값을 찾을 때, Local -> Enclosed -> Global -> Built-in
# local - 가장 가까운 함수안 범위.
# Enclosed - 파이썬은 함수 안에 함수가 정의 될수 있는데, 가장 가까운 함수가 아닌 두번째 이상의 함수 가까운 함수범위.
# Global - 함수 바깥의 변수 또는 import된 module
# Built-in - 파이썬안에 내장되어 있는 함수 또는 속성들.
# 로컬변수를 확인하는 locals()
# 글로벌변수를 확인하는 globals()
print('math' in globals())
import math
print('math' in globals())
from math import factorial
print('factorial' in globals())