# Python Format Specification 문자열.format()
# {}의 갯수는 인자보다 같거나 작아야한다.

print("{}".format(10))
print("{} {}".format(10, 20, 30))
# print("{} {} {}".format(10, 20))

print("[type :: 출력형식(d:십진수,b:2,o:8,x:16,X:16,c:문자,s:문자열)]")
print("{:8}".format("hello"))
print("{:>8}".format("hello"))
print("{:<8}".format("hello"))
print("{:^8}".format("hello"))
print("{:8d}".format(123))
print("{}".format(True)) # True 출력
print("{:b}".format(True)) # 이진수 1출력
print("{:b}".format(False)) # 이진수 0출력
print("{:o}".format(False)) # 팔진수 0출력
print("{:x}".format(False)) # 십육진수 0출력
print("{:X}".format(11)) # 십육진수 B출력
print("{:c}".format(65))
print("{:s}".format(chr(97)))
print("{:c}".format(ord('a')))
print("{:s}".format(ascii('a')))
print("{:s}".format("Hello"))
a = 10
print(a, type(a))
print(a, format(a, 'b'))
print(a, format(a, 'o'))
print(a, format(a, 'x'))
print(a, format(a, 'X'))
print(a, format(a, '#b'))
print(a, format(a, '#o'))
print(a, format(a, '#x'))
print(a, format(a, '#X'))
a = 0b1010; print(a, type(a))
a = 0o12; print(a, type(a))
a = 0xa; print(a, type(a))
a = 0XA; print(a, type(a))

print("[type :: 출력 형식(f:실수,e:지수,%:백분율,g:자동형식,.:정확도)]")
print("{:8f}".format(3.141592))
print("{:8.2f}".format(3.141592))
print("{:8.3f}".format(3.141592)) # 3자리 이하에서 반올림
print("{:.3}".format("helloworld")) # 정확도를 문자열에 지정

print("[fill :: 채우기(*, _, 0, #) 정렬과 같이 사용]")
print("{:*^10}".format("hi"))
print("{:=^10}".format("제목"))
print("{:_>8d}".format(123))
print("{:0>8d}".format(123))
print("{:#>8d}".format(123))
print("{:$>8d}".format(123))

print("[align :: 정렬(>, <, ^, =)]")
print("{:>8d}".format(123)) #왼쪽 정렬
print("{:<8d}".format(123)) #오른쪽
print("{:^8d}".format(123)) #가운데
print("{:=8d}".format(123)) #빈자리 8자리
print("{:-=8d}".format(123)) #빈자리를 -로 8자리
print("{:^20}".format("string"))
print("{:=^20}".format("string"))
print("{0:=>20}".format("string"))
print("{0:=<20}".format("string"))
print("{0:_^20}".format("string"))

print("[sign :: 부호(+, -, )]")
print("{:+d}","{:+d}".format(10))
print("{:-d}","{:-d}".format(-10))
print("{: d}","{: d}".format(-10)) # 공백은 알아서 부호 처리

print("[width :: 전체 폭]")
print("{:8}","{:8}".format("hi")) # 최소 글자 수 지정
print("{:8}","{:8}".format(123)) # 최소 글자 수 지정
print("{:8d}","{:8d}".format(123)) # 최소 글자 수 지정
print("{:8d}","{:8d}".format(123456789)) # 넘을 수 있다
print("{:-8d}","{:-8d}".format(-123)) #     -123 -포함
print("{:+08d}","{:+08d}".format(123)) # +0000123
print("{:-08d}","{:-08d}".format(-123)) # -0000123
print("{:+=8d}","{:+=8d}".format(-123)) # -++++123
print("{:-#8d}","{:-#8d}".format(-123)) #     -123
print("{:8}","{:8}".format("hi")) # hi
print("{:*^8d}","{:*^8d}".format(-123)) # **-123**

print("[대체 형식 :: #b, #x, #o]")
print("{:#b}".format(10))
print("{:#x}".format(10))
print("{:#o}".format(10))

print("[grouping :: , _ ]")
print("{:,d}".format(1234567))
print("{:_d}".format(1234567))

'''
0 → 0 패딩
= → 부호 뒤부터 패딩
+ → 양수에도 부호 표시
12 → 폭
.4 → 소수점 4자리
f → 고정 소수점
'''
print("[fill][align][sign][#][0][width][grouping][.precision][type]")
print("{:+08d}".format(-123))
print("{:08d}".format(-123))
print("{:=08d}".format(-123))  #  = → 부호 뒤부터 패딩
print("{:.3g}".format(12345.678)) # 1.23e+04 g는 일반 서식
print("{:.5s}".format("Hello, world")) # Hello 출력
print("{:*^+10d}".format(123)) #***+123***
print("{:>15,}".format(1980000))
print("{:<10} {:>10}".format("Name", "Score"))
print("{:<10} {:>10}".format("Alice", 90))
print("{:0=+12.4f}".format(-3.141592)) # -00003.1416

print("[f-string 사용]")
city = 'Busan'
print(f'내가 사는 곳{city}')
print('내가 사는 곳{}'.format(city))
print("{:=^20}".format("str"))
print(f'{"str":=^20}')
print(f'{10}')
print(f'{3.141592:0.4f}') # 소수자리에서 반올림

d={'city':'Busan', 'year':2025}
print("{}년 내가 사는 곳: {}".format(d['year'], d['city']))
print(f"{d['year']}년 내가 사는 곳: {d['city']}")
print("%d년 내가 사는 곳:%s" % (d['year'], d['city']))