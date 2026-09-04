import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time import time

import torch
from torch import nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import f1_score
import numpy as np

#하이퍼 파라미터
INPUT_DIM = 13
MY_HIDDEN = 1000
MY_EPOCH = 1000

pd.set_option('display.max_columns', None) # 출력할 컬럼수를 조정하지 않겠다.
torch.manual_seed(111)
np.random.seed(111)

raw = pd.read_csv("heart.csv")
raw = raw.sample(frac=1).reset_index(drop=True) # 섞은 후 인덱스 재조정
raw = raw.drop(raw.index[100:])

print('원본 데이터 샘플 10개')
print(raw.head(10))
print('원본 데이터 통계')
print(raw.describe())

# 입력 데이터 작업
X_data = raw.drop('target', axis=1) # 입력데이터
Y_data = raw['target'] # 라벨링, 결과

names = X_data.columns
print(names)

# 데이터를 train(훈련용, 학습용)과 test(평가용)으로 분리
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=111)

# shape 출력
print('학습용 입력 데이터 shape:', X_train.shape)
print('학습용 출력 데이터 shape:', Y_train.shape)
print('평가용 입력 데이터 shape:', X_test.shape)
print('평가용 출력 데이터 shape:', Y_test.shape)

scaler = StandardScaler() # z-점수 정규화
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.fit_transform(X_test)
# print(type(X_train)) # numpy

# numpy에서  pandas 로 변경
# header 정보 복구 필요
X_train = pd.DataFrame(X_train, columns=names)
X_test = pd.DataFrame(X_test, columns=names)

print('z-점수 정규화 된 학습용 데이터 샘플 10개')
print(X_train.head(10))
print('z-점수 정규화된 데이터의 통계 출력')
print(X_train.describe())

# 박스플롯으로 챠트 표시
# sns.set_theme(font_scale=2)
# sns.boxplot(data=X_train, palette="colorblind")
# plt.show()

print("{0:=^20}".format('인공 신경망 구현'))
model = nn.Sequential(
  nn.Linear(INPUT_DIM, MY_HIDDEN),
  nn.Tanh(),

  nn.Linear(MY_HIDDEN, MY_HIDDEN),
  nn.Tanh(),
  nn.Linear(MY_HIDDEN, 1),

  # nn.Linear(MY_HIDDEN, 5000),
  # nn.Tanh(),
  # nn.Linear(5000, 1),

  nn.Sigmoid()
)
print('DNN 요약')
print(model)

# numel() : torch Tensor의 크기 구함
# p는 가중치라고 보는게 맞음
total = sum(p.numel() for p in model.parameters())
print('총 파라미터 수 : {:,}'.format(total))

print("{0:=^20}".format('인공 신경망 학습'))

# 최적 함수와 손실 함수 지정
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# RMSprop은 최적화 도중, 학습율을 상황에 맞게 조절하는 기술을 SGD에 추가, SGD보다 진화된 알고리즘
# optimizer = torch.optim.RMSprop(model.parameters(), lr=0.01)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

# 학습용 데이터 전환
# pandas dataframe에서 python tensor로 변환
X_train = torch.tensor(X_train.values).float()
Y_train = torch.tensor(Y_train.values).float()

# DNN 학습
begin = time()
print("{0:=^20}".format('DNN 학습 시작'))

for epoch in range(MY_EPOCH):
  output = model(X_train)
  # 출력값 차원을 (212,1)에서 (212,)로 조정
  output = torch.squeeze(output)
  # 손실값 계산
  loss = criterion(output, Y_train)
  # 손실값 출력
  if(epoch % 10 == 0):
    print('Epoch: {:3},'.format(epoch), 'Loss: {:.3f}'.format(loss.item()))

  # 역전파 알고리즘으로 가중치 보정
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
end = time()
print('최종 학습 시간: {:.1f}초'.format(end - begin))

print("{0:=^20}".format('인공 신경망 평가'))
# 평가 데이터 타입 변환
# padas dataframe에서 pytorch 텐서로 변환
X_test = torch.tensor(X_test.values).float()

# DNN으로 추축, 가중치 관련 계산 불필요
with torch.no_grad(): # 이후부터는 기울기 계산을 하지 않는다.
  pred = model(X_test) # DNN은 학습이 끝났기 때문에 기울기 계산을 할 필요가 없다.
  # 시간을 줄여주는 효과

# print('pred:', pred)
pred = pred.numpy() #추축 결과 tensor타입을 numpy로 전환

pred =(pred > 0.5)
print(pred.flatten())

f1 = f1_score(Y_test, pred)
print("최종 정확도 (F1 점수): {:.3f}".format(f1))