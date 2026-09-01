import torch
from PIL.Image import Transform # 이미지를 기하학적으로 변형할 때 사용하는 상수값들을 모아둔 클래스.

hello = torch.nn.Linear(5, 3)
data = torch.randn(2, 5) # 평균이 0이고, 표준편차가 1
# 임의의 숫자를 뽑아 2행 5열의 텐서를 만듦.
print(data)
print(hello(data))

from torchvision.datasets import MNIST
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn as nn
from torchinfo import summary

# Mnist 데이터가 numpy 형태이기 때문에 pytorch의 tensor로 변환하기 위한 방식 지정
rules = transforms.Compose([transforms.ToTensor()])

train_loader = DataLoader(
    MNIST('mnist', train=True, transform=rules, download=True), batch_size=500, shuffle=True,
)
test_loader = DataLoader(
    MNIST('mnist', train=False, transform=rules, download=True), batch_size=500, shuffle=False,
)

