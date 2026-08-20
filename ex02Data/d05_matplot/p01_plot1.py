import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
import numpy as np

# Line Chart(선도표) :: y축에 대한 데이터만 있을 경우
# 점들을 연결하여 데이터의 변화를 직선적으로 관찰할 수 있다.
data = [100, 250, 140, 300, 500]
# plt.plot(data); plt.show()

# Line Chart(선도표) :: x, y축에 대한 데이터로 차트를 표기
# 점들을 연결하여 데이터의 변화를 직선적으로 관찰할 수 있다.
# o, s, p, d, $영문자$, x, +, ^,<,>,v
# -(solid), --(dashed), :(dotted), -.(dash-dot)
# color명으로 색상 지정, #RRGGBB, b,g,r,c,m,y,k,w
xdata = [10, 20, 30, 40, 50]
ydata = [10000, 15000, 33000, 34000, 60000]
# plt.plot(xdata, ydata); plt.show()
# plt.plot(xdata, ydata, color='green'
#          , linestyle='-.', marker='d'); plt.show()
# plt.plot(xdata, ydata, 'rs'); plt.show()
# plt.plot(xdata, ydata, 'rs'); plt.show()

# plt.plot([4, 5, 6], marker="1") # 1,2,3,4
# plt.plot([3, 4, 5], marker="H") # D, d, s, p, *, h, H
# plt.plot([2, 3, 4], marker="|") # x, +, |, _
# plt.plot([1, 2, 3], marker='*') # ., o, *, p, P
# plt.plot([0, 1, 2], marker='$Z$') # $영문자$
# plt.show()

# x = [1, 2, 3, 4]
# y = [2, 3, 5, 10]
#
# plt.plot(x, y)
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# x의 인덱스로 범위를 지정, 2단계 이하만 적용
# plt.fill_between(x[1:3], y[1:3], alpha=0.5)
# plt.fill_betweenx(y[2:4], x[2:4], alpha=0.5)
# plt.show()


# x = np.linspace(-10, 10, 100)
# y = x ** 3
#
# plt.plot(x, y)

# 축의 원점을 기준으로 양, 음의 방향이 대칭적인 로그 스케일로 표시
# Symmetrical Log Scale :: symlog
# plt.xscale('symlog')
#
# plt.show()

# start: 시작, stop: 끝, num: 단계(단계가 클수록 부드러워짐)
# x = np.linspace(0, 5, 100)
# y = np.exp(x)

# plt.plot(x, y)
# plt.yscale('linear')
# plt.yscale('log')
# plt.yscale('symlog')
# plt.yscale('logit')
# plt.show()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 2, 0.2)
plt.plot(x, x, 'b')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.grid(True)
plt.xticks([0,1,2], labels=['가', '나', '다'])
plt.yticks(np.arange(1,6), labels=['A','B','C','D','E'])
plt.axhline(1.0, 0.1, 0.9, color='pink',
            linestyle="--", linewidth=3)
plt.hlines(2.0,0.2, 1.6, color='red',
           linestyle="solid", linewidth=3)
plt.axvline(0.6, 0.2, 0.8, color='lime',
            linestyle="--", linewidth=2)
plt.vlines(1.5, 0.5, 4.5, color='gray',
            linestyle="-.", linewidth=2)

plt.show()