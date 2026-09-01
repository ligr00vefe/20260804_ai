import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#seaborn에서 제공하는 flights 데이터 셋을 사용
flights = sns.load_dataset('flights')

#그래프 사이즈 설정
plt.figure(figsize=(12, 3))
print(len(flights.index))
colors = np.random.rand(12)
sns.barplot(data=flights, x="year", y="passengers")
# sns.boxplot(data=flights, x="year", y="passengers")
# sns.violinplot(data=flights, x="year", y="passengers")
# sns.swarmplot(data=flights, x="year", y="passengers")
# sns.lineplot(data=flights, x="year", y="passengers")
# sns.distplot(flights["passengers"])

plt.summer()
plt.show()