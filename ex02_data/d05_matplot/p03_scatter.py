import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0) # seed를 고정하여 랜덤한 숫자를 일률적으로 생성

n = 50
x = np.random.rand(n) # 0 ~ 1까지 랜덤한 실수 50개 생성
y = np.random.rand(n) # 0 ~ 1까지 랜덤한 실수 50개 생성
print(x)
plt.scatter(x, y)
plt.show()

# np.random.randint(10) 0~9까지의 랜덤한 숫자 1개를 생성
# np.random.rand(10) 0~1사이의 난수 10개를 생성

area = (30 * np.random.rand(n)) ** 2 # 한점당 영역을 50개 생성
# print(area, len(area))
colors = np.random.rand(n) # 색상도 50개 생성

plt.scatter(x, y, s=area, c=colors)
# # plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='spring')
plt.colorbar()
plt.show()