print(f'{"list의 iter":=^20}')
a = [1, 2, 3]
a_iter = iter(a)
print(type(a_iter))

print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
# print(next(a_iter)) 다음이 없기에 에러발생

print(f'{"set의 iter":=^20}')
b = {1, 2, 3}
b_iter = iter(b)
print(dir(b))
print(b_iter.__next__())
print(next(b_iter))
print(b_iter.__next__())

print(f'{"dict의 iter":=^20}')
d={'a':1, 'b':2, 'c':3}
it = iter(d.items()) # items() key, value
print(next(it))
# it = iter(d.items()) # 위줄 다음 원소부터 출력
for k, v in iter(d.items()):
  print(k, v)

it = iter(d) # keys()
for k in iter(d.keys()):
# for k in iter(d): #아래줄과 동일.
# for k in it:
  print(k)

it = iter(d.values()) # values()
for v in it:
  print(v)

# generator : iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함
# 각각의 yield를 만날때 까지 구분
# iterable한 순서가 지정됨(모든 generator는 iterator)
# 느슨하게 평가된다.(순서의 다음 값은 필요에 따라 계산됨)
# 함수의 내부 로컬 변수를 통해 내부상태가 유지된다.
# 무한한 순서가 있는 객체를 모델링할 수 있다.(명확한 끝이 없는 데이터 스트림)
# 자연스러운 스트림 처리를 위 파이프라인으로 구성할수 있다.
# generator를 동시에 두개 생성하면, 서로가 다른 객체이며, 각기 따로 동작

def test_generator():
  print('yield 1 전')
  yield 1
  print('yield 1과 2사이')
  yield 2
  print('yield 2와 3사이')
  yield 3
  print('yield 3 후')

gen = test_generator()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
print("=== generator ===")
gen = test_generator()
for item in gen:
  print(item)