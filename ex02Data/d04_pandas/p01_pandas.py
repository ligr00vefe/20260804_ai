
import pandas as pd

from utils.functions import printt
df = pd.DataFrame({
    "id": [101, 102, 103],
    "name": ["홍길동", "김철수", "이영희"],
    "score": [85, 92, 78]
})
print(df)

data = {
  'Name'  : ['Thor', 'Hulk', 'Captain', 'IronMan'],
  'HP'    : [100, 90, 70, 75],
  'Armor' : [80, 100, 70, 60]
}
print(type(data))
df1 = pd.DataFrame(data)
print(df1)

df2 = pd.DataFrame(data, index=['하나', '둘', '셋', '넷'])
print(df2)

printt("Pandas의 속성")
print(df1.index)
print(df2.index)
print(df2.columns)

printt("Pandas의 접근")
printt("열 선택")
avengers = df2['Name'] # columns(열)로 출력
print(avengers)
avengers.name = 'Avengers' # Name: Name -> Name:Avengers
print(avengers)
printt("행 선택")
# iloc → 위치(position), loc  → label
print(df.iloc[0])
print(df.loc[0])
avengers2 = df2.loc['둘'] # index(행)로 출력
print(avengers2)
printt()
print(df2.loc['넷']['Name']) #행과 열로 값을 출력
print(df2.loc['넷', 'Name']) #행과 열로 값을 출력
print(df2.iloc[3, 0]) #행과 열로 출력 OK

print("===================================")
# 열 추가
df2['Weapon'] = ['묠니르','주먹','방패','슈트']
print(df2)
# 열 수정 및 추가
df2['Weapon'] = pd.Series(
  ['방패','슈트','묠니르'],
  index=['셋','넷','하나'])
print(df2)

# 행 추가
df2.loc['다섯'] = ['Spidy', 65, 65, '거미줄']
print(df2)
# 복수의 행 추가
new_data = {'Name':['Grute', 'Starlord', 'rocket'],
            'Weapon':['나무','총','총']}
new_df = pd.DataFrame(new_data, index=['여섯', '일곱', '여덟'])
df2 = pd.concat([df2, new_df])
print(df2)

df2 = df2.drop(['Weapon','Armor'],axis=1) #열로 지우기
print(df2)
df2 = df2.drop(['여섯','일곱','여덟'],axis=0) #행으로 지우기
print(df2)

printt("조건 검색")
print(df)
print(df[df["score"] >= 90])
printt("복수 조건")
print(df[
    (df["id"] >= 102) &
    (df["score"] >= 70)
])

printt("데이터 탐색")
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.index)
print(df["id"].unique())
print(df["name"].nunique())
print(df["score"].value_counts())

printt("데이터 정제")
printt("결측값")
print(df.isnull())
print(df.isnull().sum())
print(df.dropna()) # 결측값 제거
print(df.fillna(0)) # 결측값 대체
print(df["score"].fillna(df["score"].mean()))
print(df.duplicated())
print(df.drop_duplicates())
