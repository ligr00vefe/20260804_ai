# pip install scikit-learn

from sklearn.neighbors import KNeighborsClassifier

# 학습 데이터
X = [[1,40],[2,50],[3,60],[4,65],[5,70],[6,80]]

# 평가 데이터(정답)
y = ["Fail", "Fail", "Pass", "Pass", "Pass", "Pass"]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

new_neighbors = [[3.5, 62]]
prediction = knn.predict(new_neighbors)
print(prediction)