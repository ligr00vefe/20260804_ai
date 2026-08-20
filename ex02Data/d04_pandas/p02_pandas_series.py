import numpy as np
import pandas as pd

from utils.functions import printt

printt("numpy 1차원 배열로 Series 생성")
sr0 = pd.Series(np.arange(5))
print(sr0, type(np.arange(5)))
printt("pandas Series로 Series 생성")
sr0 = pd.Series(pd.Series([100, 50, 70, 90]))
print(sr0, type(pd.Series([100, 50, 70, 90])))
printt("python List로 Series 생성")
sr0 = pd.Series([100, 50, 70, 90])
print(sr0, type([100, 50, 70, 90]))
printt("range 로 Series 생성")
tmp = range(3, 11)
print(tmp, type(tmp)) # range(3, 11) <class 'range'>
sr0 = pd.Series(tmp)
print(sr0, tmp)
printt("python tuple로 Series 생성")
sr0 = pd.Series((100, 50, 70, 90))
print(sr0, type((100, 50, 70, 90)))
printt("python dict로 Series 생성")
sr0 = pd.Series({'a': 100, 'b': 90, 'c': 80, 'd': 90})
print(sr0, type(sr0))

ser = pd.Series([1, 2, 3, 4, 5])
print(ser)
ser.index = [f'{x}번' for x in range(5)]
print(ser)

print("6번" in ser, "1번" in ser) # False True

data = {'국어': 100, '수학': 50, '영어': 70, '과학': 90}
print(data)
new_index = ['국어', '수학', '영어', '사회']
ser = pd.Series(data, index=new_index) # 기존 index가 변경
print(ser)
printt("기존 index와 새로운 index가 일치하지 않을 경우 주의")
ser.index.name = '과목명'
printt("Series는 1차원이기 때문에 column 이름 변경 불가")
print(ser)

# series 연산할 때 한쪽이라도 없는 값은 Nan발생
sr1 = pd.Series([10, 20, 30, 40], index=['Java', 'Python', 'TypeScript', 'c#'])
sr2 = pd.Series([80, 70, 60, 50], index=['Java', 'Python', 'TypeScript', 'c#'])
sr3 = pd.Series([11, 22, 33, 44], index=['Java', 'LISP', 'Ada', 'C++'])

sr12 = sr1 + sr2
print(sr12)  # index가 같을 경우

sr13 = sr1 + sr3
print(sr13)  # index가 다른 경우