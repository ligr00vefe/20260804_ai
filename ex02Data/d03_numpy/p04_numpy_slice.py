import numpy as np

data = np.array([1, 2, 3])
print(data[0]);print(data[1]);print(data[2])
print(data[0:2])
print(data[:3])
print(data[1:])
print(data[-1])
print(data[-2:])
print(data[:-1])

SIZE = 5  # 원본 크기
startRow, startCol = 1, 1  # 새로운 리스트의 시작 위치
nSIZE = 3  # 새로운 리스트의 크기

## 넘파이 1차원 => 2차원 배열 변환
value = 1
# np.arange(start, stop, step)
myAry1 = np.arange(value, value + (SIZE * SIZE), 1)
print(">>", myAry1)
myAry1 = myAry1.reshape(SIZE, SIZE)
print(myAry1)
print(myAry1[1])
print(myAry1[1, 0:2])
print(myAry1[1, :])
print(myAry1[2:])
print(myAry1[2:4, ])
print(myAry1[2:4, :])
print(myAry1[:, 1])
print(myAry1[0:3, 1])
print(myAry1[0:3, 1:3])  # 일부만 추출할 경우
print(myAry1[[1, 3], :])  # 비연속적 추출할 경우
print(myAry1[:, :])

data = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12]])
print(data)
arr1 = data[:2, :2]
print(arr1)
print(data[:2, 1:3])
# 주의 사항 : 슬라이싱된 배열을 수정하니 원본 배열도 변경됨!!!
arr1[0,0] = 100
print(arr1)
print(data)
arr1[0,0] = 1
print(data)
print(arr1.ndim) #차원을 출력
arr2 = data[1, :] # 1차원
print(">>",arr2)
print(arr2.ndim) # 배열은 여러차원으로 슬라이싱 가능
print(arr2.shape)
arr2 = data[1:2, :]
print(arr2.ndim) # 2차원
print(arr2.shape)
# arr3 = d01_data[[0,1,2],[0,1,0]] # 2차원 배열의 이산 슬라이싱
arr3 = data[[0,1,2]] # 행단위로 출력
print(arr3)

data = np.arange(2,21,2)
print(data)
idx = np.array([0,0,0,1,1,2,3,4,4,4,5,5,5,6,6,6,7,8,9])
arr1 = data[idx]
print(arr1, arr1.shape) # arr1에는 더 많은 데이터를 가져올 수 있다.
data = np.array([[1,2],[3,4],[5,6]])
print(data)
arr1 = data[[2,0,1],:]
print(arr1)

ary = np.arange(1, 17)
ary = ary.reshape(4, 4)
print(ary)
print(ary[[1, 3], :])
print(ary[:, [1, 3]])
ary1 = np.zeros((2, 2), dtype=np.int8)
print(ary1)
ary2 = np.ones((2, 2), dtype=np.int8)
print(ary2)
ary1 = np.arange(1, 5, 1).reshape(2,2)
print(ary1)
ary2 = np.arange(5, 9, 1).reshape(2,2)
print(ary2)
print(np.concatenate((ary1, ary2), axis=0))  # 세로
print(np.concatenate((ary1, ary2), axis=1))  # 가로

print('## 넘파이 2차원 배열 리스트의 출력')
for i in range(SIZE):
  [print("%3d" % myAry1[i][k], end=' ') for k in range(SIZE)]
  print()
print()
print(myAry1.transpose(1,0))
print(myAry1.transpose(0,1))
myAry1 = myAry1.T
print(myAry1)
myAry1 = myAry1.T
print(myAry1)

## 넘파이 2차원 배열의 슬라이싱
myAry2 = myAry1[startRow:startRow + nSIZE, startCol: startCol + nSIZE].copy()
print(myAry2)

## 넘파이 2차원 배열의 출력
for i in range(nSIZE):
  [print("%3d" % myAry2[i][k], end=' ') for k in range(nSIZE)]
  print()
print()
print(myAry2)

print(myAry2)