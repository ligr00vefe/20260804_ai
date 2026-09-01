import matplotlib.pyplot as plt
import numpy as np
import random

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


def get_random3():
    list_result = []
    list_a = [1, 2, 3]

    while len(list_result) < 3:
        tmp = random.choice(list_a)
        add_sign = False
        for i in range(len(list_result)):
            if tmp == list_result[i]:
                add_sign = True;
                break
        if add_sign == False:
            list_result.append(tmp)
    return list_result


xdata = [ '1st', '2st', '3rd', '4th', '5th']
y1data = [90,82,75,58,78]
plt.title('Bar 챠트', loc='left', pad=20)
plt.bar(xdata, y1data)
plt.show()


x = np.arange(3)
years = ['2021', '2022', '2023']
values1 = [210, 430, 560]
values2 = [330, 640, 250]
values3 = [720, 520, 100]
values4 = [550, 430, 750]


plt.bar(x, values1, color='r')
plt.bar(x, values2, color='b')
plt.xticks(x, years)
plt.show()

# 막대 너비 설정
width = 0.35

# x - width/2 와 x + width/2 로 위치를 나란히 오프셋
plt.bar(x - width / 2, values1, width=width, color="r", label="Value 1")
plt.bar(x + width / 2, values2, width=width, color="b", label="Value 2")

# X축 눈금을 중앙(x)에 맞추고 연도 라벨 적용
plt.xticks(x, years)
plt.legend()  # 범례 표시
plt.show()

# 한번에 여러개의 차트를 같이 그려 넣기
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.4)

plt.subplot(221)
plt.title('A')
plt.bar(x, values1, color='y')
plt.xticks(x, years)

plt.subplot(222)
plt.title('B')
plt.bar(x, values2, color='dodgerblue')
plt.xticks(x, years)

plt.subplot(223)
plt.title('C')
plt.bar(x, values3, color='C2')
plt.xticks(x, years)

plt.subplot(224)
plt.title('D')
plt.bar(x, values4, color='#e35f62')
plt.xticks(x, years)

plt.show()


# 2x2 형태의 서브플롯을 생성합니다.
fig, axs = plt.subplots(2, 2)
list_a = [1, 2, 3]
cnt = 1
# 각 서브플롯에 데이터를 플롯합니다.
axs[0, 0].plot([1, 2, 3], [1, 2, 3], label='Subplot 1')
axs[0, 1].plot([1, 2, 3], [3, 2, 1], label='Subplot 2')
axs[1, 0].plot([1, 2, 3], [2, 1, 3], label='Subplot 3')
axs[1, 1].plot([1, 2, 3], [1, 3, 2], label='Subplot 4')

# 각 서브플롯에 라벨과 범례를 추가합니다.
for i in range(2):
    for j in range(2):
        # 중복 허용할 때
        axs[i, j].plot([1, 2, 3],
                [random.choice(list_a) for i in range(3)],
                       label='Subplot '+str(cnt) )

        # 중복 불허할 때
        # axs[i, j].plot([1, 2, 3], get_random3(),
        #                label='Subplot ' + str(cnt))

        axs[i, j].set_xlabel('X-axis')
        axs[i, j].set_ylabel('Y-axis')
        axs[i, j].legend()
        cnt += 1

# subplots_adjust() 함수를 사용하여 여백과 서브플롯 간격을 조정합니다.
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.4)

# 그래프를 화면에 표시합니다.
plt.show()

