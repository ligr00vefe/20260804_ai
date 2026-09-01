import numpy as np
import random

from utils.functions import printt

'''
고성능 수치 계산을 위해 가장 널리 사용되는 라이브러리 중 하나로, 
numpy는 주로 1차원, 2차원, 3차원 등의 배열을 처리하기 위한 용도와
선형 대수, 통계, 브로드캐스팅 등 다양한 기능을 제공
만들어진 라이브러리이다.
하나의 값이 아니라 복수개의 값을 처리하기 위한 라이브러리
'''
printt("1. 배열 생성")
a = np.array([1, 2, 3])  # 1차원
b = np.array([[1, 2], [3, 4]])  # 2차원
c = np.array([[[0, 1], [0, 1]], [[0, 1], [0, 1]]])  # 3차원
print(type(a), type(b), type(c))

printt("2. 배열 속성")
print(type(a))  # ndarray::N-dimensional array
print(b.shape)  # (2, 2)
print(b.ndim)  # 2 차원
print(b.size)
print(b.itemsize)  # 각 요소가 차지하는 메모리 크기를 바이트단위로 표기
print(b.dtype)  # int64=>8byte (또는 플랫폼에 따라 다름)
# int32는 4byte, float64는 8byte

printt("3. 기본 배열 만들기")
print(np.zeros((2, 3)))  # 2x3 영행렬::희소(sparse)행렬
print(np.ones((3, 2)))  # 3x2 모두 1인 배열
print(np.eye(3))  # 3x3 단위행렬, 항등행렬, 가로세로길이같음
print(np.full((2, 2), 7))  # 모두 7인 2x2 배열
print(np.arange(0, 10, 2))  # [0, 2, 4, 6, 8]
# 수평측에 간격 생성에 사용
print(np.linspace(0, 1, 5))  # 5단계 [0. , 0.25, 0.5 , 0.75, 1. ]

printt("4. 벡터 연산 +, *, **, /, - ")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(a ** 2)
print(b - 1)
print(b / 1) # [4. 5. 6.]
print(np.exp(a))  # 밑이 자연상수 e인 지수함수
print(np.log(b))

printt("5. 브로드캐스팅 예")
a = np.array([[1], [2], [3]])  # (3,1)
print(a)
b = np.array([10, 20, 30])  # (3,)
print(b)
print(a + b)  # (3,3)로 자동 확장됨
print(a * b)  # (3,3)로 자동 확장됨

printt("6. 배열 인덱싱")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a[0, 1])  # 2
print(a[:, 1])  # [2, 5]
print(a[1, :])  # [4, 5, 6]
print(a[1:, 1:]) #[[5 6]]

printt("7. 형태 변경 및 전치")
a = np.arange(8)  # [0 1 2 3 4 5 6 7]
print(a)
# 면, 행, 열 :: 총갯수 = 면 * 행 * 열
print(a.reshape((2, 4))) # [[0 1 2 3] [4 5 6 7]]
print("a.reshape(2, 2, 2):", a.reshape(2, 2, 2))
print(a.reshape((2, 4)).T)  # 전치

printt("8. 기본 통계")
a = np.array([[1, 2], [3, 4]])
print(np.mean(a))  # 평균
print(np.std(a))  # 표준편차
print(np.sum(a, axis=0))
print(a.sum())
print(a.mean())
print(a.max())
print(a.min())
print(a.std())
print(a.var()) #분산 Variance

printt("9. 논리 연산 및 마스킹")
a = np.array([1, 2, 3, 4, 5])
print(a[a > 3])  # [4 5]
print(a[(a > 2) & (a < 5)])  # [3 4]
print(np.where(a > 3, 1, 0))  # [0 0 0 1 1]

printt("10. 난수 생성")
np.random.seed(0)
print(np.random.rand(2, 3))  # 0~1 균등 난수  2행3열
print(np.random.randn(2, 2))  # 표준 정규 분포  2행2열

printt("11. 정규화와 표준화")
x = np.array([10, 20, 30, 40, 50])

# Min-Max Scaling 데이터를 0과 1사이의 숫자로 변환합니다.
x_norm = (x - x.min()) / (x.max() - x.min())
print(x_norm)

z = (x - x.mean()) / x.std()  # Z-score Standardization
# 역할: 데이터의 평균을 0, 표준편차를 1로 맞춰 변환
print(z)

numpyArr = np.random.randint(0, 256, size=(5, 5))  # 끝자리 제외
print(numpyArr)

numpyArr += 100
print(numpyArr)

pythonList = [random.randint(0, 255) for _ in range(5)]
print('* 파이썬 리스트 --> ', pythonList, type(pythonList))

numpyAry1 = np.array(pythonList)
print('* 형변환 pythonList --> ndarray ', numpyAry1, type(numpyAry1))

numpyAry2 = np.arange(5)
print('* arange(5) --> ', numpyAry2)

numpyAry3 = np.arange(3, 8)
print('* arange(3, 8) --> ', numpyAry3)
numpyAry3 = np.arange(0, 100, 20)
print('* arange(0, 100, 20) --> ', numpyAry3)

numpyAry4 = np.ones(5)
print('* ones(5) --> ', numpyAry4)
numpyAry5 = np.ones((3, 4))
print('* ones((3,4)) )--> ', numpyAry5)

numpyAry6 = np.zeros(5)
print('* zeros(5)--> ', numpyAry6)

numpyAry7 = np.empty(6)
print('* empty(6)--> ', numpyAry7)

numpyAry8 = np.full(5, 33)
print('* full(5, 33) --> ', numpyAry8)

numpyAry9 = np.identity(5)
print('* identity(5)--> 단위행렬 \n', numpyAry9)

printt("종합 실습")
scores = np.array([
    [80, 90, 70],
    [90, 85, 95],
    [70, 75, 80],
    [100, 95, 90]
])
print(scores.mean(axis=1)) # 학생별 평균
print(scores.mean(axis=0)) # 과목별 평균
print(scores.max())
print(np.argmax(scores)) # 최고 점수 위치
print(scores[scores >= 80])
print((scores - scores.min()) / (scores.max() - scores.min())) #정규화