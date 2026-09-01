'''
pandas : Panel Datas의 줄임말
목적: 엑셀과 같은 기능을 구현하기 위함.
엑셀은 데이터가 많으면 느려지지만, 판다스는 빠름.
고성능 수치 계산을 위한 라이브러리이며, 다차원 배열을 다루는 데 특화,
쉽고 빠르게 데이터를 분석하고 차트 기능 지원
벡터화, 선형대수, 난수 생성, 수학 함수 등에 최적화
판다스의 핵심 자료 형태가 dataframe 이다.

|Part| 주제                   | 핵심 내용                                 |
| - | ---------------------- | ---------------------------------------- |
| 1 | Pandas 소개            | Pandas의 역할, NumPy와 차이                |
| 2 | Series / DataFrame    | Pandas의 핵심 자료구조                      |
| 3 | 데이터 조회            | `loc`, `iloc`, 조건 필터링                  |
| 4 | 데이터 탐색            | `info`, `describe`, `value_counts` 등      |
| 5 | 데이터 정제            | 결측치, 중복, 이상값, 자료형                  |
| 6 | 데이터 변환            | 정렬, 새로운 컬럼, `apply`, `map`            |
| 7 | 데이터 집계결합        | `groupby`, `agg`, `merge`, `concat`,`pivot`|
| 8 | 파일 입출력 + 실전 분석 | CSV, Excel, JSON + 미니 프로젝트             |
'''

import pandas as pd
import numpy as np

from utils.functions import printt

# ============================================================
printt("1. Pandas 소개")
# ============================================================
print("\n[NumPy 배열]")
data = np.array([
    [101, "홍길동", 20, 85],
    [102, "김철수", 21, 92],
    [103, "이영희", 20, 78]
])
print(data)
print("""넘파이가 데이터를 다룰 수 있지만,
각 열의 의미,문자열/숫자 자료형,결측값,행/열 이름,조건 검색,
그룹별 통계 등을 다루기에는 불편
Python
   │
   ├── NumPy
   │     └── 수치 계산 / 배열
   │
   └── Pandas
         └── 표 형태 데이터 / 데이터 분석
""")

# ============================================================
printt("2. Series")
# ============================================================
'''
pandas의 3가지 자료구조
1) Series(1차원 데이터 자료)
2) DataFrame(2차원)
3) Panel(3차원) 데이터 자료구조
p02_pandas_series 참조
'''
s = pd.Series([90, 80, 70])

print("\n[Series]")
print(s)

print("\n[Series Index]")
print(s.index)

print("\n[Series Values]")
print(s.values)

print("\n[Series dtype]")
print(s.dtype)

print("\n[Series shape]")
print(s.shape)


# index를 직접 지정
s = pd.Series(
    [90, 80, 70],
    index=["국어", "영어", "수학"]
)

print("\n[Index를 지정한 Series]")
print(s)


# ============================================================
printt("3. DataFrame")
# ============================================================
df = pd.DataFrame({
    "id": [101, 102, 103, 104, 105],
    "name": ["홍길동", "김철수", "이영희", "박민수", "최수진"],
    "age": [20, 21, 20, 22, 21],
    "score": [85, 92, 78, 95, 88],
    "department": ["컴퓨터", "전자", "컴퓨터", "전자", "컴퓨터"]
})

print("\n[DataFrame]")
print(df)

print("\n[Index]")
print(df.index)

print("\n[Columns]")
print(df.columns)

print("\n[Values]")
print(df.values)

print("\n[dtypes]")
print(df.dtypes)

print("\n[Shape]")
print(df.shape)

print("\n dict -> dataframe")
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


# ============================================================
printt("4. 데이터 열 선택")
# ============================================================
print("\n[이름 열]")
print(df["name"])

print("\n[이름과 점수 열]")
print(df[["name", "score"]])

print("\n[score의 타입]")
print(type(df["score"]))

print("\n[score를 DataFrame으로 선택]")
print(type(df[["score"]]))


# ============================================================
printt("5. 행 선택")
# ============================================================
print("\n[첫 번째 행 - iloc]")
print(df.iloc[0])

print("\n[첫 번째부터 세 번째 행 - iloc]")
print(df.iloc[0:3])

print("\n[첫 번째 행 - loc]")
print(df.loc[0])


# ============================================================
printt("6. 조건 검색")
# ============================================================
print("\n[점수가 90점 이상인 학생]")
print(df[df["score"] >= 90])

print("\n[점수가 80점 이상이고 나이가 21세 이상]")
print(
    df[
        (df["score"] >= 80) &
        (df["age"] >= 21)
    ]
)

print("\n[컴퓨터학과 학생]")
print(df[df["department"] == "컴퓨터"])


# ============================================================
printt("7. 데이터 탐색")
# ============================================================
print("\n[head()]")
print(df.head())

print("\n[tail()]")
print(df.tail())

print("\n[info()]")
df.info()

print("\n[describe()]")
print(df.describe())

print("\n[shape]")
print(df.shape)

print("\n[columns]")
print(df.columns)

print("\n[dtypes]")
print(df.dtypes)


# ============================================================
printt("8. 범주형 데이터 탐색")
# ============================================================
print("\n[학과별 학생 수]")
print(df["department"].value_counts())

print("\n[학과 종류]")
print(df["department"].unique())

print("\n[학과 개수]")
print(df["department"].nunique())


# ============================================================
printt("9. 결측값")
# ============================================================
df_missing = df.copy()

# 결측값 추가
df_missing.loc[2, "score"] = np.nan
df_missing.loc[4, "age"] = np.nan

print("\n[결측값이 포함된 데이터]")
print(df_missing)

print("\n[결측값 확인]")
print(df_missing.isnull())

print("\n[컬럼별 결측값 개수]")
print(df_missing.isnull().sum())

print("\n[결측값 제거]")
print(df_missing.dropna())

print("\n[결측값을 0으로 변경]")
print(df_missing.fillna(0))

print("\n[score 결측값을 평균으로 변경]")
df_missing["score"] = df_missing["score"].fillna(
    df_missing["score"].mean()
)
print(df_missing)


# ============================================================
printt("10. 중복 데이터")
# ============================================================
df_duplicate = pd.concat(
    [df, df.iloc[[0]]],
    ignore_index=True
)

print("\n[중복 데이터]")
print(df_duplicate)

print("\n[중복 여부]")
print(df_duplicate.duplicated())

print("\n[중복 데이터 제거]")
print(df_duplicate.drop_duplicates())


# ============================================================
printt("11. 자료형 변경")
# ============================================================
print(df)
df_type = df.copy()

print("\n[변경 전]")
print(df_type.dtypes)

df_type["age"] = df_type["age"].astype(float)

print("\n[변경 후]")
print(df_type.dtypes)


# ============================================================
print("12. 새로운 컬럼 생성")
# ============================================================
df2 = df.copy()

df2["bonus"] = 10

df2["total"] = df2["score"] + df2["bonus"]

print("\n[새로운 컬럼 추가]")
print(df2)


# ============================================================
printt("13. apply()")
# ============================================================
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"


df2["grade"] = df2["score"].apply(grade)

print("\n[등급 컬럼 추가]")
print(df2)


# lambda 사용
df2["result"] = df2["score"].apply(
    lambda x: "합격" if x >= 60 else "불합격"
)

print("\n[합격 여부]")
print(df2)


# ============================================================
printt("14. 데이터 정렬")
# ============================================================
print("\n[점수 오름차순]")
print(
    df.sort_values("score")
)

print("\n[점수 내림차순]")
print(
    df.sort_values(
        "score",
        ascending=False
    )
)

print("\n[학과 오름차순 + 점수 내림차순]")
print(
    df.sort_values(
        ["department", "score"],
        ascending=[True, False]
    )
)


# ============================================================
printt("15. GroupBy")
# ============================================================
print(df)
print("\n[학과별 평균 점수]")
print(
    df.groupby("department")["score"].mean()
)

print("\n[학과별 최고 점수]")
print(
    df.groupby("department")["score"].max()
)

print("\n[학과별 최소 점수]")
print(
    df.groupby("department")["score"].min()
)

print("\n[학과별 통계]")
print(
    df.groupby("department").agg({
        "score": ["mean", "max", "min"],
        "age": "mean"
    })
)


# Named Aggregation
print("\n[Named Aggregation]")
print(
    df.groupby("department").agg(
        avg_score=("score", "mean"),
        max_score=("score", "max"),
        min_score=("score", "min"),
        avg_age=("age", "mean")
    )
)


# ============================================================
printt("16. concat()")
# ============================================================
df1 = pd.DataFrame({
    "id": [101, 102],
    "name": ["홍길동", "김철수"]
})

df2 = pd.DataFrame({
    "id": [103, 104],
    "name": ["이영희", "박민수"]
})

print("\n[df1]")
print(df1)

print("\n[df2]")
print(df2)

print("\n[세로 결합]")
print(
    pd.concat(
        [df1, df2],
        ignore_index=True
    )
)


# ============================================================
printt("17. merge()")
# ============================================================
customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["홍길동", "김철수", "이영희"]
})

orders = pd.DataFrame({
    "customer_id": [1, 1, 2, 3],
    "product": ["노트북", "마우스", "키보드", "모니터"],
    "sales": [1500000, 30000, 50000, 300000]
})

print("\n[고객 데이터]")
print(customers)

print("\n[주문 데이터]")
print(orders)

print("\n[Inner Join]")
print(
    pd.merge(
        customers,
        orders,
        on="customer_id",
        how="inner"
    )
)

print("\n[Left Join]")
print(
    pd.merge(
        customers,
        orders,
        on="customer_id",
        how="left"
    )
)


# ============================================================
printt("18. pivot_table()")
# ============================================================
sales = pd.DataFrame({
    "region": [
        "부산", "부산", "서울",
        "서울", "대구", "대구"
    ],
    "year": [
        2024, 2025, 2024,
        2025, 2024, 2025
    ],
    "sales": [
        100, 150, 200,
        250, 80, 120
    ]
})

print("\n[판매 데이터]")
print(sales)

print("\n[지역별/연도별 매출]")
print(
    pd.pivot_table(
        sales,
        values="sales",
        index="region",
        columns="year",
        aggfunc="sum"
    )
)


# ============================================================
printt("19. crosstab()")
# ============================================================
students = pd.DataFrame({
    "gender": ["남", "여", "남", "여", "남", "여"],
    "result": [
        "합격", "합격", "불합격",
        "합격", "합격", "불합격"
    ]
})

print("\n[학생 데이터]")
print(students)

print("\n[성별 합격 여부]")
print(
    pd.crosstab(
        students["gender"],
        students["result"]
    )
)


# ============================================================
print("20. 날짜 데이터")
# ============================================================
date_df = pd.DataFrame({
    "date": [
        "2026-01-15",
        "2026-02-20",
        "2026-03-10"
    ],
    "sales": [100, 150, 200]
})

print("\n[문자열 날짜]")
print(date_df)

date_df["date"] = pd.to_datetime(
    date_df["date"]
)

print("\n[datetime으로 변환]")
print(date_df)

print("\n[연도]")
print(date_df["date"].dt.year)

print("\n[월]")
print(date_df["date"].dt.month)

print("\n[일]")
print(date_df["date"].dt.day)


# ============================================================
printt("21. CSV 파일 입출력")
# ============================================================
# 저장
df.to_csv(
    "../source/students.csv",
    index=False
)

print("\nstudents.csv 파일 저장 완료")

# 읽기
csv_df = pd.read_csv("../source/students.csv")

print("\n[CSV 파일 읽기]")
print(csv_df)


# ============================================================
printt("22. Excel 파일 입출력")
# ============================================================
# pip install openpyxl
df.to_excel(
    "../source/students.xlsx",
    index=False
)

print("\nstudents.xlsx 파일 저장 완료")

excel_df = pd.read_excel(
    "../source/students.xlsx"
)

print("\n[Excel 파일 읽기]")
print(excel_df)


# ============================================================
printt("23. 실전 데이터 분석")
# ============================================================
final_df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "region": [
        "부산", "서울", "부산",
        "대구", "서울", "부산"
    ],
    "product": [
        "노트북", "마우스", "키보드",
        "노트북", "모니터", "마우스"
    ],
    "price": [
        1500000, 30000, 50000,
        1400000, 300000, 35000
    ],
    "quantity": [1, 3, 2, 1, 2, 4]
})

print("\n[원본 데이터]")
print(final_df)

# 매출 계산
final_df["sales"] = (
    final_df["price"] *
    final_df["quantity"]
)

print("\n[매출 컬럼 추가]")
print(final_df)

# 지역별 매출
print("\n[지역별 매출]")
print(
    final_df.groupby("region")["sales"]
    .sum()
)

# 상품별 매출
print("\n[상품별 매출]")
print(
    final_df.groupby("product")["sales"]
    .sum()
)

# 상품별 판매수량
print("\n[상품별 판매수량]")
print(
    final_df.groupby("product")["quantity"]
    .sum()
)

# 매출이 높은 순서
print("\n[매출 높은 순서]")
print(
    final_df.sort_values(
        "sales",
        ascending=False
    )
)

print("\n" + "=" * 60)
print("Pandas 전체 실습 종료")
print("=" * 60)