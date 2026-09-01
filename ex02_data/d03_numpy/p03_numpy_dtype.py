import numpy as np

# 넘파이의 데이터 형식을 dtype이라고 하는데 매우 다양한 자료형을 제공
pList1 = [10, 20, 30, True]
pList2 = [10, 20, 30, 40.0]

numpyAry1 = np.array(pList1) # 파이썬리스트를 넘파이로 형변환
print("1",numpyAry1, numpyAry1.dtype)

numpyAry1 = np.array(pList2)
print("2",numpyAry1, numpyAry1.dtype)

numpyAry2 = np.array(pList1, dtype=np.float32)
print("3",numpyAry2, numpyAry2.dtype) # 주의 40.0 => 1. 변환

numpyAry3 = np.arange(5)
print("4",numpyAry3, numpyAry3.dtype)

numpyAry4 = np.ones(5)
print("5",numpyAry4, numpyAry4.dtype)

numpyAry5 = np.ones(5, dtype=np.int8)
print("6",numpyAry5, numpyAry5.dtype)

numpyAry6 = numpyAry5.astype(np.float16)
print("7",numpyAry6, numpyAry6.dtype)