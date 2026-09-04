from random import shuffle

import torch
from PIL.Image import Transform  # 이미지를 기하학적으로 변형할때 사용하는 상수값들을 모아둔 클래스.import

hello = torch.nn.Linear(5, 3)
data = torch.randn(2, 5)  # 평균이 0이고, 표준편차가 1인 가우시안 표준정규분포에서
# 임의의 숫자를 뽑아 2행 5열의 텐서를 만듦.
print(data)  # 2행 5열의 텐서를 생성
# data 텐서를 선형레이어에 통과해서 2행 3열의 새로운 텐서를 생성.
print(hello(data))

from torchvision.datasets import MNIST
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn as nn
from torchinfo import summary

# Mnist 데이터가 numpy형태이기 때문에 pytorch의 tensor로 변환하기 위한 방식 지정
rules = transforms.Compose([transforms.ToTensor()])

train_loader = DataLoader(
    MNIST('mnist', train=True, transform=rules, download=True), batch_size=500, shuffle=True,
)
test_loader = DataLoader(
    MNIST('mnist', train=False, transform=rules, download=True), batch_size=500, shuffle=False,
)

images, labels = next(iter(train_loader))
print(images[0]); print(labels[0])

model = nn.Sequential(
    nn.Flatten(), # 2차원 텐서를 1차원으로 변환
    nn.Linear(784,128), # 입력값의 간소화(입력:784,w:784,bias:1,f(x):128)
    nn.ReLU(), # 음수의 값을 0으로 변환
    nn.Dropout(p=0.2),
    nn.Linear(128, 10),
    nn.Softmax(dim=1)# 10개의 확률값이 있는 축을 따라 가장 큰 값을 가져 와라
)
print("\n=== DNN Summary ===")
summary(model, input_size=(1, 28, 28))

optimizer = torch.optim.Adam(model.parameters())

criterion = nn.CrossEntropyLoss()

for epoch in range(5):
    for data in train_loader:
        inputs, labels = data
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()  # 이전의 가중치를 0으로 만들어주고
        loss.backward() # 다신 손실함수의 값을 가중치(기울기) 반영
        optimizer.step() # 기울기의 보정치를 구하는 역할

    print('Epoch: {},'.format(epoch), 'Loss: {:.3f}'.format(loss.item()))

#  DNN 모델의 평가
correct = 0
for images, labels in test_loader:
    with torch.no_grad():
        pred = model(images)
    pred = torch.argmax(pred, 1)
    for i in range(500):
        if(pred[i] == labels[i]):
            correct += 1

print("\n=== DNN Accuracy ===")
print(correct / 10000)