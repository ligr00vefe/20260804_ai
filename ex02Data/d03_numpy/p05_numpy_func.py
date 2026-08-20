import numpy as np

SIZE = 5  # 원본 크기
ary1 = np.array([[-1, 0], [3, 4]])
ary2 = np.array([[3, 2], [-1, -2]])

print(ary1)
print('{0:=^20}'.format("단항 수식 함수"))
print(np.abs(ary1))
print(np.sign(ary1))
# print(np.sqrt(ary1)) # 음수일 경우 warning 발생
print(np.square(ary1))
# np.log(), np.log2(), np.log10()
# np.ceil() 올림, np.float() 내림, np.rint() 반올림
# np.cos(), np.sin(), np.tan()

print('{0:=^20}'.format("이항 수식 함수"))
print(ary1, ary2, sep="\n")
print(np.subtract(ary1, ary2))
print(np.multiply(ary1, ary2))
print(np.divide(ary1, ary2))
# print(np.power(ary1, ary2)) # 음수는 에러
print(np.minimum(ary1, ary2))
print(np.maximum(ary1, ary2))
print(ary1, ary2, sep="\n")
# a를 b로 나눈 나머지인데 항상 결과가 양수여야만 됨.
print("mod: \n",np.mod(ary1, ary2))
print(ary1, ary2, sep="\n")
#배열1 값을 배열2에 적용, 부호는 배열2를 적용
print(np.copysign(ary1, ary2))

print('{0:=^20}'.format("논리 함수"))
print(ary1, ary2, sep="\n")
print(np.logical_not(ary1))
print(np.logical_or(ary1, ary2))
print(np.logical_and(ary1, ary2)) #0인경우만 False

print('{0:=^20}'.format("비교 함수"))
print(ary1, ary2, sep="\n")
print(np.greater_equal(ary1, ary2))
print(np.greater(ary1, ary2))
print(np.less(ary1, ary2))
print(np.less_equal(ary1, ary2))
print(np.equal(ary1, ary2))
print(np.not_equal(ary1, ary2))
print('{0:=^20}'.format("조건식 표현"))
ary1 = np.random.randint(0,10, size=(3,3))
print(ary1)
ary2 = np.random.randint(0,10, size=(3,3))
print(ary2)
ary3 = np.random.choice([True, False], size=(3,3))
print(ary3)
print(np.where(ary3, ary1, ary2)) #ary3 참이면 ary1,거짓이면 ary2
print(np.where(ary1<0,0,ary1)) #ary1 <0면 0,거짓이면 ary1
print('{0:=^20}'.format("통계함수"))
print(ary1)
print(ary1.sum())
print(ary1.mean())
print(ary1.sum(axis=0)) # 세로
print(ary1.sum(axis=1)) # 가로
print((ary1 > 6).sum()) # 개수를 출력
print(ary1.min())
print(ary1.max())
print(np.sort(ary1))
print(np.sort(ary1)[::-1]) # 2차원 배열을 행단위 오름차순 정렬됨
ary4 = np.random.randint(0,10, size=10)
print(np.sort(ary4))
print(np.sort(ary4)[::-1]) # 1차원 배열은 내림차순 적용
print(np.unique(ary4))
print(np.intersect1d(ary1, ary2)) # 공통된 항목 추출

## 넘파이 2차원 배열 생성
imageAry = np.random.randint(0, 255, size=(SIZE, SIZE))
print('### 1. 원본 ###')
print(imageAry)
np.save('source', imageAry)

## (1) 10 증가후 저장
imageAry += 10
print('### 2. 10 증가 ###')
print(imageAry)
np.save('result1', imageAry)

##  (2) 흑백 처리후 저장
imageAry = np.where(imageAry < 128, 0, 255)
print('### 3. 흑백 처리 ###')
print(imageAry)
np.save('result2', imageAry)

##  (3) 반전 처리후 저장
imageAry = 255 - imageAry
print('### 4. 반전 처리 ###')
print(imageAry)
np.save('result3', imageAry)

## 복구1 ##
imageAry = np.load('result2.npy')
print('### 복구1 : result2.npy ###')
print(imageAry)

## 복구2 ##
imageAry = np.load('result1.npy')
print('### 복구2 : result1.npy ###')
print(imageAry)

## 복구3 ##
imageAry = np.load('source.npy')
print('### 복구3(원본) : source.npy ###')
print(imageAry)