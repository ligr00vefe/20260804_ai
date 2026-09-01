import matplotlib.pyplot as plt
import numpy as np


# 1번 일반적인 히스토그램 챠트
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
# bins 기본값은 10, 히스토그램의 가로축 구간의 개수를 지정
# plt.hist(weight, bins=13, label='bins=12')
plt.hist(weight, bins=30, label='bins=30')
plt.legend()
plt.show()


# 2번 hist에 plt.text를 적용하려는 경우
np.random.seed(0)
# np.random.normal 정규 분포 함수
# [정규분포] 평균 0, 표준편차 1, 개수 100개
x = np.random.normal(0, 1, 100)
# print(x)
plt.figure(figsize=(10, 6))
# histogram의 경우 내가 값 리스트를 넣고,
# 입력한 bin 개수에 따라 알아서 분류해 줌
# ys: y값,
# xs: x 값
ys, xs, patches = plt.hist(x,
                           bins=5,  ## 몇 개의 바구니로 구분할 것인가.
                           density=True,  ## ytick을 퍼센트비율로 표현해줌
                           cumulative=False,  ## 누적으로 표현하고 싶을 때는 True
                           histtype='bar',  ## 타입. or step으로 하면 모양이 바뀜.
                           orientation='vertical',  ## or horizontal
                           rwidth=0.8,  ## 1.0일 경우, 꽉 채움 작아질수록 간격이 생김
                           color='hotpink',  ## bar 색깔
                           )
for i in range(0, len(ys)):
  plt.text(x=xs[i] + 0.23, y=ys[i] + 0.015,
           s='{:.1f}%'.format(ys[i] * 100),
           # fonsize=20,
           color='red')
y_min, y_max = plt.ylim()  # 글자가 안보일 경우 위의 길이 늘림
plt.ylim(y_min, y_max + 0.05)
plt.yticks([])
plt.xticks([(xs[i] + xs[i + 1]) / 2 for i in range(0, len(xs) - 1)],
           ["{:.1f} ~ {:.1f}".format(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1)])
plt.legend()
plt.show()