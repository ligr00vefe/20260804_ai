class _constant:
  # obj.some_attr = x가 호출될 때 __setattr__(self, "some_attr", x)가 실행, 즉 속성 할당을 가로채서 커스터마이징
  def __setattr__(self, key, value):
    # 인스턴스의 현재 속성 사전(__dict__)에 이미 같은 이름의 키가 있는지 확인
    if key in self.__dict__: #__dict__는 인스턴스가 가진 실제 속성(이름 → 값)들의 저장소
      raise Exception("변수에 값을 할당할 수 없습니다.")
    self.__dict__[key] = value # 속성이 아직 없을 때(처음 설정할 때)에만 __dict__에 값을 직접 넣는다.
  def __delattr__(self, item):  # 속성 삭제(del obj.some_attr)가 호출될 때 실행되는 특별 메서드
    if item in self.__dict__: # 삭제도 가로채서 금지하려는 의도
      raise Exception("변수를 삭제할 수 없습니다.")
# python의 sys객체에 _constant 클래스를 등록함으로 static하게 사용
import sys # 파이썬의 표준 라이브러리 sys 모듈
sys.modules[__name__] = _constant()