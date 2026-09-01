# Python: script 언어(소스코드를 한 줄씩 읽어 바로 실행하는 Interpreter방식)
# Python은 들여쓰기 반드시 지킬 것! 안하면 에러발생
'''
interpreter 방식을 사용하기 위해서 REPL이라는 도구를 사용합니다.
ReadEvaluationPrintLoop
'''

print("print의 속성 : self, *args, sep='', end='\n', file=None")
print('Hello Python')
print(True, 3.14, 'Python')
print("특수기호", "\\,\t,\',\",\n ")
print("hello\tworld\t")
print() # 한줄 내려쓰기
print("파이썬은 '쉬운 언어'라는 컨셉을 가짐 ")
print('문이 열리고 "배달 왔어요"')
print('''
"안녕하세요?""'" '고길동'님", '참 오래가만이죠 ""'
''')
print("""해 뜨는 동해에서
해지는 서해까지
뜨거운 남도에서
광활한 만주벌판
""")
print("="*20)
# print("="+str(20)) #에러 발생: 합치는 것은 같은 타입끼리!
print("="+str(20))

for i in range(10):
    print(i, end=',')
print()
print(1,2,3,4,5, sep=',')
print(1,2,3,4,5, sep='🍉🍉')

f = open('test.txt','r')
lines = f.readlines()
for line in lines: print(line, end="🚩")