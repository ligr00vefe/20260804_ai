# 클래스 간 상속에서 생성자 사용
from utils.functions import printt


class Animal:
  def __init__(self, species):
    self.species = species

# breed: 새끼를 낳다
class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__("Dog")
    self.name = name
    self.breed = breed

d = Dog("Max", "Golden Retriever")
print(d.species, d.name, d.breed)

class Country:
  """Super Class"""
  name = '국가명'
  population = '인구'
  capital = '수도'

  def show(self):
    print('국가 클래스의 메소드입니다.')


class Korea(Country):
  """Sub Class"""

  def __init__(self, name):
    self.name = name

  def show_name(self):
    print('국가 이름은 : ', self.name)

korea = Korea("대한민국")
print(korea.name)
print(korea.show_name())
print(korea.capital)
print(korea.show())

class Korea(Country):
  """Sub Class"""

  def __init__(self, name, population, capital):
    self.name = name
    self.population = population
    self.capital = capital

  def show(self):
    # super().show() # 부모 메서드 호출 가능
    print(
      """
      국가의 이름은 {} 입니다.
      국가의 인구는 {} 입니다.
      국가의 수도는 {} 입니다.
      """.format(self.name, self.population, self.capital)
    )


a = Korea('대한민국', 50000000, '서울')
a.show()


# 다중상속
class Country:
  pass

class Province:
  pass

class Korea(Country, Province):
  pass

printt("상속관계를 확인해주는 mro()")
print(Korea.mro())
# mro()는 클래스를 작성하면 상속 관계를 확인할 수 있는 메소드
# 다중 상속을 사용하는 클래스에서 어떤 부모 클래스(super class)를
# 먼저 탐색하여 메서드나 속성(attribute)을 찾을지 순서대로
# 리스트형태로 보여주는 메서드

from abc import *
from abc import ABC, abstractmethod
printt("추상 클래스")
# 추상클래스란 미구현 추상메소드를 한개 이상 가지며,
# 자식클래스에서 해당 추상 메소드를 반드시 구현하도록 강제.
# 상속받은 클래스는 추상메소드를 구현하지 않아도,
# import할 때까지 에러는 발생하지 않으나 객체를 생성할 시 에러가 발생.
# 반드시 abc 모듈을 import 해야함.
# 추상메소드는 생략하면 기본적인 클래스 기능은 동작하지만,
# 추상메소드를 추가한 후에는 객체를 생성하면 에러가 발생.
# 추상 클래스에 일반 메서드도 만들 수 있다
# ABC -> 명시적인 추상화 / 구현 강제
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
  def sound(self):
    print("멍멍")

class Cat(Animal):
  def sound(self):
    print("야옹")

class AbstractCountry(metaclass=ABCMeta):
  name = '국가명'
  population = '인구'
  capital = '수도'

  def show(self):
    print('국가 클래스의 메소드입니다.')

  @abstractmethod
  def show_capital(self):
    pass

class Korea(AbstractCountry):
  def __init__(self, name, population, capital):
    self.name = name
    self.population = population
    self.capital = capital

  def show_name(self):
    print('국가 이름은 : ', self.name)

  def show_capital(self):
    super().show_capital()
    print(self.capital)

# a = AbstractCountry()  # 추상클래스는 인스턴스 생성 불가
# print(a.show())

b = Korea("대한민국", 50000000, '서울')
b.show_name()

a = Korea("대한민국", 50000000, '서울')
a.show_capital()

printt("파이썬에는 interface는 없다.")
from abc import ABC, abstractmethod

# 추상클래스를 마치 interface처럼 사용
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Pet(ABC):
    @abstractmethod
    def play(self):
        pass

class Dog(Animal, Pet):

    def sound(self):
        print("멍멍")

    def play(self):
        print("공놀이")

from typing import Protocol
# interface와 더 비슷한 역할 typing.Protocol
# Protocol -> 인터페이스와 비슷한 구조적 타이핑

class Animal(Protocol):
    def sound(self) -> None:
      # ...은 Ellipsis(생략 부호)라는 파이썬 객체, 여기에는 구현 내용이 없다,pass와 유사
        ...

class Dog:
  def sound(self):
    print("멍멍")

printt("추상클래스를 사용한 실제 예")
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"카드로 {amount}원 결제")

class KakaoPayment(Payment):
    def pay(self, amount):
        print(f"카카오페이로 {amount}원 결제")

payments = [CardPayment(),KakaoPayment()]

for payment in payments:
    payment.pay(10000)

# Python에서는 Java보다 추상 클래스의 필요성이 상대적으로 낮다.
# Python은 원래 Duck Typing을 많이 사용
# "이 객체가 Animal을 상속했는가?" 보다 "이 객체가 내가 필요한 sound()를 가지고 있는가?"
class Dog:
  def sound(self):
    print("멍멍")

class Cat:
  def sound(self):
    print("야옹")

def make_sound(animal):
  animal.sound()

make_sound(Dog())
make_sound(Cat())