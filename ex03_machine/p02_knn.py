import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

figure = plt.figure()
data = pd.read_csv('Fish.csv')

bream_length = data.loc[:, 'Length2'].tolist()

bream_length = data.loc[data.Species == 'Bream', ['Length2']]
print(bream_length);
print(type(bream_length))
bream_length = bream_length.iloc[:, 0].tolist()
print(bream_length);
print(type(bream_length))
bream_weight = data.loc[data.Species == 'Bream', ['Weight']].iloc[:, 0].to_list()

plt.scatter(bream_length, bream_weight)
plt.title('Bream')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

smelt_length = data.loc[data.Species == 'Smelt', ['Length2']].iloc[:, 0].to_list()
smelt_weight = data.loc[data.Species == 'Smelt', ['Weight']].iloc[:, 0].to_list()

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.title('Bream & Smelt')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

length = bream_length + smelt_length
weight = bream_weight + smelt_weight
print(len(bream_length), len(smelt_length))
fish_data = [[l, w] for l, w in zip(length, weight)]  # 2차원 List
print(fish_data)
fish_target = [1] * 35 + [0] * 14
print(fish_target)


kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
score = kn.score(fish_data, fish_target)

print("정확도: %.1f" % score)

l = 30; w = 600
plt.scatter(l, w, marker='^', color='red')
plt.show()

print(kn.predict([[l, w]]))

kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data, fish_target)
score = kn49.score(fish_data, fish_target)
print("score:",score)
print("35/49",35/49)

