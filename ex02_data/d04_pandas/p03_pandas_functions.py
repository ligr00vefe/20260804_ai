import pandas as pd

from utils.functions import printt

# CSV 파일 불러오기
# df = pd.read_csv('../source/singer1.csv', encoding='cp949')

# Excel 파일 불러오기
df = pd.read_excel('../source/singer.xls')

# 데이터프레임 정보 확인하기
print("df.info() :: ", df.info())

# 데이터프레임 일부 데이터 보기 5 row
print("df.head() :: ", df.head())

# 데이터프레임 요약 통계량 보기
print("df.describe() :: ", df.describe())

# 열 선택하기
# df['열 이름']

# 여러 개의 열 선택하기
# df[['열 이름 1', '열 이름 2', ...]]

# 행 선택하기
# df.loc[행 이름 또는 인덱스]

# 여러 개의 행 선택하기
# df.loc[[행 이름 또는 인덱스 1, 행 이름 또는 인덱스 2, ...]]

# 조건 필터링하기
# 2010년 이후의 데이터만 선택하기
# df[df['Year'] >= 2010]

# 논리 연산자 이용하기
# df[(조건식 1) & (조건식 2)]
# df[(조건식 1) | (조건식 2)]

# isin() 함수 이용하기: 특정한 값이 포함된 데이터만 선택
# df[df['열 이름'].isin([값1, 값2, ...])]

# 'KOR', 'USA', 'JPN' 국가의 데이터만 선택하기
# df[df['NOC'].isin(['KOR', 'USA', 'JPN'])]

# groupby() 함수 이용하기
# df.groupby('열 이름')

'''
# 집계 함수 이용하기
count() : 데이터의 개수를 세는 함수
sum() : 데이터의 합을 구하는 함수
mean() : 데이터의 평균을 구하는 함수
median() : 데이터의 중앙값을 구하는 함수
min() : 데이터의 최소값을 구하는 함수
max() : 데이터의 최대값을 구하는 함수
std() : 데이터의 표준편차를 구하는 함수
var() : 데이터의 분산을 구하는 함수
'''

# 오름차순으로 정렬하기
# df.sort_values('열 이름')

# 내림차순으로 정렬하기
# df.sort_values('열 이름', ascending=False)


printt("Exercise")
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 32, 18, 47],
        'city': ['New York', 'Paris', 'London', 'San Francisco']}
df = pd.DataFrame(data)
print(df)
print(df.sort_values('age'))

df.set_index('name', inplace=True)
print(df)
print(df.reset_index())