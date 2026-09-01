from utils.functions import printt

print('f{"python class":=^20}')
'''
# Magic Methods:: 파이썬 클래스 안에서 __이름__ 형태, 특별한 순간에 자동으로 호출하는 메서드들
1. 객체 생성/소멸 관련 
__new__(cls, ...) 생성::객체 생성 단계에서 호출됨, 인스턴스를 만들어 반환함
__init__(self, ...) 초기화::__new__에서 생성된 객체의 속성을 초기화, 생성자 아니고 초기화자!
__del__(self) 객체가 메모리에서 제거될 때 호출됨, 거의 사용하지 않음(예측하기 어려움)
'''
class Person:
  def __new__(cls, *args, **kwargs):
    print("__new__ 실행")
    return super().__new__(cls)
  # __new__()가 만들어서 반환한 객체를 가지고 __init__() 실행
  def __init__(self, name):
    print("__init__ 실행")
    # __new__에서 받아든 args의 첫번째 항목을 name에 할당하면서 초기화됨.
    self.name = name

p = Person("G")
print(p); print(p.name)
p2 = Person("G2")
print(p2); print(p2.name)

class Logger:
  def __init__(self, *messages, **options):
    self.messages = messages
    self.options = options


l = Logger("Start", "Running", level="INFO", timestamp=True)
print(l.messages)
print(l.options)

class Response:
  def __init__(self, data, status=200):
    self.data = data
    self.status = status


res = Response({"msg": "ok"}, 200)
print(res.data, res.status)

'''
2. 문자열 표현 관련 (print, str, repr)
__str__(self) print(obj)할 때 보이는 예쁜 문자열,사용자 친화적
__repr__(self) __str__없을 때 객체를 “정확하게 표현"하는 문자열, 디버깅/개발자 친화적,REPL에 객체 입력 시 사용됨
'''
class User:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"User(name={self.name})"

  def __repr__(self):
    return f"User<{self.name}>"
print("== __str__, __repr__ ==")
u = User("G")
print(u)  # __str__
print(repr(u))  # __repr__


class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def __str__(self):
    return f"User(name={self.name}, email={self.email})"

print(User("G", "g@test.com"))

class Point:
  def __init__(self, x, y):
    self.x = x;
    self.y = y

  def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"

pt = Point(10, 20)
print(">>",pt)

'''
3. 연산자 오버로딩 (산술, 비교 등)
|연산자| 메서드          |
| +   | `__add__`      |
| -   | `__sub__`      |
| *   | `__mul__`      |
| /   | `__truediv__`  |
| //  | `__floordiv__` |
| %   | `__mod__`      |
| **  | `__pow__`      |
| ==  | `__eq__` |  ★ 
| !=  | `__ne__` |
| <   | `__lt__` |
| <=  | `__le__` |
| >   | `__gt__` |
| >=  | `__ge__` |
'''

class User:
  def __init__(self, id):
    self.id = id

  def __eq__(self, other):
    return self.id == other.id

print(User(1) == User(1))

class Vector:
  def __init__(self, x):
    self.x = x

  def __add__(self, other):
    return Vector(self.x + other.x)

  def __eq__(self, other):
    return self.x == other.x

v1 = Vector(10)
v2 = Vector(20)
v3 = v1 + v2  # __add__
print("v3.x: ", v3.x)

print(v1 == Vector(10))  # __eq__

class Box:
  def __init__(self, items):
    self.items = items

  def __bool__(self):
    return len(self.items) > 0

print(bool(Box([])))  # False
print(bool(Box([1, 2])))  # True

'''
4. 컨테이너 관련 (len, 반복, 인덱싱) 리스트·딕셔너리처럼 동작하게 만들 때!
크기 관련
__len__(self) ★ 원소의 길이값 반환
반복 가능 객체
__iter__(self) → iterator 반환  ★ 
__next__(self) → next() 동작 ★ 
인덱싱/슬라이싱
__getitem__(self, key)  ★ 
__setitem__(self, key, value)  ★ 
__delitem__(self, key)
'''
class Config:
  def __init__(self, **kwargs):
    self._data = kwargs

  def __getitem__(self, key):
    return self._data[key]

config = Config(db="mysql", host="127.0.0.1")
print(config["db"])

class Cache:
  def __init__(self):
    self.store = {}

  def __setitem__(self, key, value):
    self.store[key] = value


cache = Cache()
cache["token"] = "abcd1234"
cache["token2"] = "abcd1234"
print(cache.store)

class ShoppingCart:
  def __init__(self):
    self.items = []

  def __len__(self):
    return len(self.items)

print(f"{' ShoppingCart ':=^20}")
cart = ShoppingCart()
cart.items.append("apple")
cart.items.append("바나나")
cart.items.append("아보카도")
print(len(cart))


class TagList:
  def __init__(self, *tags):
    self.tags = tags
    print(type(self.tags))

  def __len__(self):
    return len(self.tags)


t = TagList("python", "ai", "chatgpt")
print(len(t))

class Count:
  def __init__(self, limit):
    self.limit = limit
    self.current = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.limit:
      self.current += 1
      return self.current
    raise StopIteration

for i in Count(4):
  print("Count",i)

class MyList:
  def __init__(self):
    self.data = []

  def __getitem__(self, index):
    return self.data[index]

  def __setitem__(self, index, value):
    self.data[index] = value

  def __delitem__(self, index):
    del self.data[index]
print(f"{' MyList ':=^20}")
lst = MyList()
lst.data = [10, 20, 30]
print(lst[1])  # __getitem__
lst[1] = 99  # __setitem__
print(lst.data)
del lst[0]  # __delitem__
print(lst.data)

class DataStream:
  def __init__(self, data):
    self.data = data
    self.idx = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.idx >= len(self.data):
      raise StopIteration
    item = self.data[self.idx]
    self.idx += 1
    return item

stream = DataStream([10, 20, 30])
for v in stream:
  print(v)

'''
5. 호출, 속성 접근
__call__(self)  obj() ★ :: 인스턴스 자체만으로도 기능을 부여
| 동작       | 메서드                                |
| obj.x 읽기 | `__getattr__` / `__getattribute__` |
| obj.x = v | `__setattr__`                      |
| del obj.x | `__delattr__`                      |
|디렉터리 목록| `__dir__`                          |
'''
class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")

g = Greeter()
g("G")  # __call__

class LogAccess:
  def __getattr__(self, name):
    print(f"{name} 속성이 없음!")
    return None

obj = LogAccess()
print(obj.missing)  # __getattr__ :: missing 속성이 없음! None

class Keywords:
  def __init__(self, items):
    self.items = items

  def __contains__(self, key):  # True, False 중 반환
    return key in self.items

k = Keywords(["python", "ai"])
print("__contains__","ai" in k)  # True

class Predictor:
  def __call__(self, x):
    return x * 2


predict = Predictor()
print(predict(5))

'''
6. 컨텍스트 매니저 (with 문)
with 객체:에서 자동 호출!
__enter__(self) ★
__exit__(self, exc_type, exc, traceback)  ★
'''

print(f'{"FileOpener":=^20}')
class FileOpener:
    def __enter__(self):
        print("파일 열기")
        return "FILE"
    def __exit__(self, exc_type, exc, tb):
        print("파일 닫기")

with FileOpener() as f:
    print("with 내부:", f)

print(f'{"Dummy":=^20}')
class Dummy:
  def __enter__(self):
    print("start")

  def __exit__(self, *args):
    print("end")

with Dummy():
  print("doing...")

print(f'{"FileManager":=^20}')
class FileManager:
  def __init__(self, path):
    self.path = path
  def __enter__(self):
    self.f = open(self.path, "w")
    return self.f
  def __exit__(self, exc_type, exc, tb):
    self.f.close()
with FileManager("log.txt") as f:
  f.write("Hello")
print("log.txt를 확인하세요")

'''
7. 클래스 관련 클래스 자체 커스터마이징
__class__ → 객체가 속한 class
__dict__ → 객체 속성 딕셔너리
__mro__ → 클래스 상속 순서(Method Resolution Order)
__bases__ → 부모 클래스
8. 복사/직렬화 같은 다양한 기능들
__copy__
__deepcopy__
__getstate__, __setstate__ (pickle 관련)
'''

printt("Flight")
# pass 내용을 정하지 않고 일단은 클래스를 생성할 경우
class Flight:
  pass

f = Flight() # 초기화
print(id(f), type(f))

printt("초기화자")
class Person:
  def __init__(self):
    print("객체가 생성되었습니다.")
p = Person()

# 속성 추가
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(self.name, self.age)

p = Person("Alice", 30)

class Flight:
  def number(self):
    return 1

f = Flight()
print(id(f), f.number(), type(f))

class Flight:
  # 만들어진 객체를 초기화 생성자
  def __init__(self):
    print('init')
    super().__init__()
  # 객체를 만들기전에 호출되는 메서드
  def __new__(cls):
    print('new')
    return super().__new__(cls)

  def number(self):
    return 1

f = Flight()
print("f.number(): ", f.number())

class Parrot: #앵무새
  def fly(self):
    print("Parrot flying")

class Airplane:
  def fly(self):
    print("Airplane flying")

class Whale:
  def swim(self):
    print("Whale swimming")
class Suyeon:
  def __new__(cls):
    return super().__new__(cls)

def lift_off(entity):
  if hasattr(entity, "fly"):
    entity.fly()
  elif hasattr(entity, "swim"):
    entity.swim()
  else:
    print("run")

parrot = Parrot()
airplane = Airplane()
whale = Whale()
sy = Suyeon()

lift_off(parrot)
lift_off(airplane)
lift_off(whale)
lift_off(sy)

class Student:
  def __init__(self, name, grades=None):
    if grades is None:
      grades = []
    self.name = name
    self.grades = grades

printt("Charile")
s = Student("Charlie")
print(s.name, s.grades)

printt("Singleton 패턴")
class Singleton:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      print("새 인스턴스 생성")
      cls._instance = super().__new__(cls)
    return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
print(id(a), id(b))
print()

printt("@classmethod와 @staticmethod")
# 정적메소드(@classmethod와 @staticmethod)
class CustomClass:
  # instance method
  def add_instance_method(self, a, b):
    return a + b

  # classmethod
  @classmethod
  def add_class_method(cls, a, b):
    return a + b

  # staticmethod
  @staticmethod
  def add_static_method(a, b):
    return a + b


print(CustomClass.add_static_method(1,1))
print(CustomClass.add_class_method(1, 1))


# @classmethod와 @staticmethod 의 차이
class Language:
  default_language = "Korean"

  def __init__(self):
    self.show = '나의 언어는 ' + self.default_language

  # cls 나 self등의 매개변수를 받는 경우, 클래스의 속성에 접근 가능
  # 첫 번째 인자 cls에는 자동으로 Language 클래스 주입
  @classmethod
  def class_my_language(cls, self): # cls 는 클래스 자체
    print("cls.default_language: ", cls.default_language)
    print(self.show)
    obj = cls()
    print(obj.show)
    return obj

  # cls 나 self등의 매개변수를 받지못함, 인스턴스를 생성하는 기능제공
  @staticmethod
  def static_my_language():
    return Language()

  def print_language(self):
    print(self.show)

lang = Language()
# Language.class_my_language(Language, lang)의 코드는 아래 코드와 동일. self 때문
print("class: ",Language.class_my_language(lang)) #cls.default_language:  Korean
print("static: ",Language.static_my_language())

# 상속으로 사용
class KoreanLanguage(Language):
  default_language = "한국어"

kor = KoreanLanguage()
kor.print_language()
