import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time

import torch
import torchvision
from torch import nn
from torchinfo import summary
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import f1_score

# 하이퍼 파라미터
MY_EPOCH = 2
MY_BATCH = 64

# 임의의 수 생성 씨앗 설정
torch.manual_seed(111)

# 3차원 데이터 변환 방식 지정
# 1. pytorch 텐서로 전환
mean = [0.5, 0.5, 0.5]
std = [0.5, 0.5, 0.5]
rules = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=mean, std=std)])

# 학습용 데이터 로더
train_loader = DataLoader(
    CIFAR10('cifar', train=True, download=True, transform=rules),
    batch_size=MY_BATCH,
    shuffle=True
)

# 평가용 데이터 로더
test_loader = DataLoader(
    CIFAR10('cifar', train=False, download=True, transform=rules),
    batch_size=MY_BATCH,
    shuffle=False
)

# 이미지 출력 함수
def sample(img):
    # 화소 정보 [-1, 1] 에서 [0, 1]로 전환
    img = img / 2 + 0.5

    # RGB 채널 정보를 마지막으로 이동
    npimg = img.numpy()
    print('전환 전 모양:', npimg.shape)

    flip = np.transpose(npimg, (1, 2, 0))
    print('전환 후 모양:', flip.shape)

    plt.imshow(flip)
    plt.axis('off')
    plt.show()

dataiter = iter(train_loader)
images, labels = next(iter(train_loader))

merged = torchvision.utils.make_grid(images)
sample(merged)

model = nn.Sequential(
    # batch: 64, inChannel: 3, w: 32, h: 32 :: 64*3*32*32
    # out_channels :: 6개의 특징 맵을 만들어 냄
    # kernel_size 필터 :: 3*2*2
    # 출력크기 = (입력크기+2P-K)/S + 1 :: (32-2)/1+1 =31
    nn.Conv2d(3,6, kernel_size=2),
    nn.ReLU(), # 음수 -> 0, 양수 -> 그대로
    # 특징 맵의 크기를 줄이는 역할 :: (31-2)/2 +1 = 15
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(6, 16, kernel_size=2),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(16*14*14, 120),
    nn.Linear(120, 84),
    nn.Linear(84, 10),
    nn.Softmax(dim=1)
)

print('\n=== model 요약 ===')
summary(model, (3, 32, 32))

########## 인공 신경망 학습 ##########
# 최적화 함수와 손실 함수 지정
optimizer = torch.optim.Adagrad(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# CNN 학습
begin = time()
print('\nCNN 학습 시작')

for epoch in range(MY_EPOCH):
    batch = 0
    for data in train_loader:
        inputs, labels = data
        outputs = model(inputs)

        # 손실값 계산
        loss = criterion(outputs, labels)
        print('  배치:', batch,' 손실: {:.3f}'.format(loss.item()))

        # 역전파 알고리즘으로 가중치 보정
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        batch += 1

    # 손실값 출력
    print('에포크: {},'.format(epoch),'손실: {:.3f}'.format(loss.item()))
end = time()
print('최종 학습 시간: {:.1f}초'.format(end - begin))


########## 인공 신경망 평가 ##########
# 이미지 라벨
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']
# 혼동 행렬 초기화
correct = 0
confusion = np.zeros([10, 10], int)


# 평가용 데이터로 CNN 평가
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        outputs = model(images)

        # 1차원 축으로 최대치 찾아 내기
        _, pred = torch.max(outputs, dim=1)

        # 혼동행렬 업데이트
        for i, truth in enumerate(labels):
            if (truth.item() == pred[i]):
                correct += 1
            confusion[pred[i].item(), truth.item()] += 1


# 최종 정확도 출력
print('\n최종 정확도: {:.2f}%'
      .format(correct / 10000 * 100))


# 카테고리별 정확도 출력
print('카테고리별 Precision:')
for i, row in enumerate(confusion):
    print('{0:10s} : {1:.1f}%'
          .format(classes[i], row[i]/np.sum(row)*100))


# 혼동 행렬 출력
print('\n혼동 행렬:')
print(confusion)


# 평가용 마지막 batch (16개 데이터) 결과
print('\n마지막 batch 데이터 모양:', data[0].shape)
print('예상:', pred)
print('정답:', labels)