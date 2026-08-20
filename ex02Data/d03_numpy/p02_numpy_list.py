import random
import numpy as np
from utils.functions import printt


printt("List 를 Numpy 로 변환", 30)
SIZE = 5
listArr = [random.randint(0, 255) for _ in range(SIZE)]
print("1차원 리스트 " + str(type(listArr)), listArr, sep="\n")

listArr = [
  [random.randint(0, 255) for _ in range(SIZE)] for _ in range(SIZE)
]
# listArr = []
# for _ in range(SIZE):
#   listTmp = []
#   for _ in range(SIZE):
#     listTmp.append(random.randint(0,255))
#   listArr.append(listTmp)
print("2차원 리스트 " + str(type(listArr)), listArr, sep="\n")

print(type(listArr))
np_list = np.array(listArr) # list => d03_numpy
print(type(np_list))

# 출력
print(listArr)
print(np_list)

printt("Numpy 를 List 로 변환", 30)
numpy_test = np.array([1, 2])
list_test = numpy_test.tolist()
print(list_test)